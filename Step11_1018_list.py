# Step_11 1018번 문제 체스판

# Array로 입력을 받아서 1 ~ 64 까지 W -> B or B -> W가 아닌 개수 파악

def check_chess(chess_8x8_list):

    #홀수 row
    chess_8x8_odd = chess_8x8_list[0::2]
    chess_8x8_even = chess_8x8_list[1::2]
    odd_str = ''.join(chess_8x8_odd)
    even_str = ''.join(chess_8x8_even)
    
    #Case 1 (W-->B)
    cnt_case1 = 0
    #홀수 column
    for i in range(0,len(odd_str),2):
        if odd_str[i] == 'B':
            cnt_case1 += 1
    for j in range(1,len(odd_str),2):
        if odd_str[j] == 'W':
            cnt_case1 += 1
    #짝수 column
    for i in range(0,len(even_str),2):
        if even_str[i] == 'W':
            cnt_case1 += 1
    for j in range(1,len(even_str),2):
        if even_str[j] == 'B':
            cnt_case1 += 1

    #Case 2 (B-->W)
    cnt_case2 = 0
    #홀수 column
    for i in range(0,len(odd_str),2):
        if odd_str[i] == 'W':
            cnt_case2 += 1
    for j in range(1,len(odd_str),2):
        if odd_str[j] == 'B':
            cnt_case2 += 1
    #짝수 column
    for i in range(0,len(even_str),2):
        if even_str[i] == 'B':
            cnt_case2 += 1
    for j in range(1,len(even_str),2):
        if even_str[j] == 'W':
            cnt_case2 += 1


    return(min(cnt_case1,cnt_case2))

row_qty, column_qty = map(int, input().split())
chess_list = [str(input()) for _ in range(row_qty)]
# print(chess_list)

#자르기 8x8

#행고정 후 오른쪽으로 한칸씩
chess_8x8_temp = []
result_list = []

for row in range(0,row_qty-7):
    for column in range(0,column_qty-7):
        for row_str in chess_list[row:row+8]:
            chess_8x8_temp.append(row_str[column:column+8])
        result_list.append(check_chess(chess_8x8_temp))
        chess_8x8_temp = []
print(min(result_list))

# print(check_chess(['BBBBBBWB', 'BBBBBBBW', 'BBBBBBWB', 'BBBBBBBW', 'BBBBBBWB', 'BBBBBBBW', 'WWWWWWWW', 'WWWWWWWW']))