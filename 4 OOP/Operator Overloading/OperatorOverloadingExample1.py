#Operator Overloading: Example 1

class Myclass:
    def __init__(self, a= 0, b= 0):
        self.x = a
        self.y = b

    def display(self):
        print(self.x, self.y)

    #lets define, how to add objects of type Myclass
    #on call:
    #"self" will be initialized as a reference to the caller object of the method
    #"other" will be initialized as a reference to the parameter object of the method

    def __add__(self, other):
        #addition logic here
        temp = Myclass()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp


def main():
    m1 = Myclass(10,20)
    m2 = Myclass(1,2)
    #Know that the LHS operand of the expression acts as the caller object for addition
    #and the RHS operand of the expression acts as the parameter object for addition.
    m3 = m1 + m2  # m1.__add__(m2) ---> __add__(m1, m2)
    m1.display()
    m2.display()
    m3.display()


main()
