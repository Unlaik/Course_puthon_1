lst = [10, 5, 8, 3]
def modify_list(l):
    g = [int(i//2) for i in l if i%2==0]
    l.clear()
    l.extend(g)

modify_list(lst)