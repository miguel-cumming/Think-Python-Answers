#arbitary number of arguments 
def f(*args):
    return sum(args)


print(f(1, 2, 3))

def g(*args):
    y = 0
    for i in args:
        y += i
    return y
    

print(g(1, 2, 3))

#zip-object defined by pairs
x = 'abc'
y = 1, 2, 3

z = zip(x,y)

for i, j in z:  #for interacts with a zip object uniquely 
    print(i, j)

#zip-object defined by triplets

q = 1.5, 2.5, 3.5 

z = zip(x,y,q)

for i, j, k in z: 
    print(i, j, k)


#has_match
def has_match(s1, s2):
    """ determines whether there exists an index where s1, s2
        share the same value
    """
    z = zip(s1, s2)
    for x,y in z:
        if x == y:
            return True
    return False

s1 = 1,2,3,4,1 #s1, s2 may be an iterable (tuple, list, string)
s2 = 3,4,21,4,1

x1 = 'hello'
x2 = 'hell'

print(has_match(s1,s2))
    
print(has_match(x1,x2))

#enumerate
x1 = 'hello'
x2 = 'hell'

z = zip(x1, x2)

for i, v in enumerate(x1):
    print(i, v)

for i, v in enumerate(x2):
    print(i, v)

for i, v in enumerate(z):
    print(i, v)

#creating a dictionary with a list of tuple-pairs

x = [ ('a',1), ('b', 2), ('c', 3)]

d1 = dict(x)

print(d1['c'])

d1.update([('d', 4), ('e', 5)]) #d.update method 

print(d1)


#dict_item object (similar to a zip object of two sequences)
k  = d1.items()

for i, j in k:
    print(i, j)

#tuple-keys
phone_book = dict()

phone_book['Cumming', 'Miguel'] = '000 000 001'
phone_book['Cumming', 'Daniel'] = '000 000 002'
phone_book['Cumming', 'Isabel'] = '000 000 003'
phone_book['Cumming', 'Juan'] = '000 000 004'

for i, j in phone_book:
    if j == 'Juan':
        print(phone_book[i,j])

#sorted() creates a new, sorted tuple

#reversed() creates a iteror object, like dict.items()
        
