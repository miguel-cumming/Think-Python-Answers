import random

def is_duplicate(x):
    y= []
    for i in x:
        if i in y:
            return True
        else: y.append(i)
    return False

def random_birthday_list():
    y = []
    for i in range(23):
        y.append(random.randint(1,365))
    return y

def probability(n):
    count = 0
    for i in range(n):
        if is_duplicate(random_birthday_list()):
            count = count + 1
    return count / n

def mean_probability(s, n):
    y = 0
    for i in range(s):
        y =  y + probability(n)
    return y / s

print(mean_probability(10, 1000))
print(mean_probability(10, 1000))
print(mean_probability(10, 1000))
print(mean_probability(10, 1000))
print(mean_probability(10, 1000))
