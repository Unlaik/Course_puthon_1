string = input()
string = string.lower().split()
dictionary = {}
for word in string:
    count = string.count(word)
    dictionary[word] = count
for item in dictionary:
    print(f'{item} {dictionary[item]}')