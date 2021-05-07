#백준, Step10, 재귀함수, 별찍기, No.2447

# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.
# 배열로?? pattern을 하나 만들자
# 3 x 3 이고 [1][1] (한가운데)만 0

def pattern(k):
    zero_pattern = [[' '*3] for i in range(3**(k-1))]
    if k == 1:
        result1 = [['***'],
                   ['* *'],
                   ['***']]
        return result1
    else:
        result2 = [[pattern(k-1),pattern(k-1),pattern(k-1)],
                    [pattern(k-1),zero_pattern,pattern(k-1)],
                    [pattern(k-1),pattern(k-1),pattern(k-1)]]
        return result2

import numpy as np
print(np.array(pattern(2)))

# 출력 함수

# def print_star(array_star):
#     row = array_star
#     row_1 = []
#     for i in range(100):
#         if row[0] == '***' or row[0] == '* *' or row[0] == '   ':
#             row_1.append(row[0])
#             break
#         row = row[0]
        
#     return row_1


# import pandas as pd


# star = pattern(2)

# while i =='***' or i == '* *' or i == '   ':
    

# # print(star)
# # for i in star:
# #     print(i)

# # df = pd.DataFrame(star)
# # print(df)
# print(star)
# print(len(star))
# # print(print_star(star))



# # print(low_1)

# # for i in pattern:
# #     print(i[0],i[1],i[2])
