#!/usr/bin/python3
import math

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FOV = 60  # Field of view
HALF_FOV = FOV / 2
FOV_RAD = math.radians(FOV)
HALF_FOV_RAD = FOV_RAD / 2
CASTED_RAYS = 320
STEP_ANGLE = FOV_RAD / CASTED_RAYS
SCALE = SCREEN_WIDTH / CASTED_RAYS
MOVE_SPEED = 0.05
ROTATION_SPEED = 0.05

TEXTURE_SIZE = 64