TC = int(input())
for tc in range(1, TC+1):
    S = input()
    E = input()
    while len(S)<len(E):
        if E[-1] == 'X':
            E = E[:-1]
        else:
            E = E[:-1][::-1]
    
    print(f"#{tc} {'Yes' if S == E else 'No'}")