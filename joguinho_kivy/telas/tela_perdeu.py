#!VENV/bin/python3
# -*- coding: UTF-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.app import App

from metodos.persistencia import salvarArquivo

class Perdeu(Screen):
    def on_pre_enter(self):

        self.ids.mostrar_score_label.text = "Sua Pontuação: " + str(App.get_running_app().root.get_screen('game').score)

        if App.get_running_app().root.get_screen('game').score > 0:
            App.get_running_app().root.get_screen('pontos').ponts.append(App.get_running_app().root.get_screen('game').score)
            salvarArquivo(App.get_running_app().root.get_screen('pontos').ponts)

