class Service:
    secret = "영구는 배꼽이 두 개다"
    def sum(self, a, b):
        result = a + b
        print('%s + %s = %s입니다.' %(a,b,result))

pay = Service()
pay.sum(1,2)
# self는 호출 시 이용했던 인스턴스로 바뀐다.
# self라는 변수를 클래스 함수의 첫 번째 인수로 받아야하는 것은 파이썬만의 특징이다.
# 클래스 내 함수의 첫 번째 인수는 무조건 self로 사용해야 인스턴스의 함수로 사용할 수 있다.