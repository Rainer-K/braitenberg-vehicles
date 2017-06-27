
import random
import numpy as np

import entities


from utils import config

class Environment:

    def __init__(self, size):

        self.size = size

        self.agent = entities.Agent()
        self.lightSources = [entities.LightSource(config.lightsource_luminosity)]

        self.agent.pos = self.random_pos()

        for light in self.lightSources:
            #light.set_pos(self.size[0] / 4, self.size[1]/2)
            light.pos = self.random_pos()


    def brightness_at_pos(self, pos):
        return sum([light.brightness(pos) for light in self.lightSources])

    def random_pos(self):
        return np.array([random.uniform(0, self.size[0]),
                         random.uniform(0, self.size[1])])