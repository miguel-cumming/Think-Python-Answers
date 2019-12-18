#lists can be mutuated as you loop through them, but dictionaries can't 
def f(x):
    for j in x:
        if j > 0:
            x.append(-1)
    return x


x = [1, -1, 2, 3, -2]

print(f(x))

def g(d):
    d1 = d.items()
    for i, j in d1:
        if i > 0:
            d[j] = -1

d = {1:-1, 2:-2, 3:-3}

print(g(d))
