class Fractions:
    def __init__(self, num, den=1):
        gcd = Divisors().gcd(num, den)
        print(gcd)
        self.num = num / gcd
        self.den = den / gcd
        
    def add(self, other):
        if(self.den == 0 or other.den == 0):
            return ValueError
        elif(self.den==None and other.den==None):
            sum = Fractions(self.num + other.num)
        elif(self.den != other.den and self.den > other.den):
            if(self.den%other.den == 0 and self.den/other.den > 0):
                sum = Fractions(self.num + (other.num * (self.den/other.den)), self.den)
            else:
                sum = Fractions(self.num *other.den + other.num * self.den, self.den * other.den)
        elif(self.den != other.den and other.den > self.den):
            if(other.den%self.den == 0 and other.den/self.den > 0):
                sum = Fractions(other.num + (self.num * (other.den/self.den)), other.den)
            else:
                sum = Fractions(self.num *other.den + other.num * self.den, self.den * other.den)        
        else:
            sum = Fractions(self.num + other.num, self.den)
        return sum
        
    def __eq__(self, other):
        if(type(self) == type(other)):
            return self.num == other.num and self.den == other.den
        return TypeError
        
class Divisors:
    def __init(self):
        pass
    
    def gcd(self, a, b):
        x= 0
        if(isinstance(a, int)):
            print "yes"
        while(b != 0):
            x = b
            b = a%x
            a = x
        return a
        