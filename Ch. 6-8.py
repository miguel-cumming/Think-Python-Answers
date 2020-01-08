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
greeting = 'hello, world'

greeting[ : -1] = 'p' #recall that the [ : ] excludes the last item

#

def f(n):
    while n > 0:
        return n  # exits loop immediately. would not be the case if 'print'

print(f(7))

#
def f(word, letter, frequency):
    index = 0
    freq = 0
    while index < len(word):
        if freq == frequency:
            return index - 1 
        elif word[index] == letter:
             freq = freq + 1
             index = index + 1
        else: index = index + 1
    return -1

print(f("soul's sorrow steeped-in", 's', 3))
    
# reversing strings, skip slicing
def f(x):
    return x == x[ : : -1]

print(f('noon'))
