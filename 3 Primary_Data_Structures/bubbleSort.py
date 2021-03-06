#Implementing Bubble Sort
def bubbleSort(ls):
    i = len(ls)-1 #index of last element
    while i > 0:
        j =0 #first element
        while j < i:
            if ls[j] > ls[j+1]:
                #swap
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp
            j+=1
        i-=1

def main():
    myList = [15,8, 20, 12, 5, 22, 7]
    print(myList)
    bubbleSort(myList)
    print(myList)


main()

