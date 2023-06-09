import pygame
from lib import sll
from lib import lib


class Trajectory:

    def __init__(self, surface: pygame.Surface) -> None:
        self.__surface = surface
        self.__points_list = sll.Sll()
    
    def add_point(self, x: float, y: float) -> None:
        new_point = (lib.pbround(x), lib.pbround(y))

        self.__points_list.add_to_tail(new_point)

    def draw(self, color: tuple) -> None:
        self.__points_list.traverse_from_head(
            self.__surface.set_at, color)
