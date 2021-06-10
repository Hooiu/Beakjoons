#Step 11 브루트포스 / 분해합

#무식하게 1부터 100만 까지의 분해합을 딕셔너리에 저장할 예정....

n = int(input())
no_dic = {}
for key_n in range(n):
    sum = 0
    for i in str(key_n):
        sum += int(i)
    no_dic[key_n] = key_n + sum

result = 0

for key, value in no_dic.items():
    if value == n:
        result = key
        break
    else:
        result = 0

print(result)

