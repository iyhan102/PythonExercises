# chapter 04- 02
# 튜플 고급사용, mutable(가변), immutable(불변), sort vs. sorted

# tuple advanced
# unpacking 
print(divmod(100,9)) # divmod=몫과 나머지 반환하는 함수
print(divmod(*(100,9))) # *를 넣으면 unpacking되면서 tuple의 하나하나 원소가 divmod에 파라미터로 입력된다. 
print(*divmod(100,9)) # 결과값을 풀어버리면 튜플 형태의 결과가 아니라 풀어져서 나옴

# packing도 해줌
x,y, rest = range(10) # ->이럴경우 unpacking해줄 변수가 모라자서 에러뜸
x,y, *rest = range(10) # -> x,y에 하나씩 unpacking해서 풀고 나머지는 rest로 묶어서 할당해줌. 
print(x,y,rest) 

x,y, *rest = range(2) # -> x,y에 하나씩 unpacking해서 풀고 나머지는 rest로 묶어서 할당해줌. 없으면 []로 빈 list로 반환
print(x,y,rest) 

# 가변 / 불변

l = (15,20,25)
m = [15,20,25]

l = l *2 
m = m*2 

l *= 2
m *= 2
print(l, id(l))
print(m, id(m))  # -> tuple은 불변이기때문에 이렇게 값을 바꾸면 바꿀때마다 새로운 id를 다시 할당함-> 메모리 많이 쓰겠지
# ->list는 id를 바꾸지 않아도 값을 바꿀수있어 id가 동일함. 

# Sort vs. Soted
# 둘다 정렬의 기능이지만 차이있음. 
# reverse, key = len , key = str.lower, key = func... -> 정렬 기준 

# sorted : 정렬후 새로운 객체 반환
 
f_list = ['orange','apple','mango','papaya','lemon','strawberry']
print(f_list)
print('sorted =',sorted(f_list))
print(sorted(f_list, reverse= True)) # reverse기본은 false
print(sorted(f_list, key = len)) # 길이순으로 정렬
print(sorted(f_list, key = lambda x: x[-1])) # x[-1]기준 마지막 글자 기준으로 정렬

# sort: 정렬 후 객체 직접 변경 
print('sort-' , f_list.sort() )
print(f_list) # -> 원본 f_list가 수정됨. 
print(f_list.sort(reverse = True), f_list)
print(f_list.sort(key=len), f_list)

# list와 array의 적합한 사용법 

# 리스트기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자기반일때: array , 고속연산을 할때(머신러닝,딥러닝) 리스트에서 사용하는 함수들이 array에서도 동일하게 많이 사용됨.