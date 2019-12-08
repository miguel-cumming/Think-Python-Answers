def right_justify(str):
    y = 70 - len(str)
    print((" " * y) + str)

right_justify('shoo' * 20)

#remark that negative string multiplication returns the empty string, so if len(str) > 70 it is inconsequential