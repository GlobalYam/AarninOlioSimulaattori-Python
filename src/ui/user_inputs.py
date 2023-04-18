import sys
import pygame as pg
from logic.floor_logic import GridManager


def key_events(my_screen_manager, my_grid_manager):
    for event in pg.event.get():

        # QUIT
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:

            # QUIT
            if event.key == pg.K_q:
                sys.exit()

            # FULLSCREEN
            if event.key == pg.K_f:
                my_screen_manager.toggle_fullsreen()

            # RESET FLOOR
            if event.key == pg.K_r:
                for i, row in enumerate(my_grid_manager.create_floor(my_grid_manager.grid_width, my_grid_manager.grid_height)):
                    my_grid_manager.my_grid[i] = row
