int_data = 12
float_data = 3.14
complex_data = 1 + 5j
str_data1 = 'Python'
str_data2 = '한글'
list_data = [1, 2, 3]
tuple_data = (1, 2, 3)                # 리스트와 비슷하지만 요소 값을 변경할 수 없음
dict_data = {'a': 'False', 'b': 'True'}   # 키:값으로 구성된 자료형
dict_data2 = {0: 'False', 1: 'True'}   # 키:값으로 구성된 자료형

print(list_data, end="")    # 파이썬 print는 \n이 포함되있기 때문에 end==""을 통해서 없이 print하는 기능으로 번경 가능 
print(str_data2)
print(tuple_data[1])
print(dict_data['b'], end=" ")
print(dict_data2[0])

print()
listdata = ['a', 'b', 'c']
if 'a' in listdata:
    print('a 는 listdata안에 존재하는 요소입니다')
    print(listdata)
else:
    print('해당 입력값은 listdata안에 존재하지 않습니다.')
