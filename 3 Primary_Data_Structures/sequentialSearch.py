#Implementation of Sequential Search
#Refer: sequentialSearch.png

def sequentialSearch(ls, val):
    i =0 #search begins with the first element
    size = len(ls)
    while i < size:
        if ls[i] == val: #comparison for equality
            return i #index (position) of element
        i+=1 #sequentially next

    #no match
    return -1 #(flag value)

def main():
    ls = [5,1,10,20,8,12,7,19,50,3,29,23]
    print(ls)
    val = int(input('Enter value to search'))
    result = sequentialSearch(ls, val)
    if result == -1:
        print(val, 'not found')
    else:
        print(val, 'found at index', result)

main()