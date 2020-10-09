from math import sin, cos, pi

import pygame

from player_right import PlayerRight


class Ball:
    def __init__(self, WIDTH, HEIGHT, startAngle=0):
        self.displayWidth, self.displayHeight = WIDTH, HEIGHT
        self.maxVelocity = 30
        self.position = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)
        angle = startAngle * pi / 180
        self.velocity = pygame.math.Vector2(int(cos(angle) * self.maxVelocity / 2),
                                            int(sin(angle) * self.maxVelocity / 2))
        self.radius = 5
        self.color = (255, 255, 255)

    def bounceUp(self):
        if self.position.y < 0:
            self.velocity.y = -self.velocity.y

    def isBouncedRight(self):
        if self.position.x + self.radius > self.displayWidth:
            return True
        return False

    def bounceDown(self):

        if self.position.y + self.radius > self.displayHeight:
            self.velocity.y = - self.velocity.y

    def isBouncedLeft(self):
        if self.position.x < 0:
            return True
        return False

    def move(self):
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, tuple(map(int, self.position)), self.radius)

    def update(self, player):
        if type(player) is PlayerRight:
            # print(f"{self.position.y=} {player.position.y=}")
            if player.position.y < self.position.y < player.position.y + player.Height:
                if self.position.x - self.radius < player.position.x + player.WIDTH:
                    relativeBallY = self.position.y - player.position.y
                    relativeCollisionPosition = relativeBallY / player.Height * 100
                    projectedAngle = 180 * relativeCollisionPosition / 100
                    pygameAngle = projectedAngle + 270
                    # print(projectedAngle)
                    pygameAngleRadian = pygameAngle * pi / 180
                    bounceVector = pygame.math.Vector2(cos(pygameAngleRadian), sin(pygameAngleRadian))
                    bouncePower = self._magnitudeOfBounce(projectedAngle)
                    amountOfVelocity = bouncePower * self.maxVelocity / 100
                    self.velocity = bounceVector * amountOfVelocity
        else:
            if player.position.y < self.position.y < player.position.y + player.Height:
                if self.position.x + self.radius > player.position.x:
                    relativeBallY = self.position.y - player.position.y
                    relativeCollisionPosition = relativeBallY / player.Height * 100
                    projectedAngle = abs((180 * relativeCollisionPosition / 100) - 180)
                    pygameAngle = projectedAngle + 270
                    print(projectedAngle)
                    pygameAngleRadian = pygameAngle * pi / 180
                    bounceVector = pygame.math.Vector2(cos(pygameAngleRadian), sin(pygameAngleRadian))
                    bouncePower = self._magnitudeOfBounce(projectedAngle)
                    amountOfVelocity = bouncePower * self.maxVelocity / 100
                    self.velocity = -bounceVector * amountOfVelocity

    def _magnitudeOfBounce(self, angle):
        i = angle / 180 * 100
        mid = 50
        if i <= mid:
            return 100 - i
        if i > mid:
            return i
