
import pygame as pg

from environment import Environment
import utils
from utils import config

pg.init()

screen = pg.display.set_mode(config.screen_size, 0, 32)

environment = Environment(config.screen_size)

print("Lightsource pos: ({}, {})".format(*environment.lightSources[0].pos))

screen.blit(environment.background, (0,0))

intensityLimits = [0, 100]

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            scale = event.pos[0] / float(config.screen_width)

    pg.display.update()

