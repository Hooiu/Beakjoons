# 블랙잭 문제 (3개의 숫자를 골라서 어떤 값에 가장 가까운 수 찾기)
# N = 숫자 개수
# M = 목표 값
# 숫자 = []

# 숫자 개수는 최대 100개
# 3개의 숫자를 뽑는 경우의 수는 100*99*98 = 약 100만개
# 하나씩 모두 비교하는 것도 그렇게 오래 걸리진 않을 듯

import sys

N, M = map(int,sys.stdin.readline().split())
no_list = list(map(int,sys.stdin.readline().split()))

from itertools import permutations
all_cases = list(permutations(no_list,3))
result = 0

for case in all_cases:
    if sum(case) == M:
        result = sum(case)
        break
    else:
        if M < sum(case):
            continue
        else:
            if abs(M - result) > abs(M - sum(case)):
                # print(result)
                result = sum(case)
# print(all_cases)
print(result)
