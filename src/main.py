
import pygame as pg

from environment import Environment
from view import View
import utils
from utils import config

pg.init()

screen = pg.display.set_mode(config.screen_size, 0, 32)

environment = Environment(config.environment_size)
view = View(environment)

print("Lightsource pos: ({}, {})".format(*environment.lightSources[0].pos))

screen.blit(view.background, (0,0))

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            scale = event.pos[0] / float(config.screen_width)

    pg.display.update()

