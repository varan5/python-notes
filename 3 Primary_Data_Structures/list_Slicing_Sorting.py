#List Processing

def listSlicing():
    ls = [11,12,13,14,15,16,17,18,19,20];
    print(ls) #entire list
    print(ls[2]) #one element

    #ls[inclusiveStartIndex:exclusiveEndIndex:step)
    print(ls[2:7]) #slice ranging elements 2-6
    print(ls[5:6])  # slice one element 5
    print(ls[2:]) #slice ranging elements 2-end
    print(ls[2:7:2])  # slice ranging elements 2-6 step 2
    print(ls[:]) #entire list
    print(ls[1::2]) # elements at odd indices
    print(ls[-5:-2])#elements from index -5 to -3
    print(ls[-2:-5:-1])  # elements from index -2 to -4
    print(ls[::-1]) #reverse the list

def lastDigit(val):
    return val%10

def listSorting():
    ls1  = [15,9,1,123,8,3,4]
    print('Original', ls1)
    ls1.sort()
    print('Sorted',ls1)
    ls1.sort(reverse= True)
    print('Reverse Sorted', ls1)
    ls1.sort(key=lastDigit)
    print('LastDigitwise', ls1)

    ls2 = ['abc','xyz', 'AAA', 'Abc', 'PqR', 'lmn']
    print('Original',ls2)
    ls2.sort()
    print('Sorted', ls2)
    ls2.sort(key= str.upper)
    print('Sorted Ignoring ASCII', ls2)

def main():
    #listSlicing()
    listSorting()

main()