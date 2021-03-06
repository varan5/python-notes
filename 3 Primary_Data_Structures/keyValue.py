#Dictionary and Persistant Dictionary
#Key-Value pairs

import dbm

def dictionary():
    # Define a dictionary (a key-value pair)
    dict = {'maharashtra':'mumbai', 'goa':'panaji'}

    # Add entries into it
    dict['rajasthan'] = 'jaipur'
    dict['gujrat'] = 'ahmedabad'
    dict['gujrat'] = 'gandhinagar' #key is unque, so instead for a new entry the existing one would be overwritten in value
    dict['sample1'] = 'value1'
    dict['sample2'] = 'value2'

    #display it
    print(dict)
    for k in dict:
        print(k,dict[k],sep="=")

    #delete an entry
    del(dict['sample1']) #key must exist or KeyError would be raised
    dict.pop('sample2') #key must exist or KeyError would be raised
    dict.popitem() #removes an arbitrary key value pair, if dict is empty then raises KeyError
    print(dict)

    #find a key
    if "gujrat" in dict:
        print("Gujrat data is available")
    else:
        print("Gujrat data is not available")

    #merge a dictionary
    d2 = {'mp':'bhopal', 'hp':'shimla'}
    dict.update(d2)
    print(dict)

    #list of keys
    keys = dict.keys()
    print(keys)

    #list of values
    values = dict.values()
    print(values)

def persistant_dictionary():
    #dbm.open : to open/create a dictionary
    #param1 : Dictionary Location (path)
    #param2 :
        # r : read only
        # w : read + write
        # c : read + write + create
        # n : read + write + create + overwrite if existing

    store = dbm.open("d:\\states.txt","c")
    #store['fruit'] = 'apple'
    #store['vegetable'] = 'brinjal'
    #store['flower'] = 'rose'
    #store['animal'] = 'monkey'

    try:
        del(store['animal'])
    except:
        print("animal not in dictionary")

    for k in store.keys():
        print(k.decode(), store[k].decode(), sep="=")

    store.close()

def main():
    #dictionary()
    persistant_dictionary()

main()