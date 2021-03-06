#Study of Object Creation, Life of Object, __init__ and __del__, self reference

#Object Creation
#Object creation is a 2 step process
# 1) Memory Allocation
# 2) Initialization of object attributes by __init__

class Person:
    # __init__
    #A special method of the class.
    #Auto executes on object creation.
    #Defines an initializes the object attributes
    def __init__(self):
        print('in init')
        self.name = 'Baby' #attribute defined on first use
        self.age = 0 #attribute defined on first use

    def setName(self, name):
        self.name = name

    #self
    #self is the first formal parameter for methods of a class.
    #It is a reference of type current class.
    #It is auto initialized with address of the caller object of the method.
    #It is used to access the object's attributes and methods.

    def setAge(self, age):
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)

    #A special method of the class
    #It is auto invoked by the Python Memory Managers garbage collector
    #(because object has become unreferenced), as a chance for the class
    #to clean up the resources used by the object.
    #After __del__ the object is removed from memory (no longer exists).
    def __del__(self):
        print('Life of the object ends')


def fx():
    p = Person() #object creation
    p.setAge(10) #setAge(p, 10)
    p.display() #display(p)
    print('~~~~~~~~')

def main():
    print('-----in main-----')
    print('-----before call to fx-----')
    fx()
    print('-----after call to fx-----')
    print('-----main ends-----')

main()
