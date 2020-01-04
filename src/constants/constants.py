import pygame

# Road line width is for two vertical lines
ROAD_LINE_WIDTH = 10
# Margin of the useful map area
MARGIN = 20
# Width of the game screen
WIDTH = 240
# Height of the game screen
HEIGHT = 600
# Width of any car on the map
CAR_WIDTH = 40
# Height of any car on the map
CAR_HEIGHT = 80
# Distance between centers of vertical lines
LINE_WIDTH = 80
# Initial coordinates of my car
MY_CAR_X = MARGIN + CAR_WIDTH/2 + LINE_WIDTH
MY_CAR_Y = HEIGHT - MARGIN - CAR_HEIGHT/2

# Colors in a format accepted by pygame
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (150, 150, 150)
GREEN = (0, 255, 0)

# Size is the game screen size in pixels
SIZE = width, height = WIDTH, HEIGHT
SCREEN = pygame.display.set_mode(SIZE)

MY_CAR = pygame.image.load('./src/img/my_car.png')
ENEMY_CAR = pygame.image.load('./src/img/enemy_car.png')
