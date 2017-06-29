
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
        self._pos = np.array(pos2D)


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
        self._pos[0:2] = np.array(pos2D)

    def set_pos3D(self, pos3D):
        assert len(pos3D) == 3
        self._pos = np.array(pos3D)


class Wheel(Entity2D):

    def __init__(self, position):
        super(Wheel, self).__init__()
        self.set_pos2D(position)


class Sensor(Entity2D):
    def __init__(self, position):
        super(Sensor, self).__init__()
        self.set_pos2D(position)


class Agent(Entity2D):

    def __init__(self):
        super(Agent, self).__init__()
        # angle around z-axis: alpha
        self.ori = 0.

        self.size = utils.config.agent["size"]
        sensor_cfg = utils.config.agent["sensor"]
        wheel_cfg = utils.config.agent["wheel"]
        wheel_x = wheel_cfg["x"] * self.size
        wheel_y = wheel_cfg["y"] * self.size
        sensor_x = sensor_cfg["x"] * self.size
        sensor_y = sensor_cfg["y"] * self.size

        self.wheel_left = Wheel((-wheel_x, wheel_y))
        self.wheel_right = Wheel((wheel_x, wheel_y))
        self.wheels = [self.wheel_left, self.wheel_right]

        self.sensor_left = Sensor((-sensor_x, sensor_y))
        self.sensor_right = Sensor((sensor_x, sensor_y))
        self.sensors = [self.sensor_left, self.sensor_right]



class LightSource(Entity3D):

    def __init__(self, luminosity):
        super(LightSource, self).__init__()
        self.luminosity = luminosity


