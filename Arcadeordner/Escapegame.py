import pygame
import random
import sys 
from collections import deque
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
        self.map=Map(ROWS, COLS)
        self.spieler=Spieler(self.map)
        self.gegner=Gegner(self.map)
    def run(self):
        while True:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.spieler.bewegen(-1,0)
        if keys[pygame.K_RIGHT]:
            self.spieler.bewegen(1,0)
        if keys[pygame.K_UP]:
            self.spieler.bewegen(0,-1)
        if keys[pygame.K_DOWN]:
            self.spieler.bewegen(0,1)
    def update(self):
        self.gegner.update((self.spieler.x, self.spieler.y))
    def draw(self):
        self.screen.fill(SCHWARZ)
        self.map.draw(self.screen)
        self.spieler.draw(self.screen)
        self.gegner.draw(self.screen)
        pygame.display.flip()
if __name__=="__main__":
    Game().run()



                        