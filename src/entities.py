
import numpy as np

import utils


class Entity:

    def __init__(self):
        # 2D position = (x,y)
        self.pos = np.array([0, 0])

    def set_pos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

class Agent(Entity):

    def __init__(self):
        super(Agent, self).__init__()
        # angle around z-axis: alpha
        self.ori = 0.


class LightSource(Entity):

    def __init__(self, luminosity):
        super(LightSource, self).__init__()
        self.luminosity = luminosity

    def brightness(self, pos):
        # shading by Fresnel effect
        # normal: (0, 0, 1) (z points up)
        # intensity = N * L, normal N, L vector to light (both normalized)
        normal = np.array([0., 0., 1.])
        light_3D_pos = np.array(list(map(utils.pixels_to_meters, self.pos)) + [utils.config.lightsource_height])
        point_3D_pos = np.array(list(map(utils.pixels_to_meters, pos)) + [0.])

        to_light = light_3D_pos - point_3D_pos
        # normalize
        to_light /= np.linalg.norm(to_light)

        intensity = self.luminosity * np.dot(normal, to_light)

        return intensity




