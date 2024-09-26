#!/usr/bin/python3
import math
from constants import MOVE_SPEED, ROTATION_SPEED

class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def rotate(self, direction):
        self.angle += direction * ROTATION_SPEED
        self.angle %= 2 * math.pi

    def move(self, direction, game_map):
        new_x = self.x + math.cos(self.angle) * direction * MOVE_SPEED
        new_y = self.y + math.sin(self.angle) * direction * MOVE_SPEED
        
        if not game_map.is_wall(new_x, self.y):
            self.x = new_x
        if not game_map.is_wall(self.x, new_y):
            self.y = new_y