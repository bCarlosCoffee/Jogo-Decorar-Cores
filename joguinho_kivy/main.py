#!VENV/bin/python3
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition

class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.transition=FadeTransition()

class appcores(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    appcores().run()
