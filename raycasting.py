#!/usr/bin/python3
import math
from constants import *

def cast_rays(player, game_map):
    rays = []
    start_angle = player.angle - HALF_FOV_RAD
    
    for ray in range(CASTED_RAYS):
        angle = start_angle + ray * STEP_ANGLE
        distance, wall_type = cast_single_ray(player.x, player.y, angle, game_map)
        rays.append((distance, wall_type, angle))
    
    return rays

def cast_single_ray(x, y, angle, game_map):
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)

    distance = 0
    while True:
        distance += 0.01
        target_x = x + distance * cos_a
        target_y = y + distance * sin_a

        if game_map.is_wall(target_x, target_y):
            wall_type = game_map.get_wall_type(target_x, target_y)
            return distance, wall_type