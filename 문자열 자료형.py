a = 'Hello world'
b = "Python"
c = """Life is too short."""
d = '''We need python.'''

# 문자열 안에 작은따옴표 포함시키기
e = "python's"
f = '"Python is Easy."'
g = 'Jun\'s Book'
h = '"Python Let\'s Go"'
# 연속된 작은/큰 따옴표를 이용해 단락 저장
i = """
    꽃이 지는 걸 보니 가을이 좋아
    낙엽이 지는 걸 보니 봄이 좋아
    """
print(h)
print(i)

# 문자열 연산하기
## 문자열 더해서 연결하기, 문자열 곱하기
print(a*2)

# 문자열 인덱싱과 슬라이싱
## 문자열 인덱싱
print(e[3])
print(e[-3])
print(e[2:7])
## 문자열 e[시작 번호:끝 번호]에서 끝 번호를 생략하면 시작번호부터 그 문자열의 끝까지 뽑는다.
print(e[2:])
print(e[:5])
print(e[:])
print(e[5:-1])
