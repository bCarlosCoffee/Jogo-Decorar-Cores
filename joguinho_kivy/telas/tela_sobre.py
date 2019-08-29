#!VENV/bin/python3
# -*- coding: UTF-8 -*-

from kivy.uix.screenmanager import Screen

class Sobre(Screen):
    def on_pre_enter(self):
        sobre = """
        Importante:
            Este jogo foi desenvolvido em Kivy
            Com o intuito de aprendizado e exemplo
            sobre oque esse framework pode fazer!
        
        Como Jogar?
            Você precisará decorar a cor que o jogo irá mostrar
            Exatamente 5 segundos para decorar...
            Depois ele irá te mostrar várias cores aleatoriamente
            Quando voce encotrar à cor.
            Clique no botão parar logo abaixo!

            São 5 tentativas!

        por Carlos => Caffee Tec
    

        :)
        """
        self.ids.texto_sobre.text = sobre
    