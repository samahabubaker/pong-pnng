import pygame, sys

from ball_class import Ball

pygame.init()
HEIGHT, WIDTH = 720, 1280
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 30
blackColor = (0, 0, 0)
whiteColor = (255, 255, 255)


def updateDisplay():
    CLOCK.tick(FPS)
    pygame.display.flip()
    SCREEN.fill(blackColor)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


def main():
    ball = Ball(WIDTH, HEIGHT)
    while True:
        events()

        ball.bounceUp()
        ball.bounceRight()
        ball.bounceDown()
        ball.bounceLeft()

        ball.move()
        ball.draw(SCREEN)

        updateDisplay()


main()
