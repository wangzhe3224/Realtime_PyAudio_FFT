import pygame as pg


if __name__ == '__main__':

    SCREENRECT = pg.Rect(0, 0, 640, 480)

    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()

    input('??> ')
