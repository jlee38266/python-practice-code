x = 0
while x < 10:
    x = x + 1
    if x < 3:
        continue
    print(x)
    if x > 7:
        break

print()
x = 1
total = 0
while 1:                # 항상 true이기 때문에 무한루프를 하게 된다. break를 써서 멈춰야한다.
    total = total + x
    if total > 100000:
        print(x)        # total value for x = 4487
        print(total)    # total value = 100128
        break
    x = x+1

