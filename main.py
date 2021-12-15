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
from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.size = (350, 550)


class Principal(BoxLayout):

    def __init__(self, um, dois, tres, quatro, cinco, seis, sete, oito, nove, zero, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.um = um
        self.dois = dois
        self.tres = tres
        self.quatro = quatro
        self.cinco = cinco
        self.seis = seis
        self.sete = sete
        self.oito = oito
        self.nove = nove
        self.zero = zero

    def clear(self):
        self.ids.calculadora.text = '0'

    def numero_um(self, numero):
        botao_um = self.ids.calculadora.text
        self.um = botao_um
        if botao_um == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora.text = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_um}{numero}'

    def numero_dois(self, numero):
        botao_dois = self.ids.calculadora.text
        self.dois = botao_dois
        if botao_dois == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora.text = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_dois}{numero}'

    def numero_tres(self, numero):
        botao_tres = self.ids.calculadora.text
        self.tres = botao_tres
        if botao_tres == "0":
            self.ids.calculadora.text = ''
            self.ids.calculadora.text = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_tres}{numero}'

    def numero_quatro(self, numero):
        botao_quatro = self.ids.calculadora.text
        self.quatro = botao_quatro
        if botao_quatro == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_quatro}{numero}'

    def numero_cinco(self, numero):
        botao_cinco = self.ids.calculadora.text
        self.cinco = botao_cinco
        if botao_cinco == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora.text = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_cinco}{numero}'

    def numero_seis(self, numero):
        botao_seis = self.ids.calculadora.text
        self.seis = botao_seis
        if botao_seis == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_seis}{numero}'

    def numero_sete(self, numero):
        botao_sete = self.ids.calculadora.text
        self.sete = botao_sete
        if botao_sete == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora.text = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_sete}{numero}'

    def numero_oito(self, numero):
        botao_oito = self.ids.calculadora.text
        self.oito = botao_oito
        if botao_oito == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora.text = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_oito}{numero}'

    def numero_nove(self, numero):
        botao_nove = self.ids.calculadora.text
        self.nove = botao_nove
        if botao_nove == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora.text = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_nove}{numero}'

    def numero_zero(self, numero):
        botao_zero = self.ids.calculadora.text
        self.zero = botao_zero
        if botao_zero == '0':
            self.ids.calculadora.text = ''
            self.ids.calculadora.text = f'{numero}'
        else:
            self.ids.calculadora.text = f'{botao_zero}{numero}'

    def remover_ultimo(self):
        ultimo = self.ids.calculadora.text
        ultimo = ultimo[:-1]
        self.ids.calculadora.text = ultimo

    def sinais(self, sinal):
        formulando = self.ids.calculadora.text
        self.ids.calculadora.text = f'{formulando}{sinal}'

    def resultado(self):
        numero = self.ids.calculadora.text
        try:
            result = eval(numero)
            self.ids.calculadora.text = str(result)
        except:
            self.ids.calculadora.text = "Equação Errada"

    def ponto(self):
        numero = self.ids.calculadora.text
        num_list = numero.split(f'\+|\*||-|/|%, {numero}')

        if ("+" in numero or "-" in numero or "/" in numero or "%" in numero or "*") and '.' not in num_list[:-1]:
            numero = f'{numero}.'
            self.ids.calculadora.text = numero

        if '.' in numero:
            pass
        else:
            numero = f'{numero}.'
            self.ids.calculadora.text = numero



class Calculadora(App):
    def build(self):
        return Principal(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


if __name__ == '__main__':
    Calculadora().run()
