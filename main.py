import pygame
import sys

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


class Ball:
    def __init__(self):
        self.Velocity = 5
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.velocityX, self.velocityY = self.Velocity, -self.Velocity
        self.Redis = 5

    def bounceUp(self):
        if self.y < 0:
            self.velocityY = -self.velocityY

    def bounceRight(self):
        if self.x + self.Redis > WIDTH:
            self.velocityX = - self.velocityX

    def bounceDown(self):

        if self.y + self.Redis > HEIGHT:
            self.velocityY = - self.velocityY

    def bounceLeft(self):
        if self.x < 0:
            self.velocityX = -self.velocityX

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

    def draw(self, screen=SCREEN, color=whiteColor):
        pygame.draw.circle(screen, color, (self.x, self.y), self.Redis)


def main():
    ball = Ball()
    while True:
        events()

        ball.bounceUp()
        ball.bounceRight()
        ball.bounceDown()
        ball.bounceLeft()

        ball.move()
        ball.draw()

        updateDisplay()


if __name__ == '__main__':
    main()
