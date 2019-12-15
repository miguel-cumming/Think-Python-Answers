path = '/users/juancumming/documents/words.txt'
fin = open(path)

def is_good_word(word, q):
    for letter in word:
        if letter not in q:
            return False
    return True

q = input('permitted letters: ')

for i in fin:
    i = i.strip()
    if is_good_word(i,q):
        print(i)
