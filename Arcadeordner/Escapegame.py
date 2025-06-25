import pygame
import random
import sys 
from collections import deque
import serial
import serial.tools.list_ports
titelgröße=30
ROWS=20
COLS=20
BREITE=COLS*titelgröße
HOEHE=ROWS*titelgröße
FPS=10

WEISS=(255,255,255)
SCHWARZ=(0,0,0)
GRUEN=(0,200,0)
ROT=(200,0,0)
GRAU=(200,200,200)
class Raspberry:
    def __init__ (self, baudrate=9600, timeout=0.1):
        self.port = self.get_com_port()
        self.ser = None 
        if self.port:
            try:
                self.ser = serial.Serial(self.port, baudrate, timeout=timeout)
            except Exception as e:
                self.ser = None
    
    def get_com_port(self):
        ports = list(serial.tools.list_ports.comports())
        com_ports = []

        for p in ports:
            if p.device.startswith('COM'):
                try:
                    num = int(p.device[3:])
                    com_ports.append((num, p.device))
                except ValueError:
                    pass
        if not com_ports:
            return None
        
        com_ports.sort(key=lambda x: x[0], reverse=True)
        return com_ports[0][1]
    
    def readline(self):
        if self.ser and self.ser.in_waiting:
            try:
                line = self.ser.readline().decode().strip()
                return line
            except Exception as e:
                return None
        return None
    
    def close(self):
        if self.ser:
            self.ser.close()
class Map:
    def __init__(self, rows, cols):
        self.rows=rows
        self.cols=cols
        self.grid=self.generate_map()
    def generate_map(self):
        grid=[]
        for r in range(self.rows):
            row=[]
            for i in range(self.cols):
                if r==0 or i==0 or r==self.rows-1 or i==self.cols-1:
                    row.append(1) # Wand außenrum
                else:
                    if random.random()<0.2:
                        row.append(1) #20% Wahrscheinlichkeit für Wand
                    else:
                        row.append(0) #Weg
            grid.append(row)
        return grid
    def draw(self, screen):
        for r in range(self.rows):
            for i in range(self.rows):
                farbe = SCHWARZ if self.grid[r][i]==1 else WEISS
                pygame.draw.rect(screen, farbe,(i*titelgröße, r*titelgröße, titelgröße, titelgröße))
                pygame.draw.rect(screen, GRAU,(i*titelgröße, r*titelgröße, titelgröße, titelgröße), 1)
class Spieler:
    def __init__(self, map_obj):
        self.map=map_obj
        self.x,self.y=1,1 
    def bewegen(self, dx, dy):
        nx, ny=self.x + dx, self.y+dy
        if self.map.grid[ny][nx]==0:
            self.x,self.y=nx, ny
    def draw(self, screen):
        pygame.draw.rect(screen, GRUEN,(self.x*titelgröße, self.y*titelgröße, titelgröße, titelgröße))
class Gegner:
    def __init__(self, map_obj):
        self.map=map_obj
        self.x ,self.y=COLS-2, ROWS-2
    def bfs(self ,start, goal):
        queue=deque([start])
        besucht={start: None}
        while queue:
            current=queue.popleft()
            if current== goal:
                break
            x, y=current
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny=x+dx, y+dy
                if 0<=nx<self.map.cols and 0<=ny<self.map.rows:
                    if self.map.grid[ny][nx]==0 and (nx, ny) not in besucht:
                        besucht[(nx, ny)]=current
                        queue.append((nx, ny))
        path=[]
        current=goal
        while current and current in besucht:
            path.insert(0 ,current)
            current=besucht[current]
        return path[1:] if len(path) > 1 else[]
    def update(self, player_pos):
        path=self.bfs((self.x, self.y), player_pos)
        if path:
            self.x, self.y =path[0]
    def draw(self, screen):
        pygame.draw.rect(screen,ROT, (self.x*titelgröße, self.y*titelgröße, titelgröße, titelgröße))
class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((BREITE, HOEHE))
        pygame.display.set_caption("Labyrinthspiel")
        self.clock=pygame.time.Clock()
        self.font=pygame.font.SysFont(None, 40)
        self.map=Map(ROWS, COLS)
        self.spieler=Spieler(self.map)
        self.gegner=Gegner(self.map)
        self.running=True
        self.tastatur_player1=(0,0)
        self.raspberry = Raspberry()
        self.startzeit=pygame.time.get_ticks()
        self.lebenszeit=0
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.input_handling()
            self.update()
            self.draw()
        self.game_over()
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    def input_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_w:
                    self.tastatur_player1 = (0, -1)
                elif event.key == pygame.K_s:
                    self.tastatur_player1 = (0,1)
                elif event.key == pygame.K_a:
                    self.tastatur_player1 = (-1,0)
                elif event.key == pygame.K_d:
                    self.tastatur_player1 = (1,0)
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    self.tastatur_player1 = (0,0)
                if event.key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d):
                    self.tastatur_player2 = (0,0)
    
    def raspberry_input(self):
        line = self.raspberry.readline()
        if line:
            try:
                w, s, a, d, escape, enter = map(int, line.split(','))
                dx = -1 if a else (1 if d else 0)
                dy = -1 if w else (1 if s else 0)
                self.tastatur_player1=(dx, dy)

                if escape:
                    self.running = False
 
            except Exception as e:
                pass
    def update(self):
        if isinstance(self.tastatur_player1, tuple):
            dx, dy=self.tastatur_player1
            self.spieler.bewegen(dx,dy)
        self.gegner.update((self.spieler.x, self.spieler.y))
        if self.gegner.x==self.spieler.x and self.gegner.y ==self.spieler.y:
            self.lebenszeit=(pygame.time.get_ticks()-self.startzeit)//1000
            self.running=False
    def draw(self):
        self.screen.fill(SCHWARZ)
        self.map.draw(self.screen)
        self.spieler.draw(self.screen)
        self.gegner.draw(self.screen)
        aktuelle_zeit=(pygame.time.get_ticks()-self.startzeit)//1000
        timertxt=self.font.render(f"Zeit: {aktuelle_zeit}s", True, (255,255,0))
        self.screen.blit(timertxt, (10, 10))
        pygame.display.flip()
    def game_over(self):
        self.screen.fill(SCHWARZ)
        text1=self.font.render("Game Over!", True, ROT)
        text2=self.font.render(f"Überlebt: {self.lebenszeit} Sekunden", True, WEISS)
        text3=self.font.render("Zum beenden beliebige Taste drücken...", True, GRAU)
        self.screen.blit(text1, (BREITE//2-text1.get_width()//2, HOEHE//2-60))
        self.screen.blit(text2, (BREITE//2-text2.get_width()//2, HOEHE//2))
        self.screen.blit(text3, (BREITE//2-text3.get_width()//2, HOEHE//2+40))
        pygame.display.flip()
        warten=True
        while warten:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    warten=False
        pygame.quit()
        sys.exit()
def main():
    maingame = Game()
    maingame.run()
if __name__=="__main__":
    Game().run()



                        