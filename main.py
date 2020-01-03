import pygame
from keras.models import load_model

from helpers.core import *
import src.constants.constants as vals

pygame.init()

# Size is the game screen size in pixels
size = width, height = vals.WIDTH, vals.HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.flip()
# Clock is set to keep track of frames
clock = pygame.time.Clock()

my_car = pygame.image.load('./img/my_car.png')
enemy_car = pygame.image.load('./img/enemy_car.png')

cars = []

data = []

