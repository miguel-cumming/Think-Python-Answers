def triangle(a,b,c):
    if (a > 0) and (b > 0) and (c > 0):
        if (a > b + c) or (b > a + c) or (c > a + b):
            print('Triangle not possible')
        else: print('Triangle possible')
    else: print('Bad inputs')

def triangle2():
    a = int(input('Input a : \n'))
    b = int(input('Input b : \n'))
    c = int(input('Input c : \n'))
    triangle(a,b,c)

triangle2()
