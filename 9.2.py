path = '/users/juancumming/documents/words.txt'
fin = open(path)

word_count = 0 
for i in fin:
    word_count = word_count + 1

fin2 = open(path)

y = 0
for i in fin2:
     if 'e' not in i:
         y = y + 1
   

print(word_count)
print(y)
print((y / word_count) * 100)
