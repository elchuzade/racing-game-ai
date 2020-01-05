import pygame
from keras.models import load_model
from helpers.utils import *
from helpers.core import *
import constants.constants as vals
from data.data import *

model = load_model('./models/categorical_crossentropy.h5')

pygame.init()

SCREEN = initialize_screen()

# Clock is set to keep track of frames
clock = pygame.time.Clock()

cars = []
data = []

my_car = My_car(vals.MY_CAR_X, vals.MY_CAR_Y)

# Stop will be set True when you lose
stop = False
# Set ai_mode false if you want to play in autopilot mode to collect data
ai = False
# Set True if you want to collect state at every frame for data analytics
collect_data = True
# Decide on amount of rows after which data should be saved
rows = 20000

counter = 0
while 1:
    # limit runtime speed to 30 frames/second
    clock.tick(60)
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
    SCREEN.fill(vals.BLACK)
    # Draw two road separater lines
    draw_vertical_lines(SCREEN)
    # Remove cars that are out of map boundaries
    deactivate_cars(cars)
    # filter out not active cars
    cars = list(filter(lambda x: (x.active != False), cars))
    # check_if_lost(cars, my_car)
    # Increase a frame counter
    counter += 1
    # Perform this action every frame
    if counter % 1 == 0 and stop == False:
        if ai == True:
            # Test your ai model's performance
            ai_model(model, cars, my_car)
        else:
            # Collect data by playing autopilot mode
            autopilot(data, cars, my_car)

    # Perform this action every 2 frames
    if counter % 2 == 0 and stop == False:
        add_new_car(cars)

    # Draw cars
    draw_cars(SCREEN, cars)
    # Draw player car
    draw_my_car(SCREEN, my_car)

    if collect_data == True and stop == False:
        if counter == rows:
            save_data(data)
        elif counter <= rows:
            print("Counter - ", counter, " / ", rows)

    if (stop == False):
        stop = check_if_lost(stop, cars, my_car)
        if (stop == True):
            print("stop - ", stop)

    # update display
    pygame.display.flip()
