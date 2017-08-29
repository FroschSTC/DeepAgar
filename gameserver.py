from threading import Thread
import time
import pygame
import config
from gui import GUI


class Gameserver(Thread):

    def __init__(self):

        self.gui = GUI()
        self.ticks = 0
        self.running = True
        self.TICKS_PER_SECOND = config.TICKS_PER_SECOND
        self.frame_counter = 0
        self.update_counter = 0

        self.players = []

    @staticmethod
    def render_interval():
        return 1.0 / config.FRAMES_PER_SECOND if config.FRAMES_PER_SECOND > 0 else 0

    @staticmethod
    def update_interval():
        return 1.0 / config.UPDATES_PER_SECOND if config.UPDATES_PER_SECOND > 0 else 0

    @staticmethod
    def stat_interval():
        return 1.0 / config.STATS_PER_SECOND if config.STATS_PER_SECOND > 0 else 0

    def loop(self):
        update_ratio = self.update_interval()
        render_ratio = self.render_interval()
        stat_ratio = self.stat_interval()
        next_update = time.time()
        next_render = time.time()
        next_stat = time.time()

        while self.running:
            now = time.time()

            if now >= next_update:
                self.update()
                next_update = now + update_ratio
                self.update_counter += 1
                self.ticks += 1

            if now >= next_render:
                self.render()
                next_render = now + render_ratio
                self.frame_counter += 1

            if now >= next_stat:
                self.caption()
                self.frame_counter = 0
                self.update_counter = 0
                next_stat = now + stat_ratio

    def update(self):
        pass

    def render(self):
        pass

    def caption(self):
        pass


if __name__ == "__main__":

    g = Gameserver()
    g.loop()