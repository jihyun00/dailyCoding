"""
피보나치 알고리즘
내가 만든 모듈을 import할 수 있다는 걸 설명하기 위한 예제
"""
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end= ' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


"""
아래와 같이 사용시에 실행인자로 값을 하나 더 받는다.
ex) python test.py 234
"""
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
