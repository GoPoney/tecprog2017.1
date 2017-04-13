import pygame
from gameEngine.GameObject import *

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameBoard:
    grid = []

    def __init__(self, width=0, height=0, margin=0):
        self.width = width
        self.height = height
        self.margin = margin

        for row in range(10):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(10):
                # Append a cell
                self.grid[row].append(0)

    def draw(self, screen):
        for row in range(5):
            for column in range(10):
                color = WHITE
                if self.grid[row][column] == 1:
                    color = GREEN

                pygame.draw.rect(screen,
                                 color,
                                 [(self.margin + self.width) * column + self.margin,
                                  (self.margin + self.height) * row + self.margin,
                                  self.width,
                                  self.height])


    def update(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (self.width + self.margin)
                row = pos[1] // (self.height + self.margin)
                # Set that location to one
                self.grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)