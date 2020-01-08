def right_justify(str):
    y = 70 - len(str)
    print((" " * y) + str)
    
#remark that negative string multiplication returns the empty string, so if len(str) > 70 it is inconsequential

right_justify('hi')
right_justify('helllllo')
