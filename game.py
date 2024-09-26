#!/usr/bin/python3
import sdl2
import sdl2.ext
import sdl2.sdlgfx
from constants import *
from player import Player
from map import Map
from raycasting import cast_rays
from textures import Textures

class Game:
    def __init__(self, map_file):
        sdl2.ext.init()
        self.window = sdl2.ext.Window("Maze Game", size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.textures = Textures()  # Create Textures instance once
        self.renderer = sdl2.ext.Renderer(self.window)
        self.player = Player(2.5, 2.5, 0)
        self.map = Map(map_file)
        self.show_map = False
        
    def run(self):
        running = True
        while running:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_m:
                        self.show_map = not self.show_map

            self.handle_input()
            self.renderer.clear()
            self.draw_scene()
            if self.show_map:
                self.draw_map()
            self.renderer.present()

        sdl2.ext.quit()

    def handle_input(self):
        keys = sdl2.SDL_GetKeyboardState(None)
        
        if keys[sdl2.SDL_SCANCODE_LEFT]:
            self.player.rotate(-1)
        if keys[sdl2.SDL_SCANCODE_RIGHT]:
            self.player.rotate(1)
        if keys[sdl2.SDL_SCANCODE_W]:
            self.player.move(1, self.map)
        if keys[sdl2.SDL_SCANCODE_S]:
            self.player.move(-1, self.map)

    def draw_scene(self):
        rays = cast_rays(self.player, self.map)
        for i, (distance, wall_type, angle) in enumerate(rays):
            height = SCREEN_HEIGHT / (distance * math.cos(self.player.angle - angle))
            texture = self.textures.get_texture(wall_type)
            texture_x = int((self.player.x + self.player.y + distance * math.cos(angle) + distance * math.sin(angle)) * TEXTURE_SIZE) % TEXTURE_SIZE
            wall_column = texture.subsurface((texture_x, 0, 1, TEXTURE_SIZE))
            self.renderer.copy(wall_column, dstrect=(i * SCALE, (SCREEN_HEIGHT - height) // 2, SCALE, height))

        # Draw floor
        self.renderer.fill((0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2), sdl2.ext.Color(50, 50, 50))

    def draw_map(self):
        scale = 5
        for y in range(self.map.height):
            for x in range(self.map.width):
                if self.map.is_wall(x, y):
                    self.renderer.fill((x * scale, y * scale, scale - 1, scale - 1), sdl2.ext.Color(255, 255, 255))

        px, py = int(self.player.x * scale), int(self.player.y * scale)
        sdl2.sdlgfx.filledCircleRGBA(self.renderer.sdlrenderer, px, py, 2, 255, 0, 0, 255)
        sdl2.sdlgfx.lineRGBA(self.renderer.sdlrenderer, px, py,
                             px + int(math.cos(self.player.angle) * 10),
                             py + int(math.sin(self.player.angle) * 10),
                             0, 255, 0, 255)