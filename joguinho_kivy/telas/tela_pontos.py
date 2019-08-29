#!VENV/bin/python3
# -*- coding: UTF-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.app import App
from os import remove

from metodos.persistencia import lerArquivo

class Pontos(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.ponts = [] # Armazena todos os pontos

        try:
            for s in lerArquivo():
                self.ponts.append(s)
        
        except:pass

    def on_pre_enter(self):
        self.contador = len(self.ponts)-1
        
        def carregarWidgets(time):
            if self.contador < 0: return False

            self.ids.box_pontuacoes.add_widget(LabelPonts(self.ponts[self.contador]))

            self.contador -= 1

        Clock.schedule_interval(carregarWidgets, 0)


    def on_pre_leave(self):
        self.contador = len(App.get_running_app().root.get_screen('pontos').ids.box_pontuacoes.children)-1
        
        def apagaWidgets(time):
            if self.contador < 0:return False

            self.ids.box_pontuacoes.remove_widget(App.get_running_app().root.get_screen('pontos').ids.box_pontuacoes.children[self.contador])

            self.contador -= 1

        Clock.schedule_interval(apagaWidgets, 0)

    def ApagarScores(self):
        try:
            remove('Pontos/salvo.txt')
            self.ponts = []
            App.get_running_app().root.current = "menu"
        
        except:pass

class LabelPonts(BoxLayout):
    def __init__(self, texto="", **kwargs):
        super().__init__(**kwargs)

        self.ids.label_pontos.text = "=> " + str(texto) + " <="
    