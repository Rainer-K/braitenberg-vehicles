import pygame as pg

import utils
from entityviews import LightSymbolStar
from utils import config


class View:

    def __init__(self, environment):
        self.screen_size = config.screen_size

        self.environment = environment

        print("Rendering background...", end="", flush=True)
        self.background = pg.Surface(self.screen_size)
        self.render_background()
        print(" Done.")

        self._light_source_symbol = LightSymbolStar()

        self.light_sources = pg.Surface(self.screen_size).convert_alpha()
        self.render_light_sources()



    def render_background(self):
        self.background.lock()

        for x in range(self.screen_size[0]):
            for y in range(self.screen_size[1]):
                pos_m = (utils.pixels_to_meters(x), utils.pixels_to_meters(y))

                brightness = self.environment.brightness_at_pos(pos_m)
                intensity = max(0, min(255, int(brightness * 255)))

                pixel_color = config.k_diffuse * intensity
                self.background.set_at((x,y), pixel_color)

        self.background.unlock()

    def render_light_sources(self):
        self.light_sources.fill((0, 0, 0, 0))
        for light in self.environment.lightSources:
            symbol_size = self._light_source_symbol.get_size()
            pos = utils.meters_to_pixels(light.get_pos2D())
            blit_pos = (pos[0] - symbol_size[0]/2,
                        pos[1] - symbol_size[1]/2)

        self.light_sources.blit(self._light_source_symbol, blit_pos)


