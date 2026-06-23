TC = int(input())
for _ in range(TC):
    S = input()
    L = len(S)

    left, right = 0, L-1
    answer = 0
    while left<right:
        if S[left] == S[right]:
            left += 1
            right -= 1
        elif S[left] == 'x':
            left += 1
            answer += 1
        elif S[right] == 'x':
            right -= 1
            answer += 1
        else:
            answer = -1
            break
    print(answer)