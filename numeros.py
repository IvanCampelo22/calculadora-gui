import copy
from entidades_numeros import Entidades_Numeros


class Numeros():
    def __init__(self):
        self.nove = Entidades_Numeros.nove
        self.oito = Entidades_Numeros.oito
        self.sete = Entidades_Numeros.sete
        self.seis = Entidades_Numeros.seis
        self.cinco = Entidades_Numeros.cinco
        self.quatro = Entidades_Numeros.quatro
        self.dois = Entidades_Numeros.dois
        self.tres = Entidades_Numeros.tres
        self.um = Entidades_Numeros.um

        self.lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.lista_um = self.lista_um
        self.lista_dois = self.lista_dois
        self.lista_tres = self.lista_tres
        self.lista_sete = self.lista_sete
        self.lista_quatro = self.lista_quatro
        self.lista_cinco = self.lista_cinco
        self.lista_seis = self.lista_seis
        self.lista_oito = self.lista_oito
        self.lista_nove = self.lista_nove

    def lista_numeros(self):
        self.lista_um = copy.deepcopy(self.lista_numeros)
        self.lista_dois = copy.deepcopy(self.lista_numeros)
        self.lista_tres = copy.deepcopy(self.lista_numeros)
        self.lista_sete = copy.deepcopy(self.lista_numeros)
        self.lista_quatro = copy.deepcopy(self.lista_numeros)
        self.lista_cinco = copy.deepcopy(self.lista_numeros)
        self.lista_seis = copy.deepcopy(self.lista_numeros)
        self.lista_oito = copy.deepcopy(self.lista_numeros)
        self.lista_nove = copy.deepcopy(self.lista_numeros)

    def numero_um(self):
        self.um = self.um
        self.um = self.lista_um[0]
        return self.um

    def numero_dois(self):
        self.dois = self.dois
        self.dois = self.lista_dois[1]
        return self.dois

    def numero_tres(self):
        self.tres = self.tres
        self.tres = self.lista_tres[2]
        return self.tres

    def numero_quatro(self):
        self.quatro = self.quatro
        self.quatro = self.lista_quatro[3]
        return self.quatro

    def numero_cinco(self):
        self.cinco = self.cinco
        self.cinco = self.lista_cinco[4]
        return self.cinco

    def numero_seis(self):
        self.seis = self.seis
        self.lista_seis = self.lista_seis
        return self.seis

    def numero_sete(self):
        self.sete = self.sete
        self.lista_sete = self.lista_sete
        return self.sete

    def numero_oito(self):
        self.oito = self.oito
        self.lista_oito = self.lista_oito
        return self.oito

    def numero_nove(self):
        self.nove = self.nove
        self.lista_nove = copy.deepcopy(self.lista_numeros)
        return self.nove
