import decimal
from decimal import Decimal
import random
import time
import sys


class Qualean:

    def __init__(self, real):
        super().__init__()
        self.real = real
        self.imag = self.real * Decimal(str(round(random.uniform(-1,1),10)))

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        if (real != 1) and (real != -1) and (real != 0):
            raise ValueError("Real Number must be either -1, 0 , 1")
        else:
            self._real = int(real)

    def __repr__(self):
        return '{0}'.format(bool(self.real))

    def __str__(self):
        return '{0}'.format(self.imag)

    def __bool__(self):
        return bool(self.real)

    def __and__(self, value):
        return self.imag and value.imag

    def __or__(self, value):
        return self.imag or value.imag

    def __add__(self, value):
        return self.imag + value.imag

    def __eq__(self, value):
        return self.imag == value.imag

    def __float__(self):
        return float(self.imag)

    def __ge__(self, value):
        return self.imag >= value.imag

    def __gt__(self, value):
        return self.imag > value.imag

    def __invertsign__(self):
        return -self.imag

    def __le__(self, value):
        return self.imag <= value.imag

    def __lt__(self, value):
        return self.imag < value.imag

    def __mul__(self, value):
        return self.imag * value.imag

    def __sqrt__(self):
        return self.imag.sqrt()




#__and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__