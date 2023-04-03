# CREATE A FLOOR
def create_floor(grid_width, grid_height):
    my_grid = []

    for i in range(grid_height):
        current_line = ''
        for j in range(grid_width):
            if i == 0 or j == 0 or i == grid_height-1 or j == grid_width-1:
                current_line += '#' # PERSONAL WALL
            elif i == 1 or j == 1 or i == grid_height-2 or j == grid_width-2:
                current_line += '=' # WALL AURA
            else:
                current_line += '-' # VOID
        my_grid.append(current_line)
        print(current_line)
    
    return my_grid