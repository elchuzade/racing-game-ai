import pygame
from keras.models import load_model

from helpers.core import *

# Colors in a format accepted by pygame
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (150, 150, 150)
GREEN = (0, 255, 0)

pygame.init()

# Size is the game screen size in pixels
size = width, height = 240, 600
screen = pygame.display.set_mode(size)
pygame.display.flip()
# Clock is set to keep track of frames
clock = pygame.time.Clock()

my_car = pygame.image.load('./img/my_car.png')
enemy_car = pygame.image.load('./img/enemy_car.png')

cars = []

data = []

