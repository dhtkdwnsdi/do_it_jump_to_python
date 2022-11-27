#set은 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
#set의 특징은 1. 중복을 허용하지 않는다. 2. 순서가 없다
#리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만, set은 그렇지 않다

s1 = set([1,2,3])
s2 = set("Hello")
print(s1)
print(s2)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

# 값 1개 추가하기
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가하기
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기
s1 = set([1,2,3])
s1.remove(2)
print(s1)