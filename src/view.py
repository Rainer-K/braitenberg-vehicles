
import pygame

import utils
from utils import config

class View:

    def __init__(self, environment):
        self.screen_size = config.screen_size

        self.environment = environment

        self.background = pygame.Surface(self.screen_size)
        self.render_background()

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