# import random
from random import randint
from data.read_data import read_room_data
from data.read_data import read_room_data_from_dir
from logic.path_logic import PathManager

# INITIALIZE FLOOR


class GridManager:
    def __init__(self):
        self.my_grid = None
        self.grid_updated = True
        self.grid_width = 0
        self.grid_height = 0
        self.solved_paths = 0

        # door array used to store the door coordinates of each room.
        self.door_array = []

    def update(self):
        if self.grid_updated:
            self.grid_updated = False
            return True
        return False

    def clear_floor(self, grid_width: int, grid_height: int):
        self.grid_updated = True
        self.door_array = []

        self.grid_width = grid_width
        self.grid_height = grid_height
        self.my_grid = []
        for i in range(self.grid_height):
            current_line = []
            for j in range(self.grid_width):
                if i == 0 or j == 0 or i == self.grid_height-1 or j == self.grid_width-1:
                    current_line += '#'  # PERSONAL WALL
                elif i == 1 or j == 1 or i == self.grid_height-2 or j == self.grid_width-2:
                    current_line += '='  # WALL AURA
                else:
                    current_line += '-'  # VOID
            self.my_grid.append(current_line)
            # print(''.join(current_line))
        return self.my_grid

    def create_floor(self, grid_width: int, grid_height: int, random_start=True):
        self.solved_paths = 0
        self.grid_updated = True

        self.my_grid = self.clear_floor(grid_width, grid_height)

        starting_room = read_room_data(
            'src/data/room_presets/starting_rooms/starting_room.txt')

        if random_start:
            x = randint(1, grid_width-1)  # pylint: disable=invalid-name
            y = randint(1, grid_height-1)  # pylint: disable=invalid-name

            fail_counter = 0
            fail_counter_max = 30

            while self.place_room(
                    self.my_grid, x, y, starting_room) is False and fail_counter < fail_counter_max:
                x = randint(1, grid_width)  # pylint: disable=invalid-name
                y = randint(1, grid_height)  # pylint: disable=invalid-name
        else:
            self.place_room(self.my_grid, grid_width//2,
                            grid_height//2, starting_room)

        fail_counter = 0
        fail_counter_max = 50

        for room in read_room_data_from_dir('src/data/room_presets/'):
            x = randint(1, grid_width-1)  # pylint: disable=invalid-name
            y = randint(1, grid_height-1)  # pylint: disable=invalid-name

            while self.place_room(
                    self.my_grid, x, y, room) is False and fail_counter < fail_counter_max:
                x = randint(1, grid_width)  # pylint: disable=invalid-name
                y = randint(1, grid_height)  # pylint: disable=invalid-name
        return self.my_grid

    def place_room(self, grid: list, rm_x: int, rm_y: int, room: list, place_by_center=True):
        self.grid_updated = True

        room = self.string_room_to_array_room(room)

        # grid_height = range(grid)
        # grid_width  = range(grid[0])

        room_height = len(room)
        room_width = len(room[0])

        if place_by_center:
            rm_x -= room_width//2
            rm_y -= room_height//2

        # check_if_free
        if not self.check_if_free(grid, rm_x, rm_y, room_height, room_width):
            return False

        # place aura to grid
        for y in range(room_height+2):  # pylint: disable=invalid-name
            for x in range(room_width+2):  # pylint: disable=invalid-name
                grid[y+rm_y-1][x+rm_x-1] = '='
        # place tiles from room to grid

        # add new list to door_array
        self.door_array.append([])

        for y in range(room_height):  # pylint: disable=invalid-name
            for x in range(room_width):  # pylint: disable=invalid-name
                grid[y+rm_y][x+rm_x] = room[y][x]
                # check if the added tile is a door, if so, add door coordinates to door_array
                if room[y][x] == 'D':
                    self.door_array[-1].append((x+rm_x, y+rm_y))

        return grid

    def check_if_free(self, grid: list, rm_x: int, rm_y: int, room_height: int, room_width: int):
        grid_height = len(grid)
        grid_width = len(grid[0])

        if rm_x+room_width > grid_width or rm_y+room_height > grid_height or rm_x < 0 or rm_y < 0:
            return False
        for y in range(rm_y, rm_y+room_height):  # pylint: disable=invalid-name
            for x in range(rm_x, rm_x+room_width):  # pylint: disable=invalid-name
                cell = grid[y][x]
                if cell != '-':
                    return False
        return True

    def string_room_to_array_room(self, room: list):
        for y in room:  # pylint: disable=invalid-name
            if isinstance(y, list):
                pass
            else:
                y.split()  # pylint: disable=invalid-name
        return room

    def check_floor(self, grid: list):

        grid_height = range(grid)
        grid_width = range(grid[0])

        for y in range(grid_height):  # pylint: disable=invalid-name, unused-variable
            for x in range(grid_width):  # pylint: disable=invalid-name, unused-variable
                cell = grid[y][x]  # pylint: disable=invalid-name, unused-variable, no-member
        return grid

    def generate_paths(self):
        if len(self.door_array) > self.solved_paths:
            self.grid_updated = True
            my_path_manager = PathManager(self)
            my_path_manager.generate_paths(self.solved_paths)
            self.solved_paths += 1
