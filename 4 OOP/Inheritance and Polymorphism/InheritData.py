#Inheritance of Data
#Python allows the sub class to inherit the attributes (data) of the super class.
#By this the sub class object is expanded to contain the attributes of the super
#class and of itself.

#How it happens?
#As object of the sub class is created, its init is auto invoked.
#The sub class init invokes the init of the class while sharing the self reference.
#The super class init executes for self (sub class object) and hence performs
#super class attribute declartions for the sub class object.
#Next after the super class init, the sub class init continues to execute ahead
#and performs declarations of attributes of the sub class in the sub class object.

#So said the sub class object is defined first by the init of super class and
#then by its init. Thus expanding it to contain the data members (attributes)
#of the super class and of itself (Inhertiance of Data).

class A:
    def __init__(self, n=5):
        print('A init')
        self.x = n

    def display(self):
        print('A display()')
        print('x:', self.x)

class B(A):
    def __init__(self, n = 10, m = 20):
        A.__init__(self, n)
        print('B init')
        self.y = m
        self.z = self.x * self.y

    def display(self):
        print('B display()')
        print(self.x , '*', self.y , '=', self.z)

def main():
    b = B(4,8)
    b.display()

main()
