class Fractions:
    def __init__(self, num, den=None):
        self.num = num
        self.den = den
    def add(self, other):
        if(self.den == 0 or other.den == 0):
            return ValueError
        elif(self.den==None and other.den==None):
            sum = self.num + other.num
        elif(self.den != other.den):
            sum = Fractions(self.num *other.den + other.num * self.den, self.den * other.den)
        else:
            sum = Fractions(self.num + other.num, self.den)
        return sum
    def __eq__(self, other):
        if(type(self) == type(other)):
            return self.num == other.num and self.den == other.den
        return TypeError
        