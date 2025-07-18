import pygame
import sys
import random
import os
import subprocess
from Raspberry import Raspberry
Breite=800
Höhe=600
pygame.mixer.init()
dir_path = os.path.dirname(os.path.realpath(__file__))
levelxsound = os.path.join(dir_path,"Grafiken", "levelx.mp3")
pygame.mixer.music.load(levelxsound)
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)
#Farben
Weiß=(255,255,255)
Schwarz=(0,0,0)
Rot=(255,0,0)
Blau=(0,0,255)
Neongrün=(57, 255, 20)
dunkelgrün=(0,100,0)
Lila=(255, 0, 255)
Grau=(50,50,50)
class Hintergrund:
    def __init__(self):
        self.straße=(Grau)
        self.straßenmakierung=(Weiß)
        self.straßenrand=(dunkelgrün)
        self.spurhöhe=(Höhe-200)//3
    def draw(self, screen):
        pygame.draw.rect(screen, self.straßenrand, (0,0,Breite,100))
        pygame.draw.rect(screen, self.straßenrand, (0,Höhe-100,Breite,100))
        pygame.draw.rect(screen,self.straße, (0,100,Breite,Höhe-200))
        for i in range(1, 3):
            y=100+i*self.spurhöhe
            for x in range(0, Breite, 40):
                pygame.draw.rect(screen, self.straßenmakierung, (x,y-2,20,4))
class Spieler:
     def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))                                      #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
        pfad_grafik1 = os.path.join(dir_path,"Grafiken", "auto1.png") 
        self.auto=pygame.image.load(pfad_grafik1).convert_alpha()
        self.auto=pygame.transform.scale(self.auto, (80,80))
        self.rect=self.auto.get_rect()
        self.rect.inflate_ip(-20,-20)
        spurhöhe=(Höhe-200)//3
        start_y=100+spurhöhe+(spurhöhe-80)//2
        self.rect.topleft=(100, start_y)
        self.speed=5
     def bewegen(self, keys):
        if keys [pygame.K_UP] and self.rect.top >100:
            self.rect.y-=self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom<Höhe-100:
            self.rect.y+=self.speed
        if keys [pygame.K_LEFT] and self.rect.left>0:
            self.rect.x-=self.speed
        if keys [pygame.K_RIGHT] and self.rect.right<Breite:
            self.rect.x +=self.speed
     def draw(self, screen):
                screen.blit(self.auto, self.rect)
                pygame.draw.rect(screen,(0,255,0),self.rect, 2)
class Hinderniss:
    def __init__(self):
        self.spurhöhe=(Höhe-200)//3
        self.spur=random.randint(0,2)
        self.y_pos=100+self.spur*self.spurhöhe+(self.spurhöhe-80)//2
        dir_path = os.path.dirname(os.path.realpath(__file__))                                      #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
        pfad_grafik2 = os.path.join(dir_path,"Grafiken", "auto2.png")
        pfad_grafik3 = os.path.join(dir_path,"Grafiken", "LKW1.png")
        pfad_grafik4 = os.path.join(dir_path,"Grafiken", "Bus1.png")  
        autos=[pfad_grafik2, pfad_grafik3, pfad_grafik4]
        autoauswahl=random.choice(autos)
        self.auto2=pygame.image.load(autoauswahl).convert_alpha()
        self.auto2=pygame.transform.scale(self.auto2, (80,80))
        self.rect=self.auto2.get_rect()
        self.rect.inflate_ip(-8,-20)
        self.rect.topleft=(Breite, self.y_pos)
        self.speed=5
    def update(self):
        self.rect.x-=self.speed
    def draw(self, screen):
        screen.blit(self.auto2, self.rect)
        pygame.draw.rect(screen,(0,255,0),self.rect, 2)   #Testen des Kollisionsalgorithmus
class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((Breite, Höhe))
        pygame.display.set_caption("Arcade")
        self.clock=pygame.time.Clock()
        self.background=Hintergrund()
        self.player=Spieler()
        self.raspberry = Raspberry()
        self.hinderniss=[]
        self.running=True
        self.score=0
        self.highscore=self.lade_highscore()
        self.font=pygame.font.SysFont(None, 36)
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.input_handling()
            self.raspberry_input()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
    def update(self):
        keys=pygame.key.get_pressed()
        self.player.bewegen(keys)
        if random.randint(0, 60)==0:
            self.hinderniss.append(Hinderniss())
        for hinderniss in self.hinderniss:
            hinderniss.update()
            if self.player.rect.colliderect(hinderniss.rect):
                self.speichere_highscore()
                self.gameover()
                self.running=False
        #nur sichtbare Autos updaten
        neueliste=[]
        for hinderniss in self.hinderniss:
            hinderniss.update()
            if hinderniss.rect.right>0:
                neueliste.append(hinderniss)
                self.hinderniss=neueliste
        self.score+=1
    def draw(self):
        self.background.draw(self.screen)
        self.player.draw(self.screen)
        for hinderniss in self.hinderniss:
            hinderniss.draw(self.screen)
        score_anzeigen=self.font.render(f"Score:{self.score}", True, Lila)
        highscore_anzeigen=self.font.render(f"Highscore:{self.highscore}", True, Neongrün)
        self.screen.blit(score_anzeigen, (10,10))
        self.screen.blit(highscore_anzeigen, (10,40))
        pygame.display.flip()
    def lade_highscore(self):
        try: 
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0
    def speichere_highscore(self):
        if self.score>self.highscore:
            with open("highscore.txt", "w") as f:
                f.write(str(self.score))  
    def gameover(self):
        self.screen.fill(Schwarz)
        gameoveranzeigen=self.font.render("GAME OVER.", True, Rot)
        textposition=gameoveranzeigen.get_rect(center=(Breite//2, Höhe//2))
        self.screen.blit(gameoveranzeigen, textposition)
        pygame.display.flip()
        pygame.time.delay(3000)

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
                if event.key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d):
                    self.tastatur_player1 = (0,0)

    def raspberry_input(self):
        line = self.raspberry.readline()
        if line:
            try:
                button_names = ["w", "s", "a", "d", "escape", "enter"]
                pressed_keys = line.strip().split(',') if line.strip() else []
                values = {key: (key in pressed_keys) for key in button_names}
                w = values["w"]
                s = values["s"]
                a = values["a"]
                d = values["d"]
                escape = values["escape"]
                enter = values["enter"]
                dx = -1 if a else (1 if d else 0)
                dy = -1 if w else (1 if s else 0)
                self.tastatur_player1 = (dx, dy)
                if escape:
                    self.running = False
                if enter:
                    pass
 
            except Exception as e:
                return None
        else:
            return

def main():
    maingame = Game()
    maingame.run()
if __name__=="__main__":
    Game().run()




