string = input()
string = string.lower().split() #create list from string, and split with space
dictionary = {} #create new dict
for word in string: #every element in list
    count = string.count(word) #get count of element in list
    dictionary[word] = count #add element and count
for item in dictionary:
    print(f'{item} {dictionary[item]}')     #print key and value