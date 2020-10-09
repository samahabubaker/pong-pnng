from math import *

import pygame, sys

from ball_class import Ball
from player_left import PlayerLeft
from player_right import PlayerRight


class PongPong:
    def __init__(self):
        pygame.init()
        self.HEIGHT, self.WIDTH = 720, 1280
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.FPS = 30
        self.blackColor = (0, 0, 0)
        self.whiteColor = (255, 255, 255)
        self.ball = Ball(self.WIDTH, self.HEIGHT)
        self.playerRight = PlayerRight()
        self.playerLeft = PlayerLeft(self.WIDTH)
        self.leftScore = 0
        self.rightScore = 0

    def updateDisplay(self):
        self.CLOCK.tick(self.FPS)
        pygame.display.flip()
        self.SCREEN.fill(self.blackColor)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def addBall(self, newBall):
        self.ball = newBall

    def ballBounceDisplay(self):
        self.ball.bounceUp()
        if self.ball.isBouncedLeft():
            self.rightScore += 1
            self.ball = Ball(self.WIDTH, self.HEIGHT,startAngle=180)
            self.playerRight = PlayerRight()

        self.ball.bounceDown()
        if self.ball.isBouncedRight():
            self.leftScore += 1
            self.ball = Ball(self.WIDTH, self.HEIGHT,startAngle=0)
            self.playerLeft = PlayerLeft(self.WIDTH)
        self.ball.move()

    def main(self):
        while True:
            self.events()
            self.ballBounceDisplay()
            self.takeUsersActions()
            self.updatePlayers()
            self.updateBalls()
            self.drawBalls()
            self.drawPlayers()
            self.showScores()
            self.updateDisplay()

    def takeUsersActions(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.playerRight.moveStepUp()
        if keys[pygame.K_s]:
            self.playerRight.moveStepDown()
        if keys[pygame.K_UP]:
            self.playerLeft.moveStepUp()
        if keys[pygame.K_DOWN]:
            self.playerLeft.moveStepDown()

    def drawPlayers(self):
        self.playerRight.draw(self.SCREEN)
        self.playerLeft.draw(self.SCREEN)

    def updatePlayers(self):
        self.playerRight.LockAtDisplayHeight(self.HEIGHT)
        self.playerLeft.LockAtDisplayHeight(self.HEIGHT)

    def updateBalls(self):
        self.ball.update(self.playerRight)
        self.ball.update(self.playerLeft)

    def drawBalls(self):
        self.ball.draw(self.SCREEN)

    def showScores(self):
        fontName = pygame.font.get_default_font()
        font = pygame.font.Font(fontName, 30)
        text = f"Scores:  Left: {self.leftScore:^3}  Right: {self.rightScore:^3}"
        textImage = font.render(text, True, self.whiteColor)
        size = font.size(text)
        self.SCREEN.blit(textImage, (((self.WIDTH // 2) - (size[0] // 2)), 0))


game = PongPong()

game.main()
# while True:
#
#     if ball.position.y in range(playerRightY, playerRightY + playerRightHeight):
#         if ball.position.x - ball.radius < playerRightX + playerRightWidth:
#             relativeBallY = ball.position.y - playerRightY
#             relativeCollisionPosition = relativeBallY / playerRightHeight * 100
#             projectedAngle = 180 * relativeCollisionPosition / 100
#             pygameAngle = projectedAngle + 270
#             pygameAngleRadian = pygameAngle * pi / 180
#             bounceVector = pygame.math.Vector2(cos(pygameAngleRadian), sin(pygameAngleRadian))
#             bouncePower = magnitudeOfBounce(projectedAngle)
#             amountOfVelocity = bouncePower * ball.maxVelocity / 100
#             ball.velocity = bounceVector * amountOfVelocity
#
#     playerRightMove()
#     playerRightLockAtDisplay()
#     playerRightDraw(SCREEN)
#
#     ball.draw(SCREEN)
#
#     updateDisplay()
