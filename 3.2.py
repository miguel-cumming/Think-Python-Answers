def right_justify(str):
    y = 70 - len(str)
    print((" " * y) + str)

def call_twice(function, value):
    function(value)
    function(value)

#test1
call_twice(right_justify, 'foo')

def call_four(function, value):
    call_twice(function, value)
    call_twice(function, value)

#test2
call_four(right_justify, 'foo')