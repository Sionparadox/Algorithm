TC = int(input())
for tc in range(1, TC+1):
    S = input()
    L = len(S)
    answer = 0
    curr = ''
    prev = ''
    for c in S:
        curr += c
        if curr != prev:
            answer += 1
            prev = curr
            curr = ''
    
    print(f'#{tc} {answer}')
