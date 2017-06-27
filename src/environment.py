
import entities

class Environment:

    def __init__(self):

        self.agent = entities.Agent()
        self.lightsource = entities.LightSource(1.)

        