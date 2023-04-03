import random
import pygame
from pygame.locals import *
import math
from logic.floor_logic import create_floor

# PYGAME INIT & SCREEN
pygame.init()
screen_w = (pygame.display.Info().current_w)//2
screen_h = (pygame.display.Info().current_h)//2
DISPLAYSURF = pygame.display.set_mode((screen_w, screen_h))
# print(f'(W, H): {(screen_w, screen_h)}')

# VARIABLES
grid_width = 40
grid_height = 22
my_grid = create_floor(grid_width, grid_height)

# PYGAME DRAW LOGIC
# fullscreen_offsets
x_fullscreen_offset = 0
y_fullscreen_offset = 0

# Check if cell cize is restricted by having to fit grid to width or height
if (screen_h // (grid_height)) < (screen_w // (grid_width)):
    cell_size = (screen_h // (grid_height))
else:
    cell_size = (screen_w // (grid_width))

x_offset = (screen_w - (grid_width)*cell_size)//2
y_offset = (screen_h - (grid_height)*cell_size)//2

# PYGAME LOOP
while True:
    ii = -1
    for i in my_grid:
        ii += 1
        jj = -1
        for j in i:
            jj += 1
            # Figure out color
            cell_color = (0,0,0)

            if j == '#':
                cell_color = (50, 50, 50)
            if j == '=':
                cell_color = (100, 100, 100)
            if j == '.':
                cell_color = (200, 200, 200)

            x1 = int(jj * cell_size) + x_offset + x_fullscreen_offset
            y1 = int(ii * cell_size) + y_offset + y_fullscreen_offset
            x2 = cell_size
            y2 = cell_size
            pygame.draw.rect(DISPLAYSURF, cell_color, pygame.Rect(x1, y1, x2, y2))
    
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_f:
                    pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    x_fullscreen_offset = screen_w//2
                    y_fullscreen_offset = screen_h//2
                elif event.key == pygame.K_w:
                    DISPLAYSURF = pygame.display.set_mode((screen_w, screen_h))
                    x_fullscreen_offset = 0
                    y_fullscreen_offset = 0