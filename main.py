from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import copy
from kivy.lang import Builder
from random import random as rand
import os
import numeros
from numeros import Numeros
from entidades_numeros import Entidades_Numeros


class Principal(BoxLayout):

    def __init__(self, um, dois, tres, quatro, cinco, seis, sete, oito, nove, **kwargs):
        super(Principal,  self).__init__(**kwargs)
        self.um = um
        self.dois = dois
        self.tres = tres
        self.quatro = quatro
        self.cinco = cinco
        self.seis = seis
        self.sete = sete
        self.oito = oito
        self.nove = nove

    def numero_um(self):
        self.ids.botao1 = self.ids.botao1
        self.um = self.um
        print(self.um)

    def numero_dois(self):
        self.ids.botao2 = self.ids.botao2
        self.dois = self.dois
        print(self.dois)

    def numero_tres(self):
        self.ids.botao3 = self.ids.botao3
        self.tres = self.tres
        print(self.tres)

    def numero_quatro(self):
        self.ids.botao4 = self.ids.botao4
        self.quatro = self.quatro
        print(self.quatro)

    def numero_cinco(self):
        self.ids.botao5 = self.ids.botao5
        self.cinco = self.cinco
        print(self.cinco)

    def numero_seis(self):
        self.ids.botao6 = self.ids.botao6
        self.seis = self.seis
        print(self.seis)

    def numero_sete(self):
        self.ids.botao7 = self.ids.botao7
        self.sete = self.sete
        print(self.sete)

    def numero_oito(self):
        self.ids.botao8 = self.ids.botao8
        self.oito = self.oito
        print(self.oito)

    def numero_nove(self):
        self.ids.botao9 = self.ids.botao9
        self.nove = self.nove
        print(self.nove)

    def numeros_soma(self):

        try:
            if self.um + self.dois:
                print(self.um + self.dois)
                return self.um + self.dois
            else:
                return self.soma
        except:
            pass

        try:
            if self.um + self.tres or self.tres + self.um:
                print(self.um + self.tres)
                return self.um + self.tres
            else:
                return self.soma
        except:
            pass

        try:
            if self.dois + self.tres or self.tres + self.dois:
                print(self.dois + self.tres)
                return self.dois + self.tres
            else:
                return self.soma
        except:
            pass

        try:
            if self.um + self.tres + self.dois or self.um + self.dois + self.tres:
                print(self.soma)
                return self.um + self.dois + self.tres
            else:
                return self.soma
        except:
            pass


class Calculadora(App):
    def build(self):
        return Principal(1, 2, 3, 4, 5, 6, 7, 8, 9)


if __name__ == '__main__':
    Calculadora().run()
