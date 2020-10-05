import pygame
import sys

pygame.init()
HEIGHT, WIDTH = 720, 1280
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 30
blackColor = (0, 0, 0)
whiteColor = (255, 255, 255)
ballX, ballY = HEIGHT // 2, WIDTH // 2
ballRedis = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.draw.circle(SCREEN, whiteColor, (ballX, ballY), ballRedis)
    CLOCK.tick(FPS)
    pygame.display.flip()
    SCREEN.fill(blackColor)
