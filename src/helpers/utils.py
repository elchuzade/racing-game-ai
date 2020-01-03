import random
from helpers.core import *
import src.constants.constants as vals


def add_new_car(cars, lines):
    # add_new_car will add a new enemy_car on the top level of one of the lines picked randomly
    index = random.randint(0, 2)
    # Y coordinate of new cars
    y = vals.MARGIN + vals.CAR_WIDTH
    if index == 0:
        # Center of first line
        x = vals.MARGIN + vals.CAR_WIDTH/2
    elif index == 1:
        # Center of second line
        x = vals.MARGIN + vals.CAR_WIDTH/2 + vals.DISTANCE_BETWEEN_LINS
    elif index == 2:
        x = 200  # third line

    car = Car(x, y)
    cars.append(car)
    return cars


def move_cars(cars):
    # move_cars calls move method of each car in cars state if the car is active
    for car in cars:
        if car.active == True:
            car.move()

    return cars


def deactivate_cars(cars):
    # deactivate_cars checks if a car is outside of map boundaries and deactivates it
    for car in cars:
        # If the enemy_car has reached the bottom of any road line, deactivate it
        if car.y >= vals.HEIGHT - vals.MARGIN - vals.CAR_HEIGHT/2:
            car.active = False

    return cars
