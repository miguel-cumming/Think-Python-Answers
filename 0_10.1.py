def nested_summation(x):
    for i in range(len(x)):
        if isinstance(x[i], list):
            x[i] = sum(x[i])
    return sum(x)

x = [[1,2], 3, [4, 5]]

print(nested_summation(x))
