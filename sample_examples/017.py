""" 실수형 자료 이해하기 """

import time

f1 = 1.0

a = 3
a *= 2
print(a)

bool1 = True
bool2 = False
bool3 = True

print(bool1 and bool2)
print(bool1 or bool2)
print(bool1 or bool3)
print(bool1 and bool3)


strdata = 'Time is money!'
print(strdata[-4:])


print('it will stop program 5 sec')
time.sleep(10)
print('it passed 5sec')
