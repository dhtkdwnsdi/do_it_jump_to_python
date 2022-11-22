# if :
# elif :
# else :

# 비교연산자
# x<y, x>y, x==y, x!=y, x>=y, x<=y
# 논리연산자
# x or y, x and y, not x

# in 연산자
# x in 리스트, x not in 리스트
# x in 튜플, x not in 튜플
# x in 문자열, x not in 문자열0

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket :
    pass
else :
    print('카드를 꺼내라')

# elif 사용
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket :
    print('택시를 타고 가라')
elif card :
    print('카드가 있으니 택시를 타고 가라')
else :
    print('카드를 꺼내라')


# if문을 한 줄로 표현하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket : pass
else : print('카드를 꺼내라')