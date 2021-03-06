#Implementing Insertion Sort

def insertionSort(ls):
    size = len(ls)
    i = 1
    while i < size:
        current = ls[i]#10,5,8
        j = i-1
        while j >= 0:
            if current < ls[j]:
                ls[j+1] = ls[j] #slide right
                j-=1
            else:
                break #stop the loop
        #out of j loop
        ls[j+1] = current #insertion
        i+=1


def main():
    myList = [7,10, 5, 8, 3, 6]
    print(myList)
    insertionSort(myList)
    print(myList)


main()
  