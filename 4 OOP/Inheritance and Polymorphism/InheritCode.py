#Inheritance of Code
class A:
    def m1(self):
        print('A m1')

    def m2(self):
        print('A m2')


class B(A): #B is a class derived from A
    def m3(self):
        print('B m3')


def main():
    objB = B() #object of class B
    objB.m1()
    objB.m2()
    objB.m3()

main()
