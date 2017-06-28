import numpy as np
import pygame as pg

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

