N = int(input())
for i in range(N):
    ox_str = input()
    o_arr = ox_str.split('X')
    o_num = []
    cnt = 0
    for j in range(len(o_arr)):
        o_num.append(len(o_arr[j]))
    for j in o_num:
        while (j>0):
            cnt += j
            j -= 1
    print(cnt)