# 숫자 바로 대입하기
"I eat {0} apples".format(3)

# 문자열 바로 대입하기
"I eat {0} apples".format('five')

# 숫자 값을 가진 변수로 대입하기
number = 10
"I eat {0} apples".format(number)

#2개 이상의 값 넣기
number = 10
day = 'three'
"I ate {0} apples. so I was sick for {1} days".format(number, day)

# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number = 10, day=3)

# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

# 왼쪽 정렬
"{0:<10}".format("hi")

# 오른쪽 정렬
"{0:>10}".format("hi")

# 가운데 정렬
"{0:^10}".format("hi")

#공백채우기
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")
"{0:#>10}".format("hi")

#소수점 표현하지
y = 3.14159297
"{0:0.04f}".format(y)
"{0:10.4f}".format(y) # 자릿수를 10으로 맞추기

#'{' 또는 '}' 문자 표현하기
k = "{{and}}".format()
j = "{{python".format()
print(k)
print(j)