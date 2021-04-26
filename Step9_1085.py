#x,y위치에서 가장 가까운 경계선은 위(h), 아래(0), 오른쪽(w), 왼쪽(0)이다. x,y 위치에서의 4개의 거리 중 가장 짧은 것을 구하면 된다.

import sys
x, y, w, h = map(int,sys.stdin.readline().split())
print(min(h-y,w-x,x,y))