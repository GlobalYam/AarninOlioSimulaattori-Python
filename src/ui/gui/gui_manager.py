# import random
# import math
import pygame as pg


class ScreenManager:

    def __init__(self, screen_w, screen_h, my_grid_manager):
        # screen_updates
        self.screen_update = True

        grid_width = my_grid_manager.grid_width
        grid_height = my_grid_manager.grid_height

        # fullscreen_offsets
        self.screen_w = screen_w
        self.screen_h = screen_h

        self.display_surf = pg.display.set_mode((screen_w, screen_h))

        self.fullscreen = False

        # Check if cell cize is restricted by having to fit grid to width or height
        self.cell_size = screen_w // grid_width

        if (screen_h // grid_height) < (screen_w // grid_width):
            self.cell_size = screen_h // grid_height

        self.x_offset = (screen_w - (grid_width)*self.cell_size)//2
        self.y_offset = (screen_h - (grid_height)*self.cell_size)//2

    def draw_screen_from_grid(self, grid_manager):

        if grid_manager.update() or self.screen_update:
            print("screen_updated")
            self.screen_update = False
            grid = grid_manager.my_grid

            for i, row in enumerate(grid):
                for j, cell in enumerate(row):

                    x_fullscreen_offset = 0
                    y_fullscreen_offset = 0
                    if self.fullscreen:
                        x_fullscreen_offset = self.screen_w//2
                        y_fullscreen_offset = self.screen_h//2

                    # Figure out color
                    cell_color = (0, 0, 0)

                    match cell:
                        case '=':
                            cell_color = (30, 30, 30)
                        case '#':
                            cell_color = (100, 100, 100)
                        case  'D':
                            cell_color = (80, 80, 80)
                        case  '.':
                            cell_color = (80, 80, 80)
                        case _:
                            cell_color = (0, 0, 0)

                    x_1 = int(j * self.cell_size) + \
                        self.x_offset + x_fullscreen_offset
                    y_1 = int(i * self.cell_size) + \
                        self.y_offset + y_fullscreen_offset
                    x_2 = self.cell_size
                    y_2 = self.cell_size
                    pg.draw.rect(self.display_surf, cell_color,
                                 pg.Rect(x_1, y_1, x_2, y_2))
            pg.display.flip()

    def toggle_fullsreen(self):
        self.screen_update = True
        if self.fullscreen is False:
            pg.display.set_mode((0, 0), pg.FULLSCREEN)
            self.fullscreen = True
        else:
            self.display_surf = pg.display.set_mode(
                (self.screen_w, self.screen_h))
            self.fullscreen = False
