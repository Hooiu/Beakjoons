#브루트포스 - 덩치 (값 비교 후 순위 메기기)
# N = 사람 명수
# x,y = 사람의 몸무게와 키

import sys

N = int(input())
Weight_Height = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# 하나씩 잡아서 비교
result_rank = []

for values in Weight_Height:
    rank = 1
    for comp_values in Weight_Height:
        if values[0] < comp_values[0] and values[1] < comp_values[1]:
            rank += 1
    result_rank.append(rank)

for i in result_rank:

    print(i, end=' ')
