#네번째 점 (수학2, 3009번 문제)
#세점이 주어지면 1) 축에 평행한 2) 직사각형이 되기 위한 4번째 점 출력
#입력은 x1 y1 \n x2 y2 \n x3 y3로 주어짐
#정사각형이 되기 위해선 두개의 x끼리 같고 / 두개의 y끼리 같아야 함

import sys
points = [list(map(int,sys.stdin.readline().split())) for i in range(3)]
result_x = points[2][0]

if points[0][0] == points[1][0]:
    result_x = points[2][0]
elif points[0][0] == points[2][0]:
    result_x = points[1][0]
else:
    result_x = points[0][0]

if points[0][1] == points[1][1]:
    result_y = points[2][1] 
elif points[0][1] == points[2][1]:
    result_y = points[1][1]
else:
    result_y = points[0][1]

print(result_x,result_y)