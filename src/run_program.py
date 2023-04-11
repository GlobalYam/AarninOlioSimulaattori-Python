# import random
# import math
import sys
import pygame as pg
from logic.floor_logic import create_floor
# from logic.floor_logic import place_room
from gui.gui_manager import ScreenManager


# PYGAME INIT & SCREEN
pg.init()
SCREEN_W = (pg.display.Info().current_w)//2
SCREEN_H = (pg.display.Info().current_h)//2

# VARIABLES
GRID_WIDTH = 70
GRID_HEIGHT = 40
my_grid = create_floor(GRID_WIDTH, GRID_HEIGHT)

# PYGAME DRAW LOGIC
# create a screen_manager
my_screen_manager = ScreenManager(SCREEN_H, SCREEN_W, GRID_HEIGHT, GRID_WIDTH)

# PYGAME LOOP
while True:
    # update the screen
    my_screen_manager.draw_screen_from_grid(my_grid)

    # manage events, to be moved to user interface
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                sys.exit()
            elif event.key == pg.K_f:
                my_screen_manager.toggle_fullsreen()

            # reset entire floor
            if event.key == pg.K_r:
                my_grid = create_floor(GRID_WIDTH, GRID_HEIGHT)
