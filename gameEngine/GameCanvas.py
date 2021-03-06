import pygame

# This class manage the game screens


# Create the game screen
class GameCanvas:
    __height = 0
    __width = 0

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def start_screen(self, screen_name):
        screen = pygame.display.set_mode((self.__height, self.__width))
        assert screen is not None, "Can't start Game without a Game Window"

        pygame.display.set_caption(screen_name)
        return screen
