#I think my solution is more elegant than the offical one http://greenteapress.com/thinkpython2/code/grid.py
#In particular, the official solution exploits vacuous functions wheras I exploit vacuous 'arguments'
#The advantadge of this is seen especially in pt. 2

def call_two(function, value1, value2):
    function(value1, value2)
    function(value1, value2)

def call_four(function, value1, value2):
    call_two(function, value1, value2)
    call_two(function, value1, value2)


fragment1 = '+' + ('-' * 4)
fragment2 = '|' + (' ' * 4)

line1 = fragment1 * 2 + '+'
line2 = fragment2 * 2 + '|'

def block(line1, line2):
    print(line1)
    call_four(print, line2, '')

call_two(block, line1, line2)
print(line1)

#pt.2
new_line1 = fragment1 * 4 + '+'
new_line2 = fragment2 * 4 + '|'

call_four(block, new_line1, new_line2)
print(new_line1)

