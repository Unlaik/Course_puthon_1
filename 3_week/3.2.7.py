count_of_number = int(input())
dictionary = {}
for item in range(count_of_number):
    x = int(input())
    if x in dictionary:
        print(dictionary[x])
    else:
        dictionary[x] = f(x)
        print(dictionary[x])
