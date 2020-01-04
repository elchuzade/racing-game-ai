import pygame
from keras.models import load_model
from src.helpers.utils import *
from src.helpers.core import *
import src.constants.constants as vals

model = load_model('./models/categorical_crossentropy_10k.h5')

pygame.init()

pygame.display.flip()
# Clock is set to keep track of frames
clock = pygame.time.Clock()

cars = []

data = []

my_car = My_car(vals.MY_CAR_X, vals.MY_CAR_Y)

counter = 0
while 1:
    # limit runtime speed to 30 frames/second
    clock.tick(30)
    pygame.event.pump()
    for event in pygame.event.get():
                # Look for any button press action
        if event.type == pygame.KEYDOWN:
            # Press Left key to move my_car to left
            if event.key == pygame.K_LEFT:
                my_car.move("left")
            # Press Right key to move my_car to right
            elif event.key == pygame.K_RIGHT:
                my_car.move("right")
            # Press Escape key to quit game
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit

                # Quit the game if the X symbol is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        # Build up a black screen as a game background
    vals.SCREEN.fill(vals.BLACK)
    # Draw two road separater lines
    draw_vertical_lines()
    # Remove cars that are out of map boundaries
    deactivate_cars(cars)
    
	# Draw cars
    draw_cars(cars)
    # Draw player car
    draw_my_car(my_car)
    check_if_lost(cars, my_car)

	# Increase a frame counter
    counter += 1
    # Perform this action every frame
    if counter % 1 == 0:
        # Collect data by playing autopilot mode
        autopilot(data, cars, my_car)
