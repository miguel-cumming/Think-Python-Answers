#Ch. 6/ 7

def f():
    while True:
        x = input('Input Expression:' + ' ')
        if x == 'done':
            break
        y = x
        print(eval(x))
    print(eval(y))

f()


#Ch. 8

#Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.

def f():
    y = ''
    for i in 'JKLMNOP':
        if i == 'O':
            y = y + i + 'uack,' + ' '
        else: y = y + i + 'ack,' + ' '
    y = y + 'Q' + 'uack'
    print(y)

f()

#

def f(n):
    while n > 0:
        return n  # exits loop immediately. would not be the case if 'print'

print(f(7))

# reversing strings, skip slicing
def f(x):
    return x == x[ : : -1]

print(f('noon'))
