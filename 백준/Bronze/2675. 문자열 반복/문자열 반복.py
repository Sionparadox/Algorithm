T = int(input())
for k in range(T):
    S_str = input()
    N,S = S_str.split(" ")
    ans = ''
    for i in range(len(S)):
        for j in range(int(N)):
            ans += S[i]
    print(ans)