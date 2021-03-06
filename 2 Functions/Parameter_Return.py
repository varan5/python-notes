#Program to:
#Define functions
#Share data as parameters and return values.

#Refer: Parameter_Return.png
#Refer: Program Control and Data Flow.png
#Interpret the code.

#user defined function
def cube(x): #formal parameter x receives the data of actual parameter
    y = x*x*x
    #print('Cube of',x,'is',y)
    return y

#user defined function
def main():
    num = 7
    ans = cube(num)#function call with num as parameter
    print('Cube of', num, 'is', ans)

#inkove main
main() 