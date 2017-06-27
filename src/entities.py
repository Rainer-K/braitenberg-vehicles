
import numpy as np

import utils


class Entity:

    def __init__(self):
        # 2D position = (x,y)
        self.pos = np.array([0, 0])

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
        light_3D_pos = np.array(list(self.pos) + [utils.config.lightsource_height])
        point_3D_pos = np.array(list(pos) + [0.])

        to_light = light_3D_pos - point_3D_pos
        # normalize
        to_light /= np.linalg.norm(to_light)

        brightness = self.luminosity * np.dot(normal, to_light)

        return brightness




