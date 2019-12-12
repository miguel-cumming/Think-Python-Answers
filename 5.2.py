#5.2.1

def fermat(a,b,c,n):
    if (a > 0) and (b > 0) and (c > 0) and (n > 2):
        if (a ** n + b ** n == c ** n):
            print("Fermat's Theorem broken")
        else: print("Fermat's Theorem upheld")
    else: print("Fermat's criteria not met")

#fermat(1, -1, 20, 100)

#5.2.2
def fermat2():
    a = int(input('Input: a \n'))
    b = int(input('Input: b \n'))
    c = int(input('Input: c \n'))
    n = int(input('Input: n \n'))
    fermat(a,b,c,n)

#fermat2()

#fun
def fermat3():
    a = int(input('Input: a \n')) 
    if a > 0:
        b = int(input('Input: b \n'))
        if b > 0:
            c = int(input('Input: c \n'))
            if c > 0:
                n = int(input('Input: n \n'))
                if n > 0:
                    fermat(a,b,c,n)
                else: print("Fermat's criteria not met")
            else: print("Fermat's criteria not met")
        else: print("Fermat's criteria not met")
    else: print("Fermat's criteria not met")
        

fermat3()


