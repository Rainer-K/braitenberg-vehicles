import pygame as pg

import utils
from entityviews import LightSymbolStar, AgentView
from utils import config


class View:

    def __init__(self, screen, environment):
        self.screen = screen
        self.screen_size = config.screen_size

        self.environment = environment

        print("Rendering background...", end="", flush=True)
        self.background = pg.Surface(self.screen_size)
        self.render_background()
        print(" Done.")

        self._light_source_symbol = LightSymbolStar()

        self.light_sources = pg.Surface(self.screen_size).convert_alpha()
        self.render_light_sources()

        self.agent = AgentView(environment.agent)

        self.agent_gadgets = pg.Surface(self.screen_size).convert_alpha()
        self.render_agent_gadgets()


    def blit_to_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.light_sources, (0, 0))

        agent_pxl_pos = utils.meters_to_pixels(self.environment.agent.get_pos2D())
        agent_blit_pos = (int(agent_pxl_pos[0] - self.agent.get_width() / 2),
                          int(agent_pxl_pos[1]))

        self.screen.blit(self.agent, agent_blit_pos)
        self.screen.blit(self.agent_gadgets, (0, 0))

    def render_background(self):
        self.background.lock()

        for x in range(self.screen_size[0]):
            for y in range(self.screen_size[1]):
                pos_m = (utils.pixels_to_meters(x), utils.pixels_to_meters(y))

                brightness = self.environment.brightness_at_pos(pos_m)
                intensity = max(0, min(255, int(brightness * 255)))

                pixel_color = config.k_diffuse * intensity
                self.background.set_at((x,y), pixel_color)

        self.background.unlock()

    def render_light_sources(self):
        self.light_sources.fill((0, 0, 0, 0))
        for light in self.environment.lightSources:
            symbol_size = self._light_source_symbol.get_size()
            pos = utils.meters_to_pixels(light.get_pos2D())
            blit_pos = (pos[0] - symbol_size[0]/2,
                        pos[1] - symbol_size[1]/2)

        self.light_sources.blit(self._light_source_symbol, blit_pos)

    def render_agent_gadgets(self):
        self.agent_gadgets.fill((0, 0, 0, 0))

        agent = self.environment.agent

        def make_cross(color):
            pgcolor = pg.Color(color)
            cross = pg.Surface((10, 10)).convert_alpha()
            cross.fill((0,0,0,0))
            cross.lock()
            pg.draw.line(cross, pgcolor, (0, 5), (10, 5))
            pg.draw.line(cross, pgcolor, (5, 0), (5, 10))
            pg.draw.circle(cross, pgcolor, (5, 5), 5, 1)
            cross.unlock()
            return cross

        wheel_marker = make_cross("#FF0000")
        sensor_marker = make_cross("#00FF00")

        def blit_marker_to_pos(marker, pos_m):
            pos_pxl = utils.meters_to_pixels(pos_m)
            blit_pos = self._blit_pos_center(pos_pxl, marker)

            self.agent_gadgets.blit(marker, blit_pos)

        for gadget in agent.wheels:
            blit_marker_to_pos(wheel_marker, gadget.get_pos2D() + agent.get_pos2D())

        for gadget in agent.sensors:
            blit_marker_to_pos(sensor_marker, gadget.get_pos2D() + agent.get_pos2D())


    def _blit_pos_center(self, pos, blitted):
        return (int(pos[0] - blitted.get_width() / 2),
                int(pos[1] - blitted.get_height() / 2))





