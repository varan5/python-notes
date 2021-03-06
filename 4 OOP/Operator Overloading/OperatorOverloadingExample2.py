#Operator Overloading: Example 2
class Complex:
    def __init__(self, r= 0, i= 0):
        self.r = r
        self.i = i

    def display(self):
        if self.i == 0:
            print(self.r)
        elif self.i < 0:
            print(self.r,  self.i, 'i', sep='')
        else:
            print(self.r, '+',self.i, 'i', sep='')

    def __add__(self, other):
        #logic to add the complex numbers
        temp = Complex()
        temp.r = self.r + other.r
        temp.i = self.i + other.i
        return temp

    def __sub__(self, other):
        #logic to subtract the complex numbers
        temp = Complex()
        temp.r = self.r - other.r
        temp.i = self.i - other.i
        return temp

    def __mul__(self, other):
        #logic to subtract the complex numbers
        temp = Complex()
        temp.r = self.r * other.r - self.i * other.i
        temp.i = self.r * other.i + other.r * self.i
        return temp

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i

def main():
    c1 = Complex(20, 5)
    c2 = Complex(14, 2)
    #c3 = c1 + c2  #c1.__add__(c2)  ---> __add__(c1, c2)
    #c3 = c1 - c2  #c1.__sub__(c2)  ---> __sub__(c1, c2)
    c3 = c1 * c2   #c1.__mul__(c2)  ---> __mul__(c1, c2)

    c1.display()
    c2.display()
    c3.display()

    if c1 == c2:
        print('c1 and c2 are equal')
    else:
        print('c1 is not equal to c2')

main()


