#Study of sets
#A set is an unordered collection of unqiue elements.
#FYI: A set doesnt support indexing and slicing.

def setStudy():
    #an empty set
    #s = set()
    a = {1,2,3,4,5}
    b = {1,3,5,7,9}

    #union
    #c = a.union(b)
    #d = a | b
    #set a updated to hold the union of a and b
    #a.update(b)

    #intersect
    #c = a.intersection(b)
    #d = a & b
    # set a updated to hold the intersection of a and b
    #a.intersection_update(b)

    #minus
    #c = a.difference(b)
    #d = a - b
    # set a updated to hold the difference of a and b
    #a.difference_update(b)

    #symmetric difference: (a|b)-(a&b)
    c = a.symmetric_difference(b)
    d = a ^ b
    # set a updated to hold the symmertic difference of a and b
    #a.symmetric_difference_update(b)

    #output
    print(a)
    print(b)
    print(c)
    print(d)

    print('-----------------')

    #removing elements
    x = a.pop() #pop removes an item in the set, but since the set is unordered, you can't determine which item was removed, it's arbitrary.
    print(x)
    #a.remove(4) #given element is removed, nothing returned. If element not found then KeyError is raised.
    #a.discard(4) #given element is removed, nothing returned. If element not found then no error raised.
    #a.clear() #empty the set
    print(a)

    print('-----------------')
    #adding values
    a.add(6)#if value is not in set, it gets added
    a.add(5)#otherwise not
    a.update([1,5,10,15])
    print(a)

def main():
    setStudy()

main()

