import pygame
import time
import math

pygame.init()
class Colors():
    def __init__(self):
        self.red = (255,0,0)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.grey = (128, 131, 137)

class Window():
    def __init__(self):
        self.x = 800
        self.y = 600

class Ball():
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.radius = rad

    def locate(self):
        return self.x, self.y

    def update(self, x, y):
        self.x += int(x)
        self.y += int(y)
        print y

class Simulator():
    def __init__(self):
        self.font = pygame.font.SysFont(None,50)
        self.colors = Colors()
        self.window = Window()
        self.clock = pygame.time.Clock()
        self.anchor = pygame.Rect(0,0,5,5)
        self.anchor.center = (self.window.x / 2), (self.window.y / 2)
        self.simDisplay = pygame.display.set_mode(( self.window.x, self.window.y ))
        self.tick = 20.0
        self.time = self.tick / 60
        self.center = (self.window.x / 2), (self.window.y / 2)
        self.ball = pygame.Rect(self.center[0], self.center[1] + 100, 25, 25)
        self.ball.center = (self.center[0] - 250, self.center[1] - 100)
        self.gravity = 10
        self.mass = 25
        self.running = True
        self.velocityY = 0.0
        self.velocityX = 0.0
        self.k = 10
        self.damping = 2

    def update(self):
        springForceY = -self.k * (self.ball.y - self.anchor.y)
        springForceX = -self.k * (self.ball.x - self.anchor.x)

        dampY = self.damping * self.velocityY
        dampX = self.damping * self.velocityX

        forceY = springForceY + (self.mass * self.gravity) - dampY
        forceX = springForceX - dampX

        accelY = (forceY / self.mass)
        accelX = (forceX / self.mass)

        self.velocityY = int(self.velocityY + (accelY * self.time))
        self.velocityX = int(self.velocityX + (accelX * self.time))

        print 'Update V -> '+ str(self.velocityY) + ' , ' + str(self.velocityX)

        self.ball.y += int(math.ceil(self.velocityY * self.time))
        self.ball.x += int(math.ceil(self.velocityX * self.time))

        pygame.draw.rect(self.simDisplay, self.colors.black, self.anchor, 3)
        pygame.draw.line(self.simDisplay, self.colors.black, self.anchor.center, self.ball.center, 3)
        pygame.draw.circle(self.simDisplay, self.colors.red, self.ball.center , self.ball.width, 5)
        print 'Update Y -> '+ str(forceY) + ' ' + str(accelY) + ' ' + str(self.velocityY)+ ' ' + str(springForceY)
        print 'Update X -> '+ str(forceX) + ' ' + str(accelX) + ' ' + str(self.velocityX)+ ' ' + str(springForceX)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False

            self.simDisplay.fill(self.colors.white)
            self.update()
            pygame.display.update()
            self.clock.tick(int(30))

    def end(self):
        pygame.quit()
        quit()


s = Simulator()
s.run()
s.end()
