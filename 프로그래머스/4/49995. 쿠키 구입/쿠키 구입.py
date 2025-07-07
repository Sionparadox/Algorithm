def solution(cookie):
    L = len(cookie)
    prefix = [0]*(L+1)
    for i in range(L):
        prefix[i+1] = prefix[i]+cookie[i]
    
    answer = 0
    for k in range(L-1):
        l = k
        r = k+1
        while l>=0 and r<L:
            left = prefix[k+1] - prefix[l]
            right = prefix[r+1] - prefix[k+1]
            if left == right:
                answer = max(answer, right)
                l -= 1
                r += 1
            elif left < right:
                l -= 1
            else :
                r += 1
    
    return answer