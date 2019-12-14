def f(x):
    del x[0]
    del x[-1]
    return x

x = list(range(9))

print(f(x))
