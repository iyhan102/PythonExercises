####### Chpater03-01
# Special methond = magic method
# 파이썬 핵심: sequence, iteration, functions, class 

# special method =  클래스 안에 정의할수있는 특별한(built-in) 메소드 => 앞서 했던 __init__, __str__ 이런거가 magic method

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10 
print(type(n))

print(n+100)
n.__add__(100) # n이라는 int 클래스 안에 사실 __add__라는 special method가 있어서 계산이된것임. 
# n.__doc__
print(n.__bool__())
print(n*100, n.__mul__(100)) # 같은 값. special method를 직접 불러서 쓸수도 있고 그냥 바로 쓸수도 있다.


#### 클래스끼리 연산 기능해보기  

class Fruit:
    x = 1000
    def __init__(self, name, price):
        self._name = name
        self._price = price    
          
    def __str__(self):
        return 'Fruit Class Info: {}, {}'.format(self._name, self._price)
    def __add__(self,x): # fruit라는 클래스로 만든 instance가 서로 더해질 때 수행되는 함수 
        return self._price + x._price
        # return self._price + Fruit.x 
    def __sub__(self, x):
        return self._price - x._price
    def __le__(self, x): # 대소 비교  x <= y
        print('Called>> __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self,x): # x>= y
        print('Called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False
        
        
s1 = Fruit('orange',7500)
# s1.__add__()
s2 = Fruit('banana',5000)

# 일반적인 계산
# print(s1._price + s2._price)

print(s1 + s2)  # __add__를 이미 클래스 안에 넣어줬기 때문에 + 연산을 알아서 인식해서 수행할수있고 무엇을 어떻게 더할지는 
# Fruit클래스 __add__안에 넣어놨기때문에 그 명령대로 더해준다. 이때 더하기 외에 다른 연산을 해주고 싶다면 예를 들어 
# price를 더한다음 1.2배를하고 싶다.-> s1+s2이지만 __add__안에 (self._price +x._price)*1.2가 있으면 이 곱하기까지 연산이 된 값이 출력된다. 
# s1+s2에서 s2가 __add__(self,x)에서 x로 인식되어 연산되는 것임. 


# magic method
# 대소 비교 magic method 
# __lt__ : x <y
# __le__ : x <= y
# __gt__ : x > y
# __ge__ : x >= y
# __eq__ : x == y
# __ne__ : x!= y 

print(s1>= s2)
print(s1<=s2) 
print(s1-s2)
print(s1)
print(s2)

### chpater 03-02
# 매직 메소드 심화 

# (5,2) + (4,3) = (9,5) 이런 vector합 이나 곱 계산하는 방법 

class Vector():
    def __init__(self, *arg): # *arg는 패키지로 통째로 받아서 클래스 안에서 풀어 쓰겠다는 의미
        """Create a vector, example: v = Vector(5,10) 
        """ 
# method단위로 주석을 호출해보면
# print(Vector.__init__.__doc__) 
        if len(arg) == 0:
            self._x, self._y = 0, 0  # 들어온 arg 없을 땐 0,0으로 
        else:
            self._x, self._y = arg # 들어온 arg를 self._x, self._y로 하나씩 받아줌(unpacking)
    
    def __repr__(self):
        """Return the vector infomation"""
        return 'Vector(%r, %r)' %(self._x, self._y) # format안쓰고 쓰는 법
    
    def __add__(self, other):
        """ Return the vector addition """
        return Vector(self._x +other._x, self._y + other._y) # 새로운 vector class를 반환    
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y) # 새로운 vector class를 반환\
    def __bool__(self):
        return bool(max(self._x, self._y))
    
    # def __str__(self):
    #     return 'vector: ({},{})'.format(self._x, self._y)
    
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

# method print

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1,v2,v3)

print(v1+v2)
print(v1*v2)
print(v1*3)
print(bool(v1))
