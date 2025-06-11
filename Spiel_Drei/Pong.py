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
    def __init__(self, position_x, position_y, durchmesser, farbe, bewegung_x, bewegung_y):
        self.position_x = position_x
        self.position_y = position_y
        self.durchmesser = durchmesser
        self.farbe = farbe
        self.bewegung_x = bewegung_x
        self.bewegung_y = bewegung_y
    
    def bewegung(self):
        self.position_x += self.bewegung_x
        self.position_y += self.bewegung_y

        if self.position_x > fensterbreite - self.durchmesser or self.position_x < 0:
            self.bewegung_x *=-1
        if self.position_y > fensterhöhe - self.durchmesser or self.position_y < 0: 
            self.bewegung_y *=-1
    
    def draw(self):
        pygame.draw.ellipse(screen, self.farbe, [self.position_x, self.position_y, self.durchmesser, self.durchmesser])

def main():
    ball = Ball(320, 240, 20, weiss, 4, 4)
    spielaktiv = True

    while spielaktiv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False

        screen.fill(schwarz)

        ball.bewegung()
        ball.draw()

        pygame.display.flip()
        clock.tick(60)


    pygame.quit()


if __name__ =="__main__":
    main()