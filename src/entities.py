
import numpy as np

import utils


class Entity:

    def __init__(self):
        pass


class Entity2D(Entity):

    def __init__(self):
        # 2D position = (x,y)
        self._pos = np.array([0, 0])

    def get_pos2D(self):
        return self._pos

    def set_pos2D(self, pos2D):
        assert len(pos2D) == 2
        self._pos = pos2D


class Entity3D(Entity):

    def __init__(self):
        # 3D poisiton = (x,y,z)
        self._pos = np.array([0, 0, 0])

    def get_pos2D(self):
        return self._pos[0:2]

    def get_pos3D(self):
        return self._pos

    def set_pos2D(self, pos2D):
        assert len(pos2D) == 2
        self._pos[0:2] = pos2D

    def set_pos3D(self, pos3D):
        assert len(pos3D) == 3
        self._pos = pos3D


class Agent(Entity2D):

    def __init__(self):
        super(Agent, self).__init__()
        # angle around z-axis: alpha
        self.ori = 0.


class LightSource(Entity3D):

    def __init__(self, luminosity):
        super(LightSource, self).__init__()
        self.luminosity = luminosity


