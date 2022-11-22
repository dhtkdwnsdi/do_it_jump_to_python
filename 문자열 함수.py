a = 'python is best choice'
# 문자열 개수 세기
print(a.count('p'))

# 위치 알려주기, 없으면 -1 반환
print(a.find('t'))
print(a.index('t'))
print(a.find('z)'))

# 문자열 삽입
print(','.join(a))

# 소문자를 대문자로 바꾸기 / 대문자를 소문자로 바꾸기
print(a.upper())
print(a.lower())

# 왼쪽 공백 지우기 / 오른쪽 공백 지우기 / 양쪽 공백 지우기
print(a.lstrip)
print(a.rstrip())
print(a.strip())

# 문자열 바꾸기
print(a.replace('python', 'java'))

# 문자열 나누기
print(a.split())
print(a.split('is'))

