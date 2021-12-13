class Entidades_Numeros():
    def __init__(self, um, dois, tres, quatro, cinco, seis, sete, oito, nove):
        self.__um = um
        self.__dois = dois
        self.__tres = tres
        self.__sete = sete
        self.__quatro = quatro
        self.__cinco = cinco
        self.__seis = seis
        self.__oito = oito
        self.__nove = nove

    @property
    def um(self):
        return self.__um

    @um.setter
    def um(self, um):
        self.__um = um

    @property
    def dois(self):
        return self.__dois

    @dois.setter
    def dois(self, dois):
        self.__dois = dois

    @property
    def tres(self):
        return self.__tres

    @tres.setter
    def tres(self, tres):
        self.__tres = tres

    @property
    def quatro(self):
        return self.__quatro

    @quatro.setter
    def quatro(self, quatro):
        self.__quatro = quatro

    @property
    def cinco(self):
        return self.__cinco

    @cinco.setter
    def cinco(self, cinco):
        self.__cinco = cinco

    @property
    def seis(self):
        return self.__seis

    @seis.setter
    def seis(self, seis):
        self.__seis = seis

    @property
    def sete(self):
        return self.__sete

    @sete.setter
    def sete(self, sete):
        self.__sete = sete

    @property
    def oito(self):
        return self.__oito

    @oito.setter
    def oito(self, oito):
        self.__oito = oito

    @property
    def nove(self):
        return self.__nove

    @nove.setter
    def nove(self, nove):
        self.__nove = nove



