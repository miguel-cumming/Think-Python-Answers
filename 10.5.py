def f(x):
    y = x[ : ]
    x.sort()
    return y == x

x = [1, 2, 3]
y = [1, 3, 2]

print(f(x))
print(f(y))
