
import numpy as np
import pygame as pg

from environment import Environment
from view import View
import utils
from utils import config

pg.init()

screen = pg.display.set_mode(config.screen_size, 0, 32)

environment = Environment(config.environment_size)
view = View(environment)

screen.blit(view.background, (0,0))
screen.blit(view.light_sources, (0, 0))

def update_title(mouse_pos):
    pos_meters = utils.pixels_to_meters(np.array(mouse_pos))
    pg.display.set_caption("Cursor position (m): {}".format(pos_meters))

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEMOTION:
            update_title(event.pos)
        if event.type == pg.MOUSEBUTTONDOWN:
            scale = event.pos[0] / float(config.screen_width)

    pg.display.update()

