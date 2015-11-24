# coding: utf-8
# license: GPLv3
from gameunit import *


class Hero(Attacker):
    _experience=None
    _name=None

    def attack(self, target):
        target._health -= self._attack


    def __init__(self, name = 'Player1' ):
        self._health = 100
        self._attack = 50
        self.experienxe = 0
        self._name = name


    def gameOver(self):
            if self._health <= 0:
                print('К сожалению, Вы проиграли...')


#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
