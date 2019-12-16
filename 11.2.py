def dict_inverse(d):
    inverse = dict()
    for i in d:
        v = d[i]
        if inverse.setdefault(v, [i]) != [i]:
            inverse[v].append(i)
    return inverse

d = {'a':1, 'b':2, 'c':2,'d':2, 'e':1}

print(dict_inverse(d))
        
