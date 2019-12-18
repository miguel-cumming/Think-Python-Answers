from operator import itemgetter

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else: d[c] += 1
    return d

def f(s):
    h = histogram(s)
    t = tuple(h.items())
    return sorted(t, key= itemgetter(1,0))

print(f('hello world'))
