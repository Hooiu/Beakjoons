#백준 수학2 No.4153 직각삼각형인지 확인
#피타고라스의 정리 이용. 주의 사항은 가장 긴 변이 맨 마지막에 주어진다고 하지 않았음.

import sys

while True:
    N = list(map(int,sys.stdin.readline().split()))
    N.sort()
    if sum(N) == 0:
        break
    elif N[2]**2 == N[0]**2+N[1]**2:
        print('right')
    else:
        print('wrong')