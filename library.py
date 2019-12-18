#################

def multiple_del(x, *y):
    """ x is the 'main' list and *y are the indices of elements to deleted"""
    y1 = list(y)
    y1.sort(reverse=True)
    for i in y1:
        del x[i]
    return x

x = list(range(9))
y = [0, 2, 3, 8]

print(multiple_del(x, *y))

#################
