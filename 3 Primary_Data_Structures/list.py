#study of list
#list is a linear data structure.
#It can expand and shrink dynamically.
#It stores data in nodes (elements) that are indexed.

def listProcessing():
    fruits = ["apple", "mango", "Banana"]
    print(fruits)
    #sorting the list
    #fruits.sort()
    #reverse sort the list
    #fruits.sort(reverse=True)
    #Every list element will be processed for str.lower
    #and sorting will be based on outcome of the process
    #fruits.sort(key=str.lower)
    #Create a new sorted list
    copyF = sorted(fruits)
    print(fruits)
    print(copyF)



def listSlicing():
    l = [10,20,30,40,50,60,70]
    print(l)
    #display element at index 2
    print(l[2])
    #display elements at index 2,3,4
    print(l[2:5])
    # display elements from index 2 onwards (all upto the end)
    print(l[2:])
    #display values at odd indices
    print(l[1: :2])
    #display reverse
    print(l[len(l)-1: :-1])

def listCreation():
    # an empty list
    #l = []
    # output
    # print(l)

    #also
    #l = list()
    # output
    # print(l)

    #list with odd numbers
    listOdd = [1,3,5,7,9]
    #list with a tuple of even numbers
    listEven = list((2,4,6,8,10))
    #numeric list
    #listNum = list(range(10))
    #listNum  = list(2**y for y in range(10))
    #listNum =+ list(2 ** y for y in range(10) if y %2 == 1)
    listNum = list(x+y for x in range(5) for y in range(10,15) )

    #listby Concatenation
    #listNum = listOdd + listEven

    listStrings = ["hello"] * 5


    print(listOdd)
    print(listEven)
    print(listNum)
    print(listStrings)

def main():
    #listCreation()
    #listSlicing()
    listProcessing()

main() # call to main