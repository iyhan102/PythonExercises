######### Chapter02-03
# 클래스를 이용한 객체지향 프로그래밍 

class Car():
    """
    코멘트 달기 
    descripton: Class, Static, Instance method
    """
    # 클래스 변수 
    # price_per_raise = 1.0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):  # 사용자가 정보를 확인하기 위해서 프린트해줄때 근데 사실 __str__, __repr 다 정보를 프린트 큰 차이는없음
        return 'str: :{} - {}'.format(self._company,self._details)
    
    def __repr__(self): # 개발자 입장에서 객체를 인식할수있는 정보까지 다 볼때는 요걸로(엄격한레벨로 프린트)
        return 'str: :{} - {}'.format(self._company,self._details)
    
    # Instance (self로 받는 것(객체), 객체의 고유의 속성값을 사용)
    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info {} {} ".format(self._company, self._details.get('price')))

    # 메서드를 이용한 정보 불러오기 Instance method
    # instance method = instance, 즉 self를 받아서 수행하는 클래스에서 찍어내는 function)
    def get_price(self):
        return 'before car price -> company:{}, price: {}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'after car price -> company:{}, price: {}'.format(self._company, self._details.get('price')*Car.price_per_raise)
        #클래스 변수 Car.price_per_raise 상승률을 곱해주어 오른 후 가격 불러오기. 
        
    @classmethod # class method를 명시/표시하는 데코레이터 
    def raise_price(cls, per): #cls가 self역할. 여기선 Car안이니까 cls가 바로 Car라는 클래스 
        if per <= 1: 
            print('Please Enger 1 or more')
            return
        cls.price_per_raise = per
        print('Suceed! price increased.')
    
    @staticmethod
    def is_bmw(inst): # inst는 전달한 instance를 나타냄 self/cls의 의미 아님. 
        if inst._company =='bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry, This car is not BMW.'


car1 = Car('ferrari',{'color': 'white', 'horsepower': 470, 'price': 8000})
car2 = Car('bmw',{'color': 'blue', 'horsepower': 400, 'price': 9000})

# 가격정보 직접접근해서 불러오기
print(car1._details.get('price'))
print(car1._details['price'])
car1.detail_info()
# 위의 식으로, 어떤 정보를 불러올 때 인스턴스에서 직접 불러오는 것은 잘 안한(실수로 값이 변경될수도, 보안상 안될수도 여러가지 이유로)
# 그래서 보통 메서드로 원하는 정보를 하나 하나씩 불러오는 방법을 선택함. 

# 가격정보 
dir(car1)
car1.get_price() # 인상전
car1.get_price_culc() # 인상후 # self를 받는 거니까 ()아무것도 안해도 알아서 자기자신을 받아서 기능을 수행(function수행)

# 인상률 상승후 
Car.price_per_raise = 1.2 # 1.1-> 1.2
car1.get_price() # 인상전
car1.get_price_culc() # 인상후
# car1._details.get('price')*1.2
# 그러나 클래스 변수도 직접 접근해서 바꾸는 건 좋지 않음. method를 이용해 바꾸기 이럴 때 클래스method를 사용함 
# class method = self가 아니라 class를 받아서 수행하는 function

@classmethod # class method를 명시/표시하는 데코레이터 
def raise_price(cls, per): #cls가 바로 Car라는 클래스 
    if per <= 1: 
        print('Please Enger 1 or more')
        return
    cls.price_per_raise = per
    print('Suceed! price increased.')
    
    # -> 요걸 이제 class안에 instance methon와 같은 라인에 넣어주는 거지
    
# class method 사용  
Car.raise_price(1) 
Car.raise_price(1.2)
# static method는 specific한 파라미터를 받지않고(self나 cls를 안써줌) 쓰는 것임. 

# 이 차가 어떤 company에서 나온건지 확인하는 method를 만들자(static method 예)
# static method
@staticmethod
def is_bmw(inst): # inst는 받을 instance를 나타냄 self/cls의 의미 아님.
    # staticmethod는 어떤 instance 자체를 받아서 기능을 수행하게할때 쓰기 적합. 
    if inst._company =='bmw':
        return 'OK! This car is {}'.format(inst._company)
    return 'Sorry, This car is not BMW.'
 # -> 요걸 이제 class안에 instance method와 같은 라인에 넣어주는 거지

print(car1.is_bmw(car1)) # instance에서 staticmethod로 접근할때 staticmethod로 들어가는 instance를 지정해줘야하므로 car1을 써줌. 
print(car2.is_bmw(car2))
print(Car.is_bmw(car2)) #-> 이렇게 클래스에서 staticmethod로 접근해도 됨. 

