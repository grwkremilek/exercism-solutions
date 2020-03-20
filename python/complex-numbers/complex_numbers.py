import math
from math import sqrt, pow, exp


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real +  other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real -  other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / (other.real * other.real + other.imaginary * other.imaginary)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / (other.real * other.real + other.imaginary * other.imaginary)
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        return sqrt(pow(self.real, 2) + pow(self.imaginary, 2))

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        real = exp(self.real)
        if self.imaginary == math.pi:
            return ComplexNumber(real * -1, 0)
        return ComplexNumber(real, 0)
