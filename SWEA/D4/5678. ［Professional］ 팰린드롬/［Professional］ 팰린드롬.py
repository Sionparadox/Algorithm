def is_palindrome(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True

TC = int(input())
for tc in range(1, TC+1):
    S = input()
    N = len(S)
    answer = 0
    
    for length in range(N, 0, -1):
        for i in range(N-length+1):
            if is_palindrome(S[i:i+length]):
                answer = length
                break
        if answer:
            break
    
    print(f'#{tc} {answer}')