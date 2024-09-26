#!/usr/bin/python3
from map_parser import parse_map

class Map:
    def __init__(self, map_file):
        self.map = parse_map(map_file)
        self.width = len(self.map[0])
        self.height = len(self.map)
    
    def is_wall(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[int(y)][int(x)] != '0'
        return True

    def get_wall_type(self, x, y):
        return self.map[int(y)][int(x)]