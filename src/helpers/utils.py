import random
from helpers.core import *
import src.constants as vals


def addNewCar(cars, lines):
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
