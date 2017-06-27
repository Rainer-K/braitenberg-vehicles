
import yaml


class Config:
    def __init__(self):
        with open("../config/config.yaml", "r") as configfile:
            try:
                config = yaml.safe_load(configfile)
            except yaml.YAMLError as exc:
                print(exc)

        self.screen_width = config["screen_width"]
        self.screen_height = config["screen_height"]
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen_extent = config["screen_extent"]

        self.pixel_to_meter_ratio = self.screen_extent / max(*self.screen_size)

        self.lightsource_luminosity = config["lightsource_luminosity"]
        self.lightsource_height = config["lightsource_height"] # in m


config = Config()

def pixels_to_meters(pixels):
    return pixels * config.pixel_to_meter_ratio


def meters_to_pixels(meters):
    return meters / config.pixel_to_meter_ratio

