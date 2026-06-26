dots = {'.', '!', '?'}
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    cnt = 0
    answer = [0]*N
    while True:
        line = input().split()
        for word in line:
            if word[0].isupper():
                if len(word) == 1:
                    answer[cnt] += 1  
                elif word[1:].islower():
                    if word[-1] in dots and word[1:-1].isalpha():
                        answer[cnt] += 1
                    elif word[1:].isalpha():
                        answer[cnt] += 1
                    
            if word[-1] in dots:
                cnt += 1
        if cnt == N:
            break
    print(f'#{tc}', *answer)