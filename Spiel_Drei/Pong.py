import pygame
import serial
import random
import math

ser= serial.Serial('COM5', 9600, timeout=0.1)

pygame.init()

orange = ( 255, 140, 0)
rot = (255, 0, 0)
grün = (0, 255, 0)
schwarz = (0, 0, 0)
weiss = (255, 255, 255)

fensterhöhe = 480
fensterbreite = 640
screen = pygame.display.set_mode((fensterbreite, fensterhöhe))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)

class Ball:
    def __init__(self, ball_position_x, ball_position_y, ball_durchmesser, ball_farbe, ball_bewegung_x, ball_bewegung_y):
        self.ball_position_x = ball_position_x
        self.ball_position_y = ball_position_y
        self.ball_durchmesser = ball_durchmesser
        self.ball_farbe = ball_farbe
        self.ball_bewegung_x = ball_bewegung_x
        self.ball_bewegung_y = ball_bewegung_y
    
    def bewegung(self):
        self.ball_position_x += self.ball_bewegung_x
        self.ball_position_y += self.ball_bewegung_y

        if self.ball_position_x > fensterbreite - self.ball_durchmesser or self.ball_position_x < 0:
            self.ball_bewegung_x *=-1
        if self.ball_position_y > fensterhöhe - self.ball_durchmesser or self.ball_position_y < 0: 
            self.ball_bewegung_y *=-1
    
    def reset(self):
        self.ball_position_x = fensterbreite // 2
        self.ball_position_y = fensterhöhe // 2

        geschwindigkeit = 5


        while True:
            winkel = random.uniform(0, 2 * math.pi)
            x = math.cos(winkel)
            y = math.sin(winkel)

            if 0.4 < abs(x) < 0.95:
                break

        self.ball_bewegung_x = geschwindigkeit * x
        self.ball_bewegung_y = geschwindigkeit * y
    
    def draw(self):
        pygame.draw.ellipse(screen, self.ball_farbe, [self.ball_position_x, self.ball_position_y, self.ball_durchmesser, self.ball_durchmesser])

class Player:
    def __init__(self, player_position_x, player_position_y, player_breite, player_höhe, player_farbe, player_bewegung_y):
        self.player_position_x = player_position_x
        self.player_position_y = player_position_y
        self.player_breite = player_breite
        self.player_höhe = player_höhe
        self.player_farbe = player_farbe
        self.player_bewegung_y = player_bewegung_y
    
    def bewegung(self):
        if self.player_bewegung_y != 0:
            self.player_position_y += self.player_bewegung_y
        
        if self.player_position_y < 0:
            self.player_position_y = 0
        
        if self.player_position_y > fensterhöhe - self.player_höhe:
            self.player_position_y = fensterhöhe - self.player_höhe
    
    def reset(self):
        self.player_position_y = fensterhöhe // 2 - self.player_höhe // 2

    def draw(self):
        pygame.draw.rect(screen, self.player_farbe, [self.player_position_x, self.player_position_y, self.player_breite, self.player_höhe])

class Spielstand:
    def __init__(self, font_size=50, font_color=(0, 0, 0)):
        self.punkte_player1 = 0
        self.punkte_player2 = 0
        self.font = pygame.font.SysFont(None, font_size)
        self.font_color = font_color

    def draw (self, screen):
        text1 = self.font.render(str(self.punkte_player1), True, self.font_color)
        text2 = self.font.render(str(self.punkte_player2), True, self.font_color)
        screen.blit(text1, (fensterbreite // 4, 20))
        screen.blit(text2, (fensterbreite *3// 4, 20))

    def player1_punkt(self):
        self.punkte_player1 +=1
    
    def player2_punkt(self):
        self.punkte_player2 +=1
    
    def reset(self):
        self.punkte_player1 = 0
        self.punkte_player2 = 0

class Maingame:
    def __init__(self):
        self.ball = Ball(320, 240, 20, weiss, 0, 0)
        self.ball.reset()
        self.player1 = Player(100, 100, 20, 60, rot, 0)
        self.player2 = Player(540, 100 ,20, 60, weiss, 0)
        self.spielstand = Spielstand()
        self.tastatur_player1 = 0
        self.tastatur_player2 = 0
        self.running = True
    
    def input_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.tastatur_player1 = -5
                elif event.key == pygame.K_s:
                    self.tastatur_player1 = 5
                elif event.key == pygame.K_i:
                    self.tastatur_player2 = -5
                elif event.key == pygame.K_k:
                    self.tastatur_player2 = 5
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    self.tastatur_player1 = 0
                if event.key in (pygame.K_i, pygame.K_k):
                    self.tastatur_player2 = 0
    
    def raspberry_input(self):
        try:
            if ser.in_waiting:
                line = ser.readline().decode().strip()
                if line:
                    w, s, i, k = map(int, line.split(','))
                    self.player1.player_bewegung_y = -5 if w else(5 if s else 0)
                    self.player2.player_bewegung_y = -5 if i else(5 if k else 0)
                else:
                    self.player1.player_bewegung_y = self.tastatur_player1
                    self.player2.player_bewegung_y = self.tastatur_player2
        except Exception as e:
            print("Fehler bein Lesen der Seriellen Schnittstelle", e)
    
    def kollision(self):
        ball_rect = pygame.Rect(self.ball.ball_position_x, self.ball.ball_position_y, self.ball.ball_durchmesser, self.ball.ball_durchmesser)
        player1_rect = pygame.Rect(self.player1.player_position_x, self.player1.player_position_y, self.player1.player_breite, self.player1.player_höhe)
        player2_rect = pygame.Rect(self.player2.player_position_x, self.player2.player_position_y, self.player2.player_breite, self.player2.player_höhe)

        if ball_rect.colliderect(player1_rect):
            self.ball.ball_bewegung_x = abs(self.ball.ball_bewegung_x) 

        if ball_rect.colliderect(player2_rect):
            self.ball.ball_bewegung_x = -abs(self.ball.ball_bewegung_x) 

        if self.ball.ball_position_x < 0:
            self.spielstand.player2_punkt()
            self.ball.reset()

        if self.ball.ball_position_x > fensterbreite - self.ball.ball_durchmesser:
            self.spielstand.player1_punkt()
            self.ball.reset()
    
    def check_win(self):
        if self.spielstand.punkte_player1 >= 5 or self.spielstand.punkte_player2 >=5:
            gewinner_text = "Spieler 1 hat Gewonnen!" if self.spielstand.punkte_player1 >=5 else "Spieler 2 hat Gewonnen"
            font = pygame.font.SysFont(None, 60)
            text_surface = font.render(gewinner_text, True, schwarz)
            screen.fill(weiss)
            screen.blit(text_surface, (fensterbreite // 2 - text_surface.get_width() // 2, fensterhöhe // 2 -30))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.spielstand.reset()
            self.ball.reset()
            self.player1.reset()
            self.player2.reset()

    def update(self):
        self.player1.player_bewegung_y = self.tastatur_player1
        self.player2.player_bewegung_y = self.tastatur_player2
        self.raspberry_input()
        self.ball.bewegung()
        self.player1.bewegung()
        self.player2.bewegung()
        self.kollision()
        self.check_win()
    
    def draw(self):
        screen.fill(orange)
        self.ball.draw()
        self.player1.draw()
        self.player2.draw()
        self.spielstand.draw(screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.input_handling()
            self.update()
            self.draw()
            clock.tick(60)
        pygame.quit()



                                 
def main():
    maingame = Maingame()
    maingame.run()

if __name__ =="__main__":
    main()