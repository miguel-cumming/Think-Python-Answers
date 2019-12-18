path = '/users/juancumming/desktop/think python/words.txt'
fin = open(path)

def print_elements(x):
    for i in x:
        print(i)

def f(d):
    d1 = d.items()
    d2 = dict()
    q = []
    for i,j in d1:
        if i not in d2:
            y = []
            for m, n in d1:
                if set(i) == set(m) and len(i) == len(m):
                    y.append(m)
                    d2[m] = m 
            if len(y) > 1:
                q.append(y)
    q.sort(key= len, reverse= True)
    print_elements(q)

s1 = 'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless'
    
d = dict(zip(s1, s1))

f(d)
