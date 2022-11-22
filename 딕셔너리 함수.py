dic = {'name' :'pey', 'phone':'01099993333', 'age':29} #d.keys() 는 d의 key만 모아서 dict_keys라는 객체를 리턴함
# Key 리스트 만들기
print(dic.keys())

# Value 리스트 만들기
print(dic.values())

# Key, Values 쌍으로 얻기
print(dic.items())

# Key, Values 쌍 모두 지우기
print(dic.clear())

# 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하는 함수 get()
print(dic.get('abc', 'def'))

# 해당 key가 딕셔너리 안에 있는지 조사하기
dic = {'name' :'pey', 'phone':'01099993333', 'age':29}
print('name' in dic)
print('nickName' in dic)