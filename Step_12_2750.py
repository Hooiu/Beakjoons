#오름차순 정렬
# 첫번째에 숫자 개수 N
# 중복 없음

import sys

N = int(input())
numbers = sorted([int(input()) for i in range(N)])

for number in numbers:
    print(number)
