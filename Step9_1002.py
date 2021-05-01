# 터렛 1002번
# 두 원이 만나지 않을 경우의 수
# 1. dist > r1+r2, 두 원이 멀리 떨어져 있을 때
# 2. dist + min(r1,r2) < max(r1,r2), 한 원이 다른 원 안에 있을 때
# 두 원의 접점 경우의 수
# 0. 두 중심점사이의 거리 dist = sqrt((x1-x2)**2+(y1-y2)**2)
# 1. x1 == x2 and y1 == y2, 두 원이 같을 경우 : 무한대
# 2. abs(r1-r2) == dist,두원의 접점이 1개일 때(내접)
# 3. dist < r1 + r2, 두 원의 접점이 2개 일 때
# 4. r1+r2 == dist,외접

import sys
import math
T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())

    dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if dist == 0 and r1 == r2:
        print(-1)
    elif dist == r1 + r2 or max(r1,r2) == min(r1,r2) + dist:
        print(1)
    elif dist > r1+r2 or max(r1,r2) > dist + min(r1,r2):
        print(0)
    else: print(2)