def is_duplicate(x): #general implentation
    y= []
    for i in x:
        if i in y:
            return True
        else: y.append(i)
    return False

x = [1, 2, 3, 4, 4]
y = list(range(5))
print(is_duplicate(x))
print(is_duplicate(y))

#implentation for sortable lists 
def is_duplicate2(x):
    y = x[ : ]
    y.sort()
    for i in range(1, len(y) - 1):
        if y[i] == y[i -1] or y[i] == y[i + 1]:
            return True
    return False

print(is_duplicate2(x))
print(is_duplicate2(y))
