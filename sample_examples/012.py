scope = [1,2,3,4,5]
for x in scope:
    if x <= 3:
        print(x)
        continue
    else:
        break
    
    
for x in scope:
    print(x)
    if x >= 3:
        break