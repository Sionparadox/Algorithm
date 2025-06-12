N = int(input())

arr = [[0 for x in range(100)] for y in range(100)]
cnt = 0
for t in range(N):
    w, h = map(int, input().split())
    for i in range(h, h+10,1):
        for j in range(w, w+10,1):
            if(arr[i][j] != 1):
                arr[i][j] = 1
                cnt += 1

print(cnt)