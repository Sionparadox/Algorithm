def solution(n, lost, reserve):
    answer = 0
    arr = [1] * (n+1)
    for i in lost:
        arr[i] -= 1
    for i in reserve:
        arr[i] += 1
    
    for i in range(1,n+1):
        if(arr[i] == 0):
            if(arr[i-1] == 2):
                arr[i-1] = 1
                arr[i] = 1
            elif(i<n and arr[i+1] == 2):
                arr[i+1] = 1
                arr[i] = 1
        if(arr[i] > 0):
            answer += 1
    
    return answer

