# Chapter02-02
# 클래스를 이용한 객체지향 프로그래밍 

# dictionary structure

car_dicts = [
    {'car_company': 'ferrari', 'car_detail': {'color': 'white', 'horsepower': 470, 'price': 8000},
     'car_company': 'bmw', 'car_detail': {'color': 'blue', 'horsepower': 400, 'price': 9000},
     'car_company': 'audi', 'car_detail': {'color': 'red', 'horsepower': 340, 'price': 6000}}
]

print()
print()

# class structure

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
car1 = Car('ferrari',{'color': 'white', 'horsepower': 470, 'price': 8000})
print(car1) # __str__, __repr__ 없이 그냥 init만 해서 self에 입력해서 프린트하면 Car클래스에 입력한 정보를 프린트해서 확인할수없다

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):  # 사용자가 정보를 확인하기 위해서 프린트해줄때 근데 사실 __str__, __repr 다 정보를 프린트 큰 차이는없음
        return 'str: :{} - {}'.format(self._company,self._details)
    
    def __repr__(self): # 개발자 입장에서 객체를 인식할수있는 정보까지 다 볼때는 요걸로(엄격한레벨로 프린트)
        return 'str: :{} - {}'.format(self._company,self._details)

print(car1)


car1 = Car('ferrari',{'color': 'white', 'horsepower': 470, 'price': 8000})
car2 = Car('bmw',{'color': 'blue', 'horsepower': 400, 'price': 9000})
car3 = Car('audi',{'color': 'red', 'horsepower': 340, 'price': 6000})
print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(dir(car1)) # 이렇게 프린트해서 보면, class에서 내가 만든 것 포함해서 제공하는 모든 기능(함수/메서드?)들이 나옴( __str__, __repr__포함해서 __??__형식은 기본적으로
# 파이썬에서 제공하는 것임 ) 이 중에서 필요한거 바로 쓰면 됨. 

print()
print()

# list로 묶어보기
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)


# Chapter02-03
# 클래스 변수 vs. 인스턴스 변수 

class Car():
    """
    코멘트 달기 
    """
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):  # 사용자가 정보를 확인하기 위해서 프린트해줄때 근데 사실 __str__, __repr 다 정보를 프린트 큰 차이는없음
        return 'str: :{} - {}'.format(self._company,self._details)
    
    def __repr__(self): # 개발자 입장에서 객체를 인식할수있는 정보까지 다 볼때는 요걸로(엄격한레벨로 프린트)
        return 'str: :{} - {}'.format(self._company,self._details)


# self 의미 

car1 = Car('ferrari',{'color': 'white', 'horsepower': 470, 'price': 8000})
car2 = Car('bmw',{'color': 'blue', 'horsepower': 400, 'price': 9000})
car3 = Car('audi',{'color': 'red', 'horsepower': 340, 'price': 6000})

print(id(car1))
print(id(car2))
print(id(car3))
# 같은 클래스에서 만든 변수지만 각자 id다름. 각자 따로 관리됨. 그래서 calss내에서 self를 입력해서 따로 만들어주는 것임.

# dir & __dict__ 확인

print(dir(car1))
print(dir(car2))

print(car1.__dict__) # 키와 밸류형태로 self.에 들어간 변수 다 보여줌(예제 경우 _company, _details) 

print(car1.__doc__) # 클래스의 코멘트 주석을 볼수있음. 


class Car():
    """
    코멘트 달기 
    """
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):  # 사용자가 정보를 확인하기 위해서 프린트해줄때 근데 사실 __str__, __repr 다 정보를 프린트 큰 차이는없음
        return 'str: :{} - {}'.format(self._company,self._details)
    
    def __repr__(self): # 개발자 입장에서 객체를 인식할수있는 정보까지 다 볼때는 요걸로(엄격한레벨로 프린트)
        return 'str: :{} - {}'.format(self._company,self._details)

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info {} {} ".format(self._company, self._details.get('price')))
        
 
car1 = Car('ferrari',{'color': 'white', 'horsepower': 470, 'price': 8000})
car2 = Car('bmw',{'color': 'blue', 'horsepower': 400, 'price': 9000})
car3 = Car('audi',{'color': 'red', 'horsepower': 340, 'price': 6000})

       
car1.detail_info()  # detail_info메서드에 이미 print있으니까 또 print안써줘도 되지. 
car2.detail_info()
        
print(car1.__class__) # car1을 찍어낸 class가 무엇인지 나옴. (.Car가 클래스)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__)) # id가 모두 같음 모두 같은 클래스를 사용했으니까 

# Error
Car.detail_info() # self가없으니 에러 
Car.detail_info(car2) # self를 car2로 넣어줌. -> class이름으로 접근


# 클래스 변수 class variable

class Car():
    """
    코멘트 달기 
    """
    car_count = 0 # 클래스 변수-> 모든 인스턴스가 공유 
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1 # __init__가 실행될때마다 1씩 증가 ->car1,car2,car3에서 1씩증가 1,2,3이 되겠지.
        # 이 변수는 모든 인스컨스에서 공유되어서 car2에서 이 클래스변수가 바뀌면 car1에도 반영됨.  
        
    def __str__(self):  # 사용자가 정보를 확인하기 위해서 프린트해줄때 근데 사실 __str__, __repr 다 정보를 프린트 큰 차이는없음
        return 'str: :{} - {}'.format(self._company,self._details)
    
    def __repr__(self): # 개발자 입장에서 객체를 인식할수있는 정보까지 다 볼때는 요걸로(엄격한레벨로 프린트)
        return 'str: :{} - {}'.format(self._company,self._details)

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info {} {} ".format(self._company, self._details.get('price')))

car1 = Car('ferrari',{'color': 'white', 'horsepower': 470, 'price': 8000})
print(car1.car_count)
car2 = Car('bmw',{'color': 'blue', 'horsepower': 400, 'price': 9000})
print(car1.car_count)
car3 = Car('audi',{'color': 'red', 'horsepower': 340, 'price': 6000})
print(car1.car_count)

print(dir(car1)) # 클래스 변수까지 다 나옴. 
# 클래스 변수에는 _언더바를 안쓰고 인스턴스의 변수에는 _를 보통 붙여서 클래스변수와 구별함 (_company 와 car_count처럼)

# 인스턴스 네임스페이스에 없으면 상위에서 검색 -> 동일한 이름으로 변수 생성 가능(우선 인스턴스 검색 후-> 클래스 변수 검색)
# 인스턴스에서 변수(그 값)를 불러올때 인스턴스의 변수 먼저-> 없으면 그 담에 클래스 변수에서 검색함
car1.car_count  # self.car_count로 인스턴스 변수를 지정해줬다면 이 인스턴스변수값이 호출됨.(우선임)




 