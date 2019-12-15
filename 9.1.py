path = '/users/juancumming/documents/words.txt'
fin = open(path)

for i in fin:
    i = i.strip()
    if len(i) > 20:
        print(i)
