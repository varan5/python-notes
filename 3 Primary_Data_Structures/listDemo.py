#List
#A list is a collection of values arranged in seqeuntial order.
#It can expand/shrink dynamically.
#It is indexed i.e. the elements are identified by their position (index).
#0 based incrementing index allows processing the list elements left to right.
#-1 based decrementing index allows processing the list right to left.

def listDemo():
    #empty = list() #creates an empty list
    #also_empty = [] #creates an empty list
    l1 = [11,22,33,44,55]
    print(l1) #display the list
    #print(l1[3]) #element 4
    #print(l1[-2]) #element 4
    #print(l1[99]) #invalid index result IndexError

    #loop through the list
    i =0
    size = len(l1)
    while i < size:
        #l1[i] *= 10 #element updated (written)
        print(l1[i])  #element read
        i+=1

    #for each loop to iterate over a list (sequence)
    for x in l1:
        #x*=10 #copy (and not the element) updates
        print(x)

def main():
    listDemo()

main()