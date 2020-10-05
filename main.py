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


playerRightX, playerRightY = 20, 20
playerRightWidth, playerRightHeight = 20, 100
playerRightVelocity = 10

ball = Ball(WIDTH, HEIGHT)
while True:
    events()

    ball.bounceUp()
    ball.bounceRight()
    ball.bounceDown()
    ball.bounceLeft()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerRightY -= playerRightVelocity
    if keys[pygame.K_s]:
        playerRightY += playerRightVelocity

    if playerRightY < 0:
        playerRightY = 0
    elif playerRightY + playerRightHeight > HEIGHT:
        playerRightY = HEIGHT - playerRightHeight

        # Rect((left, top), (width, height)) -> Rect
    playerRightRect = pygame.rect.Rect((playerRightX, playerRightY), (playerRightWidth, playerRightHeight))
    pygame.draw.rect(SCREEN, whiteColor, playerRightRect)
    ball.move()
    ball.draw(SCREEN)

    updateDisplay()
