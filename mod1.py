def sum(a,b):
    return a + b

def safe_sum(a,b):
    if type(a) != type(b) :
        print('더할수 있는 것이 아닙니다.')
        return
    else:
        result = sum(a, b)
        return result


# if __name__ == "__main__" :  > mod1.py에서 직접 실행시키는 것 아니면 실행 안됨(import 된 파이썬 파일에서 실행안됨)
if __name__ == "__main__" :
    print(safe_sum('a', 1))
    print(safe_sum(10, 1))
    print(sum(7, 1))
