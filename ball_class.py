import pygame


class Ball:
    def __init__(self, WIDTH, HEIGHT):
        self.displayWidth, self.displayHeight = WIDTH, HEIGHT
        self.Velocity = 5
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.velocityX, self.velocityY = self.Velocity, -self.Velocity
        self.Redis = 5
        self.color = (255, 255, 255)

    def bounceUp(self):
        if self.y < 0:
            self.velocityY = -self.velocityY

    def bounceRight(self):
        if self.x + self.Redis > self.displayWidth:
            self.velocityX = - self.velocityX

    def bounceDown(self):

        if self.y + self.Redis > self.displayHeight:
            self.velocityY = - self.velocityY

    def bounceLeft(self):
        if self.x < 0:
            self.velocityX = -self.velocityX

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.Redis)
