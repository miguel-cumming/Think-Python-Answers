def f(x):
    for i in range(1, len(x)):
        x[i] = x[i] + x[i-1]
    return x

x = [1, 2, 3, 4]

print(f(x))
