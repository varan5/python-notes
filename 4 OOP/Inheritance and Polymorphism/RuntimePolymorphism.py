#Type Compatibility and Runtime Polymorphism in Python

#Type Compatibility is established by inheritance.
#By type compatibility the objects of sub classes (derived) become convertible
#into super type (base), thus allowing a super class reference to refer to them.

#Method overriding is redefining an inherited method.

#Runtime Polymorphism
#Runtime polymorphism allows an operation to be performed in multiple ways.

#For runtime polymorphism:
#* A class is defined with necessary attributes and methods.
#* It is sub classed, i.e. its derived classes are defined.
#* The sub classes define extended attributes and methods.
#* Also that, the sub classes override the polymorphic method and use the
#  extended attributes and methods from within, to provide an updated approach
#  for the same (polymorphic) operation.
#* An algorithm (a process) accepts objects of super and sub types in a generic
#  reference.
#* It does its job and invokes the polymorphic (overridden method) as well.
#* On call to the polymorphic method, Python's runtime environment detects
#  the type of object in the reference and links the call to the polymorhic
#  method with the definition provided by the type (class) of the object.
#  Hence when object is of super type the core definitions execute and when
#  the object is of sub type the overridden (core + extended) definition
#  execute. Thus providing a dynamic changing behaviour of the operation.

class A:
    def identification(self):
        print('Debit Card')

    def authorization(self):
        print('ATM PIN')


class B(A): #B is a class derived from A
    #overriden code (gateway for extended code)
    def authorization(self):
        A.authorization(self) #to invoke super class overridden method
        self.otp() #invoking extended code

    #extended code
    def otp(self):
        print('OTP')


def transaction(ref):
    if not isinstance(ref, A): # if ref is not of type A
        print('Incompatible type')
        return

    print('---- Transaction starts ----')
    ref.identification()
    ref.authorization() #runtime polymorpshim applied
    print('---- Transaction ends ----')

def main():
    amt = int(input('Enter Amount '))
    if amt < 10000:
        transaction(A()) #object of A as parameter
    else:
        transaction(B()) #object of A as parameter

main()
