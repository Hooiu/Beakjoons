# Step_11 1018번 문제 체스판

# Array로 입력을 받아서 1 ~ 64 까지 W -> B or B -> W가 아닌 개수 파악

import sys
import numpy as np

def check_chess(chess_8x8):
    # chess_list = chess_8x8.tolist()
    # chess_temp_list = []
    # for k in chess_list:
    #     chess_temp_list.append(''.join(k))
    # chess_str = ''.join(chess_temp_list)
    # print(chess_str)
    # Case 1 = 'W -> B
    cnt_case1 = 0
    #홀수 row
    for i in range(0,7,2):
        one_row = chess_8x8[i]
        #홀수 column
        for j in range(0,8,2):
            if one_row[j] == 'B':
                cnt_case1 += 1
        #짝수 Column
        for k in range(1,8,2):
            if one_row[k] == 'W':
                cnt_case1 += 1
    #짝수 row
    for i in range(1,8,2):
        one_row = chess_8x8[i]
        #홀수 column
        for j in range(0,8,2):
            if one_row[j] == 'W':
                cnt_case1 += 1
        #짝수 Column
        for k in range(1,8,2):
            if one_row[k] == 'B':
                cnt_case1 += 1
    
    # Case 2 = B -> W
    cnt_case2 = 0
    #홀수 row
    for i in range(0,8,2):
        one_row = chess_8x8[i]
        #홀수 column
        for j in range(0,8,2):
            if one_row[j] == 'W':
                cnt_case2 += 1
        #짝수 Column
        for k in range(1,8,2):
            if one_row[k] == 'B':
                cnt_case2 += 1                
    #짝수 row
    for i in range(1,8,2):
        one_row = chess_8x8[i]
        #홀수 column
        for j in range(0,8,2):
            if one_row[j] == 'B':
                cnt_case2 += 1
        #짝수 Column
        for k in range(1,8,2):
            if one_row[k] == 'W':
                cnt_case2 += 1

    return(min(cnt_case1,cnt_case2))

row_qty, column_qty = map(int, input().split())
chess_list = [list(map(str, input())) for _ in range(row_qty)]
chess_arr = np.array(chess_list)

chess_8x8 = []
result =[]

for row in range(row_qty-7):
    for column in range(column_qty-7):
        chess_8x8 = chess_arr[row:row+8,column:column+8]
        result.append(check_chess(chess_8x8))
        chess_8x8=[]
print(min(result))
