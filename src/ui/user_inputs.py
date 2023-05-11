import sys

import pygame as pg


def key_events(my_screen_manager, my_grid_manager):
    """Funktio joka kuuntelee käyttäjän näppäinpainalluksia,
    ja kutsuu managerien funktioita vastaavien toimintojen perusteella

    Args:
        my_screen_manager: Näyttömanageri, joka hoitaa näkymän ruudukkomanagerin perusteella.
        grid_manager:  Ruudukkomanageri, joka sisältää halutut metodit ruudukon muokkaamisen kannalta.
    """
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

            if event.key == pg.K_s:
                my_grid_manager.save_floor("src/data/local")

            if event.key == pg.K_l:
                my_grid_manager.load_floor("src/data/local")

            if event.key == pg.K_p:
                print(my_grid_manager.room_to_string_room(my_grid_manager.my_grid))

            if event.key == pg.K_u:
                my_grid_manager.grid_updated = True

            # RESET FLOOR
            if event.key == pg.K_r:
                floor = my_grid_manager.create_floor(
                    my_grid_manager.grid_width, my_grid_manager.grid_height
                )
                for row_i, row in enumerate(floor):
                    my_grid_manager.my_grid[row_i] = row

            # GENERATE DOORS
            if event.key == pg.K_d:
                my_grid_manager.generate_paths()
                print("generate paths")

            # debug update
            if event.key == pg.K_u:
                my_screen_manager.screen_update = True
