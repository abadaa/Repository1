class Fractions:
    def __init__(self, num, den=None):
        self.num = num
        self.den = den
    def add(self, self2):
        if(self.den == 0 or self2.den == 0):
            return ValueError
        elif(self.den==None and self2.den==None):
            sum = self.num + self2.num
        else:
            sum = Fractions(self.num + self2.num, self.den)
        return sum
    def __eq__(self, other):
        if(type(self) == type(other)):
            return self.num == other.num and self.den == other.den
        return TypeError
        