#Program to demonstrate function definition and invokation.
#Refer: functions.png

def fx1():
    print("This is fx1")
    print("It takes no parameters")
    print("It wishes hello to all")


def fx2(user):
    print("This is fx2")
    print("It takes 1 parameter")
    print("It wishes hello to", user)

print("----------")
fx1() #call(invoke) fx1
print("----------")
fx2("FE") #call(invoke) fx2(parameter)
print("----------")
