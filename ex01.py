# 클래스 및 메소드 

# 일반적인 코딩. 너무 코드가 길어짐. 
car_company_1 = 'ferrari'
car_detail_1 = [
    {'color': 'white'},
    {'horsepower': 400},
    {'price': 8000}
             ]

car_company_2 = 'volvo'
car_detail_2 = [
    {'color': 'red'},
    {'horsepower': 300},
    {'price': 6000}
             ]

# list 구조
# index 접근 실수. 삭제 불편. 관리 불편 
car_company_list = ['ferrari','bmw', 'volvo']
car_detail_list = [
    {'color': 'white','horsepower': 400,'price': 8000},
    {'color': 'red','horsepower': 500,'price': 6300},
    {'color': 'yellow','horsepower': 300,'price': 7700}
]

del car_company_list[1]
del car_detail_list[1]

car_company_list
car_detail_list

# 딕셔너리 구조
# 중첩문제(키 이름이 같으면 중첩됨) 키 조회 예외처리 
car_dict = [
    {'car_company': 'ferrari', 'car_detail' : {'color': 'white','horsepower': 400,'price': 8000}} ,
    {'car_company': 'bmw', 'car_detail' : {'color': 'red','horsepower': 507,'price': 7000}} ,
    {'car_company': 'volvo', 'car_detail' : {'color': 'yellow','horsepower': 600,'price': 6000}}
]

print(car_dict)

del car_dict[1]

car_dict.pop(0) # pop(지울 키 index)

print(car_dict)

# 클래스 구조 
class Car(): # 괄호는 있어도 되고 없어도 되고 
    def __init__(self,company, details):
        self._company = company
        self._details = details 
        
    def __str__(self):
        return 'str :{}-{}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
car1 = Car('ferrari',  {'color': 'white','horsepower': 400,'price': 8000}) 



