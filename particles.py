import pygame
import random

pygame.init()
sDisplay = pygame.display.set_mode(( 1000 , 800 ))
clock = pygame.time.Clock()

# Formulas To Remember
# force = mass * acceleration
# displacement = Velocity * time
# speed = (change in position / change in time)
# acceleration = (change in speed / change in time)
# v_after = -(Elasticity) * Velocity


#Vectors: magnitude and direction -> displacement
#Scalars: just magnitude          -> velocity (no direction)

gravity = 10
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128, 131, 137)

# gravity
# wind
# collision
# alive
# onScreen
# heat
# air temperature

class Vect2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vect2):
            return Vect2(self.x + other.x, self.y + other.y)
        elif hasattr(other, "__getitem__"):
            return Vect2(self.x + other[0], self.y + other[1])
        else:
            return Vect2(self.x + other, self.y + other)
    __radd__ = __add__

    def __iadd__(self, other):
        if isinstance(other, Vect2):
            self.x += other.x
            self.y += other.y
        elif hasattr(other, "__getitem__"):
            self.x += other[0]
            self.y += other[1]
        else:
            self.x += other
            self.y += other
        return self

class Particle():
    def __init__(self, location, size):
        self.location = location
        self.size = size
        x = random.randrange(0, 1)
        y = random.randrange(0, 1)
        print (str(x), str(y))
        self.accel = Vect2(.25, 0.25)
        self.velocity = Vect2(0 , 0)

    def update(self):
        self.velocity += self.accel
        self.location += self.velocity

    def render(self):
        pygame.draw.circle(sDisplay, BLACK, (int(self.location.x), int(self.location.y)), self.size)

class ParticleContainer():
    def __init__(self, x, y, count, shape, size):
        self.particles = []
        self.count = count
        self.shape = shape
        self.size = size
        self.location = Vect2(x, y)
        self.color = RED
        self.alive = True

    def generate(self):
        for i in range(self.count):
            self.particles.append(Particle(self.location, self.size))

    def update(self):
        p_log = []
        for p in self.particles:
            p.update()
            p_log.append((p.location.x, p.location.y))
        print p_log

    def render(self):
        for p in self.particles:
            p.render()

        pygame.display.update()

    def run(self):
        i = 255
        running = True
        while running:
            self.update()
            self.render()

            clock.tick(10)


sim = ParticleContainer(800, 15, 8, "circle", 5)
sim.generate()
sim.run()
