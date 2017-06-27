
import random

import entities
import pygame

from utils import config

class Environment:

    def __init__(self, size):

        self.size = size

        self.agent = entities.Agent()
        self.lightSources = [entities.LightSource(config.lightsource_luminosity)]

        self.agent.set_pos(*self.random_pos())

        for light in self.lightSources:
            light.set_pos(self.size[0] / 4, self.size[1]/2)
            #light.set_pos(*self.random_pos())

        self.background = pygame.Surface(self.size)
        self.render_background()

    def brightness_at_pos(self, pos):
        return sum([light.brightness(pos) for light in self.lightSources])

    def render_background(self):
        self.background.lock()

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                brightness = self.brightness_at_pos((x, y))
                gray_value = max(0, min(255, int(brightness * 255)))
                pixel_color = [gray_value, gray_value, gray_value, 1.]
                self.background.set_at((x,y), pixel_color)

        self.background.unlock()

    def random_pos(self):
        return (random.randint(0, self.size[0]),
                random.randint(0, self.size[1]))