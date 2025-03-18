import sys
input = sys.stdin.read
data = input().strip().split('\n')

T = int(data[0])

for t in range(T):
    k, n = map(int, data[t*5+1].split())
    weight = [list(map(int, data[t*5+2+i].split())) for i in range(4)]
    group1 = []
    group2 = []
    for i in range(n):
        for j in range(n):
            group1.append(weight[0][i] + weight[1][j])
            group2.append(weight[2][i] + weight[3][j])
    
    group1.sort()
    group2.sort()
    
    canoe = float('inf')
    for v in group1 :
        s = 0
        e = n * n - 1
        value = k-v
        while (s <= e):
            mid = (s + e) // 2
            if (group2[mid] < value):
                s = mid + 1
            elif (group2[mid] > value):
                e = mid - 1
            else :
                canoe = k
                break
        
        if (s < n * n):
            sum1 = v + group2[s]
            if(abs(sum1 - k) < abs(canoe - k) or (abs(sum1 - k) == abs(canoe - k) and sum1 < canoe)):
                canoe = sum1
        
        if (e >= 0):
            sum2 = v + group2[e]
            if(abs(sum2 - k) < abs(canoe - k) or (abs(sum2 - k) == abs(canoe - k) and sum2 < canoe)):
                canoe = sum2
    
    print(canoe)