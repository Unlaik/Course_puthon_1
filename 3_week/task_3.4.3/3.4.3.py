import collections
with open("../task_3.4.4/text.txt", 'r') as data:
    dictionary = {} #create new dict
    #strings = Data.readlines()  #cycle for ever sting in document
    #for string in strings:
    string = data.read().replace('\n', ' ').lower().split()  # create list from string, and split with space
    for word in string:  # every element in list
        count = string.count(word)  # get count of element in list
        dictionary[word] = count  # add element and count
    new_dict = collections.OrderedDict(sorted(dictionary.items()))
    out_count = max(new_dict.items(), key=lambda x: x[1])  # create tuple key with maximum value


with open("../task_3.4.4/text.txt", 'w') as data:
    data.write(f"{out_count[0]} {out_count[1]}")  #add  key and maximum value of keys