#How many values can a function return?
#Ideally a function returns zero or one value.

#But, Python allows returning multiple values
#comma separated and associated with the return statement.

#Internally the comma separated values are grouped (packed)
#to form a tuple and that one tuple is returned.

#At the point of call the tuple can either by received
#as one tuple or can be auto ungrouped (unpacked) into
#individual values. For unpacking it is mandatory that
#the number of identifiers receiving the return must be
#equal to the size of the tuple, otherwise operation fails.


def fx(num):
    x = num *1
    y = num *2
    z = num *3
    #multiple result generated
    return x,y,z

def main():

    print('----------------')
    result = fx(5) #return received as a tuple
    # process like a tuple
    for i in result:
        print(i)
    print('----------------')
    a,b,c = fx(10) #return received in 3 variables
    # process like variables
    print(a,b,c)
    print('----------------')

    #Observe the use of less/more number of identifiers
    #to receive the return.
    #Here Python's tuple unpacking mechanism fails resulting
    #in ValueError (assignment not possible).

    #p,q = fx(20) #too many values to unpack (expected 2, got 3)
    #l,m,n,o = fx(30) #not enough values to unpack (expected 4, got 3)

main()