import pygame
import sys
import random
Breite=800
Höhe=600
Weiß=(255,255,255)
Schwarz=(0,0,0)
Rot=(255,0,0)
Blau=(0,0,255)
class Hintergrund:
    def __init__(self):
        self.color=Weiß
    def draw(self, screen):
        screen.fill(self.color)
class Spieler:
     def __init__(self):
        self.rect=pygame.Rect(100, Höhe//2,50,50)
        self.speed=5
     def bewegen(self, keys):
        if keys [pygame.K_UP] and self.rect.top >0:
            self.rect.y-=self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom<Höhe:
            self.rect.y+=self.speed
        if keys [pygame.K_LEFT] and self.rect.left>0:
            self.rect.x-=self.speed
        if keys [pygame.K_RIGHT] and self.rect.right<Breite:
            self.rect.x +=self.speed
     def draw(self, screen):
                pygame.draw.rect(screen, Blau, self.rect)
class Hinderniss:
    def __init__(self):
        self.rect=pygame.Rect(Breite, random.randint(0, Höhe-50),50 ,50)
        self.speed=5
    def update(self):
        self.rect.x-=self.speed
    def draw(self, screen):
        pygame.draw.rect(screen, Rot, self.rect)
class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((Breite, Höhe))
        pygame.display.set_caption("Arcade")
        self.clock=pygame.time.Clock()
        self.background=Hintergrund()
        self.player=Spieler()
        self.hinderniss=[]
        self.running=True
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
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
                print("Berührung! Game Over")
                self.running=False
        self.hinderniss=[hinderniss for hinderniss in self.hinderniss if hinderniss.rect.right>0]
    def draw(self):
        self.background.draw(self.screen)
        self.player.draw(self.screen)
        for hinderniss in self.hinderniss:
            hinderniss.draw(self.screen)
        pygame.display.flip()
if __name__=="__main__":
    Game().run()




