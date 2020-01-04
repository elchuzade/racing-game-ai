import constants.constants as vals


class Car:
    # Car class is representing common values of all cars in the game
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # width is originating from car image width
        self.width = vals.CAR_WIDTH
        # height is originating from car image width
        self.height = vals.CAR_HEIGHT


class My_car(Car):
    # My_car class specifies distinct features of player's car
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, direction):
        # move method allows to move the car to the left or right
        # 40 is the distance form the left wall to the center of the 1st road line
        if direction == "left" and self.x > vals.MARGIN + vals.LINE_WIDTH/2:
            # 80 is the distance between the road lines
            self.x = self.x - vals.CAR_HEIGHT
        elif direction == "right" and self.x < vals.WIDTH - vals.CAR_WIDTH:
            self.x = self.x + vals.CAR_HEIGHT


class Enemy_car(Car):
    # Enemy_car class specifies distinct features of all enemy cars
    def __init__(self, x, y):
        super().__init__(x, y)
        # active bool will help to remove the car from the state
        self.active = True

    def move(self):
        # move method descends a car by its height ( 80px )
        self.y = self.y + self.height

    def deactivate(self):
        # deactivate method changes car's state to be removed later
        self.active = False
