def solution(n, times):
    answer = 0
    s = 0
    e = max(times)*n//len(times)
    while s<=e:
        mid = (s+e)//2
        people = sum(mid//t for t in times)
        
        if people >= n:
            answer = mid
            e=mid-1
        else :
            s = mid+1
    return answer
