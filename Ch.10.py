def f(x):
    for i in range(len(x)):
        x[i] = x[i] + 1
    return x

x = [1, 2, 3]
print(f(x))

#
def f(x):
    y = 0
    for i in x:
        y += i
    return y

x = [1, 2, 3]

print(f(x))

print(sum(x))

#
