
import random
import numpy as np

import entities


from utils import config

class Environment:

    def __init__(self, size):

        self.size = size

        self.agent = entities.Agent()
        self.lightSources = [entities.LightSource(config.light_luminosity)]

        self.agent.set_pos2D(self.random_pos())

        for light in self.lightSources:
            light.set_pos3D(np.concatenate((self.random_pos(),
                                            np.array([config.light_height]))))
            print("Lightsource position: {}".format(light.get_pos3D()))


    def brightness_at_pos(self, pos):
        return sum([self.brightness_of_lightsource(pos, light)
                    for light in self.lightSources])

    def random_pos(self):
        return np.array([random.uniform(0, self.size[0]),
                         random.uniform(0, self.size[1])])

    def brightness_of_lightsource(self, pos, lightsource):
        # shading by Fresnel effect
        # normal: (0, 0, 1) (z points up)
        # intensity = N * L, normal N, L vector to light (both normalized)
        normal = np.array([0., 0., 1.])

        to_light = lightsource.get_pos3D() - np.array(list(pos) + [0.])
        # normalize
        to_light /= np.linalg.norm(to_light)

        brightness = lightsource.luminosity * np.dot(normal, to_light)

        return brightness
