# Step_11 1018번 문제 체스판

# Array로 입력을 받아서 1 ~ 64 까지 W -> B or B -> W가 아닌 개수 파악

def check_chess(chess_8x8_list):

    case1_str = ''.join(['WBWBWBWBBWBWBWBW' for _ in range(8)])
    case2_str = ''.join(['BWBWBWBWWBWBWBWB' for _ in range(8)])
    chess_str = ''.join(chess_8x8_list)
    
    
    #Case 1 (W-->B)
    cnt_case1 = 0
    for i in range(64):
        if case1_str[i] != chess_str[i]:
            cnt_case1 += 1


    #Case 2 (B-->W)
    cnt_case2 = 0
    for j in range(64):
        if case2_str[j] != chess_str[j]:
            cnt_case2 += 1

    return(min(cnt_case1,cnt_case2))

row_qty, column_qty = map(int, input().split())
chess_list = [str(input()) for _ in range(row_qty)]

#자르기 8x8

chess_8x8_temp = []
result_list = []

for row in range(0,row_qty-7):
    for column in range(0,column_qty-7):
        for row_str in chess_list[row:row+8]:
            chess_8x8_temp.append(row_str[column:column+8])
        result_list.append(check_chess(chess_8x8_temp))
        chess_8x8_temp = []
print(min(result_list))
