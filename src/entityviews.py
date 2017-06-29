import numpy as np
import pygame as pg

import utils
from utils import config



class AgentView(pg.Surface):
    def __init__(self, agent):
        # load image
        image = pg.image.load("../assets/agent-sym.png").convert_alpha()
        aspect_ratio = float(image.get_height()) / image.get_width() # h / w

        height_pxl = int(utils.meters_to_pixels(agent.size))
        width_pxl = int(height_pxl / aspect_ratio)

        super(AgentView, self).__init__((width_pxl, height_pxl))
        image_scaled = pg.transform.scale(image, (width_pxl, height_pxl))

        self.blit(image_scaled, (0,0))


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

