
import numpy as np
import pygame as pg

import utils
from utils import config


class LightSymbolPolygon(pg.Surface):

    def __init__(self):
        size = config.light_symbol["size"]
        super(LightSymbolPolygon, self).__init__((size, size), pg.SRCALPHA)
        # draws a 4 pointed star
        inset = 0.3
        points = np.array([
            (0, 1), (inset, inset), (1, 0), (inset, -inset),
            (0, -1), (-inset, -inset), (-1, 0), (-inset, inset)
        ])
        # scale and shift
        points *= size / 2
        points += size / 2

        self.fill((0, 0, 0, 0))
        color = pg.Color(config.light_symbol["color"])
        pg.draw.polygon(self, color, points)
        # pg.draw.aalines(surface, color, True, points)

class LightSymbolStar(pg.Surface):

    def __init__(self):
        size = config.light_symbol["size"]
        color = pg.Color(config.light_symbol["color"])
        super(LightSymbolStar, self).__init__((size, size), pg.SRCALPHA)

        # draws an 8-pointed *
        sqr = np.sqrt(1**2 / 2)
        lines = [((0, 1), (0, -1)),
                 ((-1, 0), (1, 0)),
                 ((-sqr, -sqr), (sqr, sqr)),
                 ((-sqr, sqr), (sqr, -sqr))]
        lines = [ (np.array(p), np.array(q)) for (p, q) in lines]

        # scale and shift
        lines = [(p*size/2 + size/2, q*size/2 + size/2) for (p, q) in lines]

        self.fill((0, 0, 0, 0))
        for line in lines:
            pg.draw.line(self, color, line[0], line[1], 3)



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


