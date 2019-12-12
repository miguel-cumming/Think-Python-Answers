def f():
    while True:
        x = input('Input Expression:' + ' ')
        if x == 'done':
            break
        y = x
        print(eval(x))
    print(eval(y))

f()
