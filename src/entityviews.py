import numpy as np
import pygame as pg

import utils
from utils import config



class AgentView(pg.Surface):
    def __init__(self, agent):
        color = pg.Color("#FF0000")
        width = utils.meters_to_pixels(0.1*3)
        height = utils.meters_to_pixels(0.1*4)
        super(AgentView, self).__init__((width, height), pg.SRCALPHA)

        center = 0.5 * np.array([width, height])

        def _rel_to_abs(rel_pos):
            return rel_pos + center

        def _abs_to_blit(abs_pos, blit_size):
            return abs_pos - blit_size * 0.5

        self.lock()

        # draw center
        pg.draw.line(self, color, _rel_to_abs(np.array([0, 10])),
                     _rel_to_abs(np.array([0,-10])))
        pg.draw.line(self, color, _rel_to_abs(np.array([-10, 0])),
                     _rel_to_abs(np.array([10, 0])))

        wheel_size = np.array([10, 20])

        def draw_wheel(wheel):
            # coords relative to center
            wheel_pos = utils.meters_to_pixels(wheel.get_pos2D())
            blit_wheel_pos = _abs_to_blit(_rel_to_abs(wheel_pos), wheel_size)
            self.fill(color, pg.Rect(blit_wheel_pos, wheel_size))

        draw_wheel(agent.wheel_left)
        draw_wheel(agent.wheel_right)

        sensor_radius = int(utils.meters_to_pixels(0.05))

        def draw_sensor(sensor):
            sensor_pos = utils.meters_to_pixels(sensor.get_pos2D())
            abs_pos = _rel_to_abs(sensor_pos)
            pg.draw.circle(self, color, list(map(int, abs_pos)), int(sensor_radius))

        draw_sensor(agent.sensor_left)
        draw_sensor(agent.sensor_right)

        self.unlock()




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

