# Chapter03-03
# Special methond = magic method
# 파이썬 핵심: sequence, iteration, functions, class 

# 모든 객체->id, type-> value 
# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5) 

from math import sqrt
leng1 = sqrt((pt1[0]- pt2[0])**2 +  (pt1[1]- pt2[1])**2)
print(leng1)

# named tuple 사용 
# named tuple = dict처럼 key&value로 데이터 접근이 가능한 튜플, not class under collections
from collections import namedtuple

Point = namedtuple('point', 'x y') # 벡터 인수가 2개필요하니까 x, y 두 개 (space로 ''안을 구분)
# namedtuple안의 첫번째 'point'는 key에 대한 설명이고 x,y가 key와 같은 역할임. 
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5,1.5)

print(pt3)
print(pt3.x) # 이렇게 key처럼 접근해도 되고 index로 접근해도 됨. 
print(pt3[0])

Size = namedtuple('size','x y z')
s1 = Size(1,4,5)
print(s1)

leng2 = sqrt((pt3.x- pt4.x**2 +  (pt3.y- pt4.y)**2))
print(leng2)

# namedtuple 선언 방법 (위가 ''안에 space구분 방법)

Point1 = namedtuple('point',['x','y']) # list안에 ''로 넣기 
Point2 = namedtuple('point','x, y') # ,로 구분 (space로 구분도 가능 위처럼)
Point3 = namedtuple('point','x y x class', rename = True) # key는 unique해야해서 x를 중복시키면 에러남 
# class같은 경우도 이미 class는 클래스만들때 쓰는명령어이기 때문에 중복되어 에러가 나올 수있음
# 이때 rename = Ture로 해주면 에러를 막을 수있음. default값은 rename = False
print(Point3) # -> 타입이 클래스라고 나옴 

p1 = Point1(x = 10, y = 35) # 이렇게 매핑해도 됨. 
p2 = Point2(20,40) 
p3 = Point2(45, y =20)
p4 = Point3(10,20,30,40)
print(p4) # print해보면 중복된 x와 class 변수를 난수생성해서 임의의 변수로 할당해서 넣은걸알수있음.(_2, _3 변수에 값을할당)

print(p1[0]+p2[1])
print(p1.x + p2.y) # key로 불러오기 

x, y = p1 # 묶어준걸 다시 풀어줄수도 있음

# Dict to Unpacking 
# dict타입을 namedtuple로 데이터를 unpacking해서 넣어줄수있음
temp_dict = {'x': 75, 'y': 55} 
p5 = Point2(**temp_dict)
print(p5)



# 네임드튜플의 메서드

# _make(): 새로운 객체 생성
temp = [52,38]
p4 = Point1._make(temp)
print(p4) # _make: list를 namedtuple로 변환(Point1의 네임드튜플형식을 그대로 가져와서 namedtuple화 시켜줌)

# _fields: 필드네임 확인
# key값확인
print(p1._fields, p2._fields, p3._fields) 

# _asdict(): ordered dict 으로 변환 
print(p1._asdict()) # dict 형식으로 바꿔져서 나옴 ordered dict은 나중에
print(p2._asdict())

# 실습
# 반 20명, 4개의 반(A,B,C,D)

Classes = namedtuple('Classes', ['rank','number']) 

# 그룹리스트 
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()  # .split(): 띄어쓰기(space)를 기준으로 문자를 나눠서 리스트로 만들어주는 메서드 
print(ranks)
print(numbers)

# list Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(students)
print(len(students))

# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n) 
                    for n in range(1,21)]]

print(len(students2))
print(students2)

# 출력

for s in students2:
    print(s)