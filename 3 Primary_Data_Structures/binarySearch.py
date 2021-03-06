#Implementation of binarySearch
#Refer: binarySearch.png

def binarySearch(ls, val):
    x = 0 # lower boundary
    y = len(ls)-1 # upper boundary
    while x <=y:
        m = (x+y)//2
        if val == ls[m]: #match
            return m
        elif val < ls[m]: #look at lhs
            y = m -1
        elif val > ls[m]: #look at rhs
            x = m + 1

    #boundaries crossed (not found)
    return -1


def main():
    ls = [5,10,12,18,20,22,25,30,31,35,40,42]
    ls.sort()
    print(ls)
    val = int(input('Enter value to search'))
    result = binarySearch(ls, val)
    if result == -1:
        print(val, 'not found')
    else:
        print(val, 'found at index', result)

main()