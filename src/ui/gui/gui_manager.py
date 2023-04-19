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
        self.screen_res_default = (screen_w, screen_h)
        self.screen_w, self.screen_h = self.screen_res_default

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

            for y, row in enumerate(grid):
                for x, cell in enumerate(row):
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

                    self.draw_cell_to_screen(grid_manager, x, y, cell_color)
            pg.display.flip()

    def draw_cell_to_screen(self, grid_manager, x, y, cell_color):

        # fullscreen_offsets
        # x_fullscreen_offset = 0
        # y_fullscreen_offset = 0
        # if self.fullscreen:
        #     x_fullscreen_offset = self.screen_w//2
        #     y_fullscreen_offset = self.screen_h//2

        grid_width = grid_manager.grid_width
        grid_height = grid_manager.grid_height

        # Check if cell cize is restricted by having to fit grid to width or height
        self.cell_size = self.screen_w // grid_width

        if (self.screen_h // grid_height) < (self.screen_w // grid_width):
            self.cell_size = self.screen_h // grid_height

        self.x_offset = (self.screen_w - (grid_width)*self.cell_size)//2
        self.y_offset = (self.screen_h - (grid_height)*self.cell_size)//2

        x_1 = int(x * self.cell_size) + self.x_offset
        y_1 = int(y * self.cell_size) + self.y_offset

        x_2 = self.cell_size
        y_2 = self.cell_size
        pg.draw.rect(self.display_surf, cell_color,
                     pg.Rect(x_1, y_1, x_2, y_2))

    def toggle_fullsreen(self):
        self.screen_update = True
        if self.fullscreen is False:
            pg.display.set_mode((0, 0), pg.FULLSCREEN)
            self.screen_w, self.screen_h = pg.display.get_window_size()
            self.fullscreen = True
        else:
            self.screen_w, self.screen_h = self.screen_res_default
            self.display_surf = pg.display.set_mode(
                (self.screen_w, self.screen_h))
            self.fullscreen = False
