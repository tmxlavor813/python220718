#function1.py
#함수 정의
def times(a,b):
    return a+b, a*b

#함수 호출
result = times(3,4)
print(result)

#함수 정의
def setValue(newValue):
    x = newValue
    print("함수 내부:", x)

#호출
result = setValue(5)
print(result)

#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수로 리스트를 초기화
    reuslt = []

    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
        return result
print(intersect("HAM","SPAM"))