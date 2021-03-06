#Nested functions and Closures
#--------------------------------------
#A nested function is a function defined inside another function.
#It is created, used and destroyed dynamically, by the enclosing function,
#thus hiding it from the global scope.
#It has read only access of variables of the enclosing scope.

#A Closure is memory object in the nested function, that remembers data
#of the enclosing scope even if they are not present in memory.


#Higher order function
#---------------------------
#Higher order functions are functions that operate on other functions.
#Ideally a higher order function takes another function as argument
#and adds meta code that processes input and or output of the function
#received as argument.
#For this it may define a nested function as well.


#Decorators
#-----------------
#Python decorators are for adding functionality (code injection)
#into an existing code (wrapped function).
#This is also called "Meta Programming" as a part of the program tries
#to modify another part of the program at compile time.

#Python decorators are implemented as Higher order functions that:
#1) Take other functions (wrapped functions) as arguments.
#2) Create a nested function (wrapper function) which hosts meta code, invokes wrapped function through closure.
#3) Returns reference to nested function (wrapper functions).
#4) Updates wrapped function reference to refer to nested function (wrapper functions).

def makeBeautiful(fp): #Higher Order function
    def wrapperfn(string): #Wrapper function
        print('---------------') #meta code
        fp(string.upper()) #call to wrapped function
        print('---------------') #meta code
    return wrapperfn

def makeOdd(fp): #Higher Order function
    def wrapperfn(x): #Wrapper function
        res = fp(x) #Wrapped function
        if res% 2 == 0: #meta code to process the return of wrapped function
            res+=1 #meta code
        return res #processed return
    return wrapperfn


@makeOdd
def square(n):
    return n*n

@makeOdd
def cube(n):
    return n*n*n

@makeBeautiful
def greet(msg):
    print( msg)

def main():
    print(cube(10))
    print(square(2))
    greet('Hello Python')

main()
