class Fractions:
    def __init__(self, num, den=None):
        self.num = num
        self.den = den
    def add(self, self2):
        if(self.den!=None):
            sum = Fractions(self.num + self2.num, self.den)
        else:
            sum = self.num + self2.num
        return sum
    def __eq__(self, other):
        if(self.num == other.num):
            return True
        return False
        