TC = int(input())
for _ in range(TC):
    S = input()
    index = [-1]*10
    
    answer = 'yes'
    for i in range(len(S)):
        n = int(S[i])
        if index[n] == -1:
            index[n] = i
        elif i-index[n] == n+1:
            index[n] = -2
        else:
            answer = 'no'
            break
    for idx in index:
        if idx>=0:
            answer = 'no'
            break
    print(answer)