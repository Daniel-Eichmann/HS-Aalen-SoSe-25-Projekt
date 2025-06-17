import pygame

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

    def draw(self):
        pygame.draw.rect(screen, self.player_farbe, [self.player_position_x, self.player_position_y, self.player_breite, self.player_höhe])


def main():
    ball = Ball(320, 240, 20, weiss, 4, 4)
    player1 = Player(100, 100, 20, 60, rot, 0)
    player2 = Player(540, 100, 20, 60, weiss, 0)
    spielaktiv = True

    while spielaktiv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.player_bewegung_y = -5
                if event.key == pygame.K_s:
                    player1.player_bewegung_y = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1.player_bewegung_y = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    player2.player_bewegung_y = -5
                if event.key == pygame.K_k:
                    player2.player_bewegung_y = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_i or event.key == pygame.K_k:
                    player2.player_bewegung_y = 0

        screen.fill(schwarz)

        ball.bewegung()
        ball.draw()

        player1.bewegung()
        player1.draw()
        player2.bewegung()
        player2.draw()

        pygame.display.flip()
        clock.tick(60)


    pygame.quit()


if __name__ =="__main__":
    main()