# Ch04-01
# Sequence / non-sequence 
# 파이썬 자료형 - 시퀀스형
#   컨테이너(container:서로 다른 자료형을 담을 수 있음- list, tuple, deque, collections)
#   플랫(flat: 한개의 자료형만 담을 수있음- str, bytes, bytearray, array.array, memoryview )
#   참고) tuple은 수정불가
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 지능형 리스트( list comprehension)
chars = '+@#!@^$%&$@'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))
    
print(code_list1)

code_list2 = [ord(s) for s in chars] # -> 요렇게 쓰는게 조금 더 속도가 빠르대 
print(code_list2)

# comprehending list + map +filter

code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x : x> 40, map(ord, chars))) # code_list3을 map, lambda이용

print(code_list3)
print(code_list4)
print([chr(s) for s in code_list4])

# Generator 제네레이터 생성
# 제네레이터는 기본적으로 sequence타입이고 generator를 이용해 메모리 사용량을 줄여 효과적으로 메모리를 사용할수있음.
# 보고픈 결과값만 출력함 제네레이터는 그래서 메모리 많이 안사용해도 됨.=> 한번에 한 개의 항목을 생성(메모리유지x) 

tuple_g = [ord(s) for s in chars] # list comprehension
tuple_g = (ord(s) for s in chars) # generator

print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g)) # tuple_g의 전체 값이 나오는게 아니라 하나씩 나옴. iteration이 끝날때까지.

import array 
array_g  = array.array('I', (ord(s) for s in chars))
print(array_g)
print(array_g.tolist())

# generator example

print(('%s' % c + str(n) for c in ['a','b','c','d'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['a','b','c','d'] for n in range(1,21)):
    print(s)


# list 주의 
# 깊은 복사 얕은 복사 

marks1 = [['~']*3 for n in range(4)]
marks2 = [['~']*3] *4
print(marks1)
print(marks2)  # marks1,2 같은 결과값이지만 수정할때 접근할떄 달라짐

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1)
print(marks2)  # -> 모든 ['~']*3의 [1]자리 원소가 'X'로 바뀜. 두 가지 경우 결과가 다름. 
# marks2를 만들때는 ['~']*3라는 값을 4번복사해서 만든것이라서 ['~']*3의 id를 동일하게 복사해서 사용하고 marks1[0][1]의
# 원소가 바뀌면 동일한 id를 4번복사해서 만든것이기에 똑같이 'X'가 반영되어 나타남. id(marks2[0][1]) == id(marks2[1][1])
# for를 써서 하나씩 할당해준경우는 id(marks1[0][1]) ~= id(marks1[1][1]) id가 같지 않음.
print([id(i) for i in marks1])
print([id(i) for i in marks2])