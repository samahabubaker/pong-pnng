import math

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


playerRightWidth, playerRightHeight = 20, 100
playerRightX, playerRightY = 20, (HEIGHT // 2) - (playerRightHeight // 2)
playerRightVelocity = 20


def playerRightMove():
    global playerRightY
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerRightY -= playerRightVelocity
    if keys[pygame.K_s]:
        playerRightY += playerRightVelocity


def playerRightLockAtDisplay():
    global playerRightY
    if playerRightY < 0:
        playerRightY = 0
    elif playerRightY + playerRightHeight > HEIGHT:
        playerRightY = HEIGHT - playerRightHeight


def playerRightDraw(screen):
    playerRightRect = pygame.rect.Rect((playerRightX, playerRightY), (playerRightWidth, playerRightHeight))
    pygame.draw.rect(screen, whiteColor, playerRightRect)


ball = Ball(WIDTH, HEIGHT)
while True:
    events()

    ball.bounceUp()
    ball.bounceRight()
    ball.bounceDown()
    ball.bounceLeft()
    ball.move()
    if ball.y in range(playerRightY, playerRightY + playerRightHeight):
        if ball.x < playerRightX + playerRightWidth:
            relativeBallY = ball.y - playerRightY
            collisionPlace = relativeBallY / playerRightHeight * 100
            angle = 180 * collisionPlace / 100
            pygameAngle = (angle + 270)
            pygameAngleRadian = pygameAngle * math.pi / 180
            vectorX, vectorY = math.cos(pygameAngleRadian), math.sin(pygameAngleRadian)
            ball.velocityX = int(vectorX * ball.Velocity)
            ball.velocityY = int(vectorY * ball.Velocity)

    playerRightMove()
    playerRightLockAtDisplay()
    playerRightDraw(SCREEN)

    ball.draw(SCREEN)

    updateDisplay()
