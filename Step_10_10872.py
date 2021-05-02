#백준 단계10 재귀함수 - 팩토리얼
#팩토리얼을 재귀 함수로 --> 0과 1일 함수에 들어갈 때만 주의할 것!
#0!은 0이 아닌 1이다!!

n = int(input())

def factorial(n):
    if n == 1:
        return(1)
    elif n == 0:
        return(1)
    else:
        return(factorial(n-1)*n)

print(factorial(n))
    