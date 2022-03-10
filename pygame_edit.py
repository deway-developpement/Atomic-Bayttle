import pygame 
from tools.tools import animation_Manager
from game import Camera
from typing import Union

# rewrite of get_pos to send now the pos in the virtual surface and not the screen.
def get_pos(func):
    def wrap(abs=False):
        if abs:
            return func()
        else:
            coord = func()
            return Camera.to_virtual(*coord)
    return wrap

pygame.mouse.get_pos = get_pos(pygame.mouse.get_pos)