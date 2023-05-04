class PathManager():
    """Luokka, joka vastaa polkujen lisäämisestä.

    Attributes:
        my_grid_manager: Luokan kutsunut ruudukkomanageri.
        grid_updated: Kertoo mikäli ruudukkoa on muutettu tällä askeleella, tällä hetkellä turha
        temp_grid:   Väliaikainen ruudukko, johon voidaan luoda polut
        room_num:  Huoneen lukunumero, joka yhdistää poluilla
    """

    def __init__(self, my_grid_manager):
        """Luokan konstruktori, joka alustaa managerin.

        Args:
            my_grid_manager:  Luokan kutsunut ruudukkomanageri.
        """
        self.my_grid_manager = my_grid_manager
        self.grid_updated = False
        self.temp_grid = False
        self.room_num = 0

    def generate_paths(self, room_to_generate_paths_for):
        """Luokan konstruktori, joka alustaa managerin.

        Args:
            room_to_generate_paths_for:  Huoneen lukunumero, joka yhdistää poluilla.
        """
        # door array used to store the door coordinates of each room.
        # self.my_grid_manager.door_array.copy() #
        temp_doors = [line.copy() for line in self.my_grid_manager.door_array]

        room_doors = temp_doors[room_to_generate_paths_for]

        # self.my_grid_manager.my_grid.copy() #
        temp_grid = [line.copy() for line in self.my_grid_manager.my_grid]

        # make templist for the doors of a single room
        temp_paths = []

        # start paths for room
        for door_number, door in enumerate(room_doors):
            temp_paths.append([])

            if self.expand_branch(door, temp_grid, temp_paths[door_number]):
                print('two paths immidiately connected!')

        # print(f'temp_paths for current room: {temp_paths}')
        max_path_lenght = 1000
        for iter_num in range(0, max_path_lenght):
            lists_used = 4
            # print(f'handling branch repeat num: {iter_num}')
            for i, branch in enumerate(temp_paths):
                # print(f'branch_len, branh_num {len(branch), i}')
                lenght = len(branch)
                if lenght == 0:
                    lists_used -= 1
                    continue
                if lenght > iter_num:
                    if self.expand_branch(branch[iter_num], temp_grid, temp_paths[i]):
                        temp_paths[i] = []
                        # print('found connection')

                        xx, yy = branch[iter_num]  # pylint: disable=invalid-name
                        next_coords = temp_grid[yy][xx]  # pylint: disable=invalid-name
                        list_of_path_coords = []
                        # print(f'xx, yy: {xx, yy}')
                        # print(f'next_coords: {next_coords}')
                        # print(branch)

                        self.my_grid_manager.my_grid[yy][xx] = 'X'  # pylint: disable=invalid-name
                        list_of_path_coords.append((xx, yy))

                        for rep in range(iter_num):
                            self.my_grid_manager.my_grid[next_coords[1]
                                                         ][next_coords[0]] = 'X'

                            if temp_grid[next_coords[1]][next_coords[0]] == next_coords:
                                continue

                            list_of_path_coords.append(next_coords)
                            # print(next_coords)
                            next_coords = temp_grid[next_coords[1]
                                                    ][next_coords[0]]

                        return list_of_path_coords
            # print(lists_used)
            if lists_used <= 1:
                return []

        return []

    def expand_branch(self, path_parent, grid, temp_paths):
        """Metodi joka laajentaa haaraa yhdellä askeleella eteenpäin.

        Args:
            path_parent:  polku vanhempi, jota laajentaa.
            grid:  ruudukko johon lisätä uudet haarat
            temp_paths:  lista johon lisätään lisätyt solut  

        """
        # print(path_parent)
        x, y = path_parent  # pylint: disable=invalid-name

        # print(f'y: {y}')
        # print(f'x: {x}')

        tile = grid[y][x]  # pylint: disable=invalid-name

        if tile == 'D':
            grid[y][x] = (x, y)  # pylint: disable=invalid-name

        try:
            upper_tile = (x,  y-1)  # pylint: disable=invalid-name
            lower_tile = (x,  y+1)   # pylint: disable=invalid-name
            left_tile = (x-1,  y)   # pylint: disable=invalid-name
            right_tile = (x+1,  y)   # pylint: disable=invalid-name
        except Exception as exc:
            raise 'OOPS, INVALID TILE INPUT' from exc

        child_tiles = [upper_tile, lower_tile, left_tile, right_tile]

        for coords in child_tiles:
            tile = grid[coords[1]][coords[0]]
            if tile in ('-', '='):
                # checked tile is all good, now it can be set to my tile.
                grid[coords[1]][coords[0]] = path_parent
                temp_paths.append(coords)
            elif tile == 'D':
                return True
        return False
