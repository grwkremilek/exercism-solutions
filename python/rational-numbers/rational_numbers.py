from __future__ import division

class Rational:
    def __init__(self, numer, denom):
        gcd, b = sorted([numer, denom])
        while b != 0:
            gcd, b = b, gcd % b
        if denom < 0 < gcd:
            gcd = -gcd
        self.numer = numer // gcd
        self.denom = denom // gcd
        
    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numerator = self.numer * other.denom + self.denom * other.numer
        denominator = self.denom * other.denom
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numer * other.denom - self.denom * other.numer
        denominator = self.denom * other.denom
        return Rational(numerator, denominator)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        if power < 0:
            self.numer, self.denom  = self.denom, self.numer
            power = abs(power)
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
