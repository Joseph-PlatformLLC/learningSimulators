import pygame
pygame.init()
sDisplay = pygame.display.set_mode(( 1000 , 800 ))

# Formulas To Remember
# force = mass * acceleration
# displacement = Velocity * time
# speed = (change in position / change in time)
# acceleration = (change in speed / change in time)
# v_after = -(Elasticity) * Velocity


#Vectors: magnitude and direction -> displacement
#Scalars: just magnitude          -> velocity (no direction)


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


class Particle():
    def __init___(self):
