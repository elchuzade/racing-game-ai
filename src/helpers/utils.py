import pygame
import random
from src.helpers.core import *
import src.constants.constants as vals
import numpy as np


def add_new_car(cars):
    # add_new_car will add a new enemy_car on the top level of one of the lines picked randomly
    index = random.randint(0, 2)
    # Y coordinate of new cars
    y = vals.MARGIN + vals.CAR_WIDTH
    if index == 0:
        # Center of first line
        x = vals.MARGIN + vals.CAR_WIDTH/2
    elif index == 1:
        # Center of second line
        x = vals.MARGIN + vals.CAR_WIDTH/2 + vals.LINE_WIDTH
    elif index == 2:
        x = 200  # third line

    car = Car(x, y)
    cars.append(car)


def move_cars(cars):
    # move_cars calls move method of each car in cars state if the car is active
    for car in cars:
        if car.active == True:
            car.move()


def deactivate_cars(cars):
    # deactivate_cars checks if a car is outside of map boundaries and deactivates it
    for car in cars:
        # If the enemy_car has reached the bottom of any road line, deactivate it
        if car.y >= vals.HEIGHT - vals.MARGIN - vals.CAR_HEIGHT/2:
            car.active = False
    # filter out not active cars
    cars = list(filter(lambda x: (x.active != False), cars))


def draw_cars(cars):
    # draw_cars will draw each car from cars array on screen using its icon
    for car in cars:
        vals.SCREEN.blit(
            vals.ENEMY_CAR, (car.x - car.width/2, car.y - car.height/2))


def draw_my_car(my_car):
    # draw_my_car will draw my car on screen using its icon
    vals.SCREEN.blit(vals.MY_CAR, (my_car.x - my_car.width /
                                   2, my_car.y - my_car.height/2))


def draw_vertical_lines():
    # draw left vertical line to separate roads
    pygame.draw.rect(vals.SCREEN, vals.GREY,
                     (vals.LINE_WIDTH - vals.ROAD_LINE_WIDTH / 2, 0, vals.ROAD_LINE_WIDTH, vals.HEIGHT))
    # draw right vertical line to separate roads
    pygame.draw.rect(vals.SCREEN, vals.GREY, (vals.LINE_WIDTH *
                                              2 - vals.ROAD_LINE_WIDTH / 2, 0, vals.ROAD_LINE_WIDTH, vals.HEIGHT))


def map_cars_to_lines(cars, my_car):
    # lines will represent 3 arrays corresponsding to 3 vertical road lines
    lines = [[0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    for car in cars:
        # 2 is a label for enemy cars
        coord_x = car.x // vals.LINE_WIDTH
        coord_y = car.y // vals.LINE_WIDTH
        lines[int(coord_x)][int(coord_y)] = 2

    # 1 is a label for my car
    my_coord_x = my_car.x // vals.LINE_WIDTH
    my_coord_y = my_car.y // vals.LINE_WIDTH
    lines[int(my_coord_x)][int(my_coord_y)] = 1
    return lines


def find_my_position(my_car):
    # returns index of a line my car is at (0 or 1 or 2)
    return my_car.x // vals.LINE_WIDTH


def find_closest_car(lines, index):
    # find a return the distance to the first car on a line given by index
    # count is to return distance 1 step higher then amount of rows incase no cars were found in the line
    count = 1
    for i in range(len(lines[index])):
        if lines[index][len(lines[index]) - 1 - i] == 2:
            return i
        count = count + 1

    return count


def find_all_distances(lines):
    # returns an array of 3 values representing distances to the nearest cars on each road line
    all_distances = []

    distance_0 = find_closest_car(lines, 0)
    all_distances.append(distance_0)

    distance_1 = find_closest_car(lines, 1)
    all_distances.append(distance_1)

    distance_2 = find_closest_car(lines, 2)
    all_distances.append(distance_2)

    return all_distances


def choose_action(cars, my_car):
    # Decide to either go left right or stay at still and Return a tuple of decision, my_position, all_distances
    
    # Find X index of my position
    my_position = find_my_position(my_car)
    # Find state of each road line
    lines = map_cars_to_lines(cars, my_car)
    # Find distances to the nearest cars in all road lines
    all_distances = find_all_distances(lines)
    # Find the safest line
    max_index = all_distances.index(max(all_distances))

    # I am on the left most, best line on the right most
    if my_position + 1 < max_index:
        # Check if there is a car in the middle
        if all_distances[1] > 1:
            return "right", my_position, all_distances
        else:
            return "stay", my_position, all_distances
    # I am on the right most, best line on the left most
    elif my_position - 1 > max_index:
        # Check if there is a car in the middle
        if all_distances[1] > 1:
            return "left", my_position, all_distances
        else:
            return "stay", my_position, all_distances
    # I am one step to the left of the best line
    elif my_position < max_index:
        return "right", my_position, all_distances
    # I am one step to the right of the best line
    elif my_position > max_index:
        return "left", my_position, all_distances
    # I am one on the best line
    else:
        return "stay", my_position, all_distances


def perform_action(action, my_car):
    my_car.move(action)


def check_if_lost(cars, my_car):
    # For all cars on map check if x and y coordinates are equal to my_car's
    for car in cars:
        if car.x == my_car.x and car.y == my_car.y:
            pygame.quit()
            raise SystemExit


def save_data_row(data, action, my_position, all_distances):
    if action == "left":
        action_index = 0
    elif action == "stay":
        action_index = 1
    elif action == "right":
        action_index = 2
    row = []
    # Inputs
    row.append(my_position)
    row.append(all_distances[0])
    row.append(all_distances[1])
    row.append(all_distances[2])
    # Labels
    row.append(action_index)
    # Save each row to data file
    data.append(row)


def predict(input_array, model):
    # Puts input state into neural network and returns an action predicted by model
    # Convert array into model input format
    input_state = np.array([input_array])
    # Pass input through model to get prediction
    action = model.predict_classes(input_state)

    if (action == 0):
        return "left"
    elif (action == 1):
        return "stay"
    elif (action == 2):
        return "right"


def build_input_state(my_position, all_distances):
    # Turns all input variables into a single array
    return [my_position, all_distances[0], all_distances[1], all_distances[2]]
