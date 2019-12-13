
#does not non-alphabetical characters nor rotations outside 1 - 26

def encode(sentence, rotation):
    sentence = sentence.lower()
    y = ''
    for i in sentence:
        if i == ' ':
            y = y + ' '
        else: y = y + chr(((((ord(i) % 97) + rotation) % 26) + 97)) 
    return y

def decode(sentence, rotation):
    return encode(sentence, 26 - rotation)

def decrypt(sentence):
    for i in range(26):
        print(decode(sentence, i))

x =  encode("I wandered lonely as a cloud", 19)

decrypt(x)
