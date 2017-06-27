
import numpy as np



class Entity:

    def __init__(self):
        # 2D position = (x,y)
        self.pos = np.array(0, 0)
        # angle around z-axis: alpha
        self.ori = 0

class Agent:

    def __init__(self):
        pass



class LightSource:

    def __init__(self, luminosity=1.0):
        self.luminosity = luminosity

    def shade(self, pos):
        """Return the brightness at point pos,
        by the inverse-square law."""
        # inverse square law: B = L / 4*pi*D^2
        distance = np.sqrt(sum(map(lambda x: x**2,
                                   map(lambda pp: pp[0] - pp[1], zip(self.pos, pos)))))
        return self.luminosity / (4 * np.pi * distance**2)

