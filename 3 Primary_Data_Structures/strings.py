#String Operations

def stringOp1():
    #define a string
    string = 'This is a String. It carries a message'
    print('String:')
    print('\t',string)

    #Get a upper case equivalent of the string
    print('Uppercase:')
    print('\t',string.upper())

    #Get a lower case equivalent of the string
    print('Lowercase:')
    print('\t',string.lower())

    # Get a strictly lower case equivalent of the string
    print('Lowercase (casefold):')
    another_str = str(chr(223))
    print('\t', another_str, another_str.casefold())
    print('\t', another_str, another_str.lower())

    #Get a title case (first letter of every word is capitalized) equivalent of the string
    print('Titlecase:')
    print('\t',string.title())

    #Get a capitalize (first letter is capitalized) case equivalent of the string
    print('Capitalize:')
    print('\t', string.capitalize())

    #Get a swapcase equivalent of the string
    print('swapcase:')
    print('\t', string.swapcase())

    #Get a string of specific width:
    #If specified width is less than string length
    #then specified width is ignored, otherwise
    #fillers are padded and string is either:
    #centered, left justified or right justified

    print('Centered:')
    print('\t',string.center(50,'-'))
    print('Left Justified:')
    print('\t', string.ljust(50,'-'))
    print('Right Justified:')
    print('\t', string.rjust(50,'-'))

    #String length
    print('String length:')
    print('\t', len(string))

    # Counting, Finding, Replacing : substrings
    print('Counting : es')
    print('\t', string.count('es'))
    print('Finding : es')

    try:
        print('\t', string.index('es'))
        print('\t', string.rindex('es'))
        #print('\t', string.index('es', startPos))
        #returns index if found raises ValueError if not found
    except ValueError as ve:
        print(ve)

    print('\t', string.find('es'))
    # print('\t', string.find('es', startPos))
    # returns index if found -1 if not found

    print('\t', string.rfind('es'))
    # print('\t', string.find('es', startPos))
    # returns index if found -1 if not found

    print('\t', string.replace('es', 'ES'))# all occurrences
    print('\t', string.replace(' ', 'Q', 4))# first 4 occurrences

def stringOp2(srcString, findString):
    #say findString : 'aeiou'
    #so freq would be {'a':0, 'e':0, 'i':0 ,'o':0, 'u':0}
    freq = {}.fromkeys(findString,0)

    for x in srcString:
        if x in freq:
            freq[x]+=1

    return freq


def stringOp3(src, substr):
    i = -1
    pos = []
    while True:
        i = src.find(substr, i+1)
        if i != -1:
            pos.append(i)
        else:
            break

    return pos

def main():
    #all ASCII
    #for i in range(256):
    #    print('(', chr(i),i,')', end=' ')

    stringOp1()

    string = 'Today is Saturday. Date is 21st September 2019.'
    srch = 'aeiou'
    substr = 'day'

    #print('Finding :' , srch)
    #print('In :', string)
    #freq = stringOp2(string, srch)
    #print(freq)

    #ls = stringOp3(string, substr)
    #print(ls)

main()