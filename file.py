print('hello world')
import math
T = int(input())

while T > 0:
    num = int(input())
    sqrt = int(math.sqrt(num))

    if sqrt * sqrt == num:
        print('1')
    else:
        print('0')

    T = T - 1
