n =int(input())
if n % 10 == 1 and not n % 100 == 11:
    print(str(n) + " программист")
elif 1 < n % 10 < 5 and not n % 100 == 12 and not n % 100 == 13 and not n % 100 == 14:
     print(str(n) + " программиста")
else:
     print(str(n) + " программистов")