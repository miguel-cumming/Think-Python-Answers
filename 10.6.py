def is_anagram(x,y):
    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    return x == y

x = 'hello'
y = 'ohell'

print(is_anagram(x,y))
