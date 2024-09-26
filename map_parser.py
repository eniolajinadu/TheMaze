#!/usr/bin/python3

def parse_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]