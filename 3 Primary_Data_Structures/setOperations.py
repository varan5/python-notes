#set operations on list

def sequentialSearch(ls, size, val):
    i =0 #search begins with the first element
    while i < size:
        if ls[i] == val: #comparison for equality
            return i #index (position) of element
        i+=1 #sequentially next

    #no match
    return -1 #(flag value)

def scanUniqueValues(ls, n):
    i = 0
    while i < n:
        temp = int(input("Enter a unique value "))
        result = sequentialSearch(ls, i, temp)
        if result == -1:
            ls.append(temp)
            i+=1
        else:
            print('Duplicate value, not added')

def union(ls1, ls2):
    ls3 = []#empty list

    #ls3.extend(ls1) #copy all elements of ls1 into ls3
    i =0
    size1 = len(ls1)
    while i < size1:
        ls3.append(ls1[i])
        i+=1

    size2 = len(ls2)
    i =0
    while i < size2:
        result = sequentialSearch(ls1, size1, ls2[i])
        if result == -1:
            ls3.append(ls2[i])
        i+=1

    return ls3



def intersect(ls1, ls2):
    ls3 = []#empty list

    size1 = len(ls1)
    size2 = len(ls2)
    i =0
    while i < size2:
        result = sequentialSearch(ls1, size1, ls2[i])
        if result != -1:
            ls3.append(ls2[i])
        i+=1

    return ls3

def minus():
    print('To be implemented by Student...')

def symmetricDifference():
    print('To be implemented by Student...')

def main():
    ls1 = [] #empty
    ls2 = [] #empty
    print('Provide data for first list ')
    scanUniqueValues(ls1, 7)
    print('Provide data for second list ')
    scanUniqueValues(ls2, 5)

    print(ls1)
    print(ls2)
    ls3 = union(ls1, ls2)
    print('Union', ls3)
    ls4 = intersect(ls1, ls2)
    print('Interesect', ls4)

main()