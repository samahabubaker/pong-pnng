import pygame
import sys

pygame.init()
HEIGHT, WIDTH = 720, 1280
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 30
blackColor = (0, 0, 0)
whiteColor = (255, 255, 255)
ballV = 5
ballX, ballY = WIDTH // 2, HEIGHT // 2
ballVx, ballVy = ballV, -ballV
ballRedis = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    ballX += ballVx
    ballY += ballVy
    pygame.draw.circle(SCREEN, whiteColor, (ballX, ballY), ballRedis)
    CLOCK.tick(FPS)
    pygame.display.flip()
    SCREEN.fill(blackColor)
