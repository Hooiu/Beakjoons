#백준's Stage9 (기본수학) 9020번 골드바흐의 추측

# 자연수 2의 배수 N이 주어지며 4 ≤ n ≤ 10,000
# 두 소수의 합으로 N을 나타낼 수 있는 소수를 구하는 문제

# 문제풀이 아이디어
# 1. 10,000까지의 소수를 미리 구하고 (에라토스테네스의 체 이용)
# 2. 소수 중 작은 수를 A, 큰수를 B라고 하면 A+B = N
# 3. B를 N의 절반(N/2)부터 1까지 모든 수를 뒤져서 B와 A(N-A)가 모두 소수인 첫번째 쌍을 찾음

import time
import sys

start = time.time() # 시작시간


#에라토스테네스의 체
def isPrime(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    return(primes)
# 1. 소수 리스트를 먼저 만들자


prime_no_list = isPrime(10001)

#골든바흐의 추측 함수

def golden(N):
    k = int(N/2)
    for j in range(k,0,-1):
        if j in prime_no_list and N-j in prime_no_list:
            print(j, N-j)
            break

# 2. 소수의 합 반복

import sys
T=int(input())
N_list=[sys.stdin.readline().strip() for i in range(T)]
N_list = map(int,N_list)



for N in N_list:
  golden(N)


print('time :', time.time() - start)