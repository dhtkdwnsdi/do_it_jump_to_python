# __init__ : 인스턴스를 만들 때 항상 실행된다.
# 인스턴스가 생성될 때 마다 실행되는 함수
# __init__ 함수에 self 말고 파라매타를 받는 경우 클래스를 생성 할 때 매개변수의 값을 세팅해야함

class Service:
    secret = "영구는 배꼽이 두 개다"
    def __init__(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print('%s님 %s + %s = %s입니다.' %(self.name, a,b,result))

pay = Service("홍길동")
pay.sum(1,2)