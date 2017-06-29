
import numpy as np
import yaml

class Config:
    def __init__(self):
        with open("../config/config.yaml", "r") as configfile:
            try:
                config = yaml.safe_load(configfile)
            except yaml.YAMLError as exc:
                raise exc

        self.screen_width = config["screen_width"]
        self.screen_height = config["screen_height"]
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen_extent = config["screen_extent"]

        self.pixel_to_meter_ratio = self.screen_extent / max(*self.screen_size)

        self.environment_width = self.screen_width * self.pixel_to_meter_ratio
        self.environment_height = self.screen_height * self.pixel_to_meter_ratio
        self.environment_size = np.array([self.environment_width,
                                          self.environment_height])

        self.light_luminosity = config["light_luminosity"]
        self.light_height = config["light_height"] # in m

        k_diffuse_dict = config["k_diffuse"]
        self.k_diffuse = np.array([k_diffuse_dict["r"],
                                   k_diffuse_dict["g"],
                                   k_diffuse_dict["b"]])

        self.light_symbol = config["light_symbol"]

        self.agent_view = config["agent_view"]

config = Config()

def pixels_to_meters(pixels):
    return pixels * config.pixel_to_meter_ratio


def meters_to_pixels(meters):
    return meters / config.pixel_to_meter_ratio

