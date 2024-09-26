# textures.py
import sdl2
import sdl2.ext

class Textures:
    def __init__(self):
        self.textures = {
            'N': self.load_texture('assets/wall_n.jpeg'),
            'S': self.load_texture('assets/wall_s.jpeg'),
            'E': self.load_texture('assets/wall_e.jpeg'),
            'W': self.load_texture('assets/wall_w.jpeg'),
        }

    def load_texture(self, path):  
        surface = sdl2.ext.load_image(path)
        if surface is None:
            print(f"Failed to load texture: {path}")
        print(f"Pssing surface to Texture: {surface}")
        texture = sdl2.ext.Texture(surface)
        return texture

    def get_texture(self, direction):
        return self.textures[direction]