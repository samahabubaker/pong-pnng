import pygame


class PlayerLeft:
    def __init__(self, displayWidth):
        self.maxVelocity = 20
        self.velocity = pygame.math.Vector2() * self.maxVelocity // 2
        self.WIDTH, self.Height = 20, 100
        self.position = pygame.math.Vector2(displayWidth - self.WIDTH , (720/2)-(self.Height/2))
        self.color = (255, 255, 255)

    def LockAtDisplayHeight(self, displayHeight):
        if self.position.y < 0:
            self.position.y = 0
        elif self.position.y + self.Height > displayHeight:
            self.position.y = displayHeight - self.Height

    def moveStepUp(self):
        self.position.y -= self.maxVelocity

    def moveStepDown(self):
        self.position.y += self.maxVelocity

    def draw(self, screen):
        rect = pygame.rect.Rect((self.position.x, self.position.y), (self.WIDTH, self.Height))
        pygame.draw.rect(screen, self.color, rect)
