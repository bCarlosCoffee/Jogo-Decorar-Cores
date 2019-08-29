#!VENV/bin/python3
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

from random import randint

# Responsavel pelo jogo todo em si!

class Game(Screen): 
    def on_pre_enter(self):
        #self.nivel = É multiplicado por 2 toda vez em que o usuario Acerta a Cor!
        #self.nivel é definido na cor do rgba.

        self.nivel = 2
        self.score = 0
        self.tentativas = 5

        self.mostraCorParaDecorar()


    def mostraCorParaDecorar(self):
        # If para self.nivel nunca passar de 255 que é o maximo do rgb (255,255,255)
        if self.nivel >= 250: self.nivel = 250
        
        while True:
            self.r = int(randint(0, self.nivel))
            self.g = int(randint(0, self.nivel))
            self.b = int(randint(0, self.nivel))

            if self.r == self.g and self.g == self.b and self.r == self.b:
                # Só parar quando red green blue não forem iguais
                pass
            else:
                break
                
        self.cor_definida = (self.r,self.g,self.b)
        self.contador_de_tempo = 5
        self.wdc = WidgetDecoraCor(self.contador_de_tempo, self.r,self.g,self.b)
        self.wdj = WidgetDoJogo()
        self.ids.box_principal.add_widget(self.wdc)

        def decorarCor(segundo):

            if self.contador_de_tempo == 0: 
                self.ids.box_principal.remove_widget(self.wdc)
                self.ids.box_principal.add_widget(self.wdj)
                return False

            self.contador_de_tempo -= 1
            self.wdc.ids.tempo_label.text = str(self.contador_de_tempo)

        Clock.schedule_interval(decorarCor, 1)
    
    def ApagaWidgets(self):
        try:
            self.ids.box_principal.remove_widget(self.wdj)
            self.ids.box_principal.remove_widget(self.wdc)
        
        except:pass


class WidgetDoJogo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.loop = True
        self.ids.score_label.text = "Pontuação: " + str(App.get_running_app().root.get_screen('game').score)
        self.ids.tentativas_label.text = "Tentativas: " + str(App.get_running_app().root.get_screen('game').tentativas)
        self.perdeu = False

        def start(time):
            nivel = App.get_running_app().root.get_screen('game').nivel
           
            r = int(randint(0, nivel))
            g = int(randint(0, nivel))
            b = int(randint(0, nivel))

            if r == g and g == b and r == b:
                pass
            
            else:
                self.cor_atual = (r,g,b)

                self.desenha_cor(r,g,b)
                self.update_rect()
            
            if self.loop == False: 
                App.get_running_app().root.get_screen('game').ApagaWidgets()
                App.get_running_app().root.get_screen('game').mostraCorParaDecorar()
                return False
            
            
            if self.perdeu == True: return False

        Clock.schedule_interval(start, 1)

    
    def desenha_cor(self, r="",g="",b=""):
        
        with self.canvas.before:
            Color(f'.{r}',f'.{g}',f'.{b}')
            self.rect = Rectangle(pos = self.center, size =(self.width / 2., self.height / 2.))

    def update_rect(self, *args): 
        self.rect.pos = self.pos 
        self.rect.size = self.size 
    
    def verifica(self):
        self.ids.botao_parar.disabled = True
        self.cor_definida = App.get_running_app().root.get_screen('game').cor_definida

        if self.cor_atual == self.cor_definida:
            App.get_running_app().root.get_screen('game').score += 10
            App.get_running_app().root.get_screen('game').nivel *= 2
            self.ids.score_label.text = "Pontuação: " + str(App.get_running_app().root.get_screen('game').score)
            self.loop = False
        
        else:
            App.get_running_app().root.get_screen('game').tentativas -= 1

            if App.get_running_app().root.get_screen('game').tentativas <= 0:
                self.perdeu = True
                App.get_running_app().root.current = "perdeu"
                App.get_running_app().root.get_screen('game').ApagaWidgets()

            self.ids.tentativas_label.text = "Tentativas: " + str(App.get_running_app().root.get_screen('game').tentativas)
        
        self.ids.botao_parar.disabled = False


class WidgetDecoraCor(BoxLayout):
    def __init__(self, tempo="", r="",g="",b="", **kwargs):
        super().__init__(**kwargs)

        self.ids.tempo_label.text = str(tempo)

        with self.canvas.before:
            Color(f'.{r}',f'.{g}',f'.{b}')
            self.rect = Rectangle(pos = self.center, size =(self.width / 2., self.height / 2.))

            self.bind(pos = self.update_rect, size = self.update_rect) 

    def update_rect(self, *args): 
        self.rect.pos = self.pos 
        self.rect.size = self.size 
