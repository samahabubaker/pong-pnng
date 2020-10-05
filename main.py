import pygame
import sys

pygame.init()
HEIGHT, WIDTH = 720, 1280
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 30
blackColor = (0, 0, 0)
whiteColor = (255, 255, 255)
ballVelocity = 5
ballX, ballY = WIDTH // 2, HEIGHT // 2
ballVelocityX, ballVelocityY = ballVelocity, -ballVelocity
ballRedis = 5


def ballMove():
    global ballX, ballY
    ballX += ballVelocityX
    ballY += ballVelocityY


def ballDraw():
    pygame.draw.circle(SCREEN, whiteColor, (ballX, ballY), ballRedis)


def updateDisplay():
    CLOCK.tick(FPS)
    pygame.display.flip()
    SCREEN.fill(blackColor)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


def ballBounceUp():
    global ballVelocityY
    if ballY < 0:
        ballVelocityY = -ballVelocityY


while True:
    events()

    ballBounceUp()
    if ballX + ballRedis > WIDTH:
        ballVelocityX = - ballVelocityX
    ballMove()
    ballDraw()
    updateDisplay()
