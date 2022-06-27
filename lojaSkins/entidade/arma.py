from abc import ABC, abstractmethod


class Arma(ABC):
    @abstractmethod
    def __init__(self, arma: str):
        if isinstance(arma, str):
            self.__arma = arma

    @property
    def arma(self):
        return self.__arma

    @arma.setter
    def arma(self, arma):
        if isinstance(arma, str):
            self.__arma = arma
