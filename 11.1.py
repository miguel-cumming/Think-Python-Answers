path ='/users/juancumming/Desktop/Think Python/words.txt'
fin = open(path)

d = dict()

for i in fin:
    i = i.strip()
    d[i] = i

print(d['hora'])
print(d['horat'])
