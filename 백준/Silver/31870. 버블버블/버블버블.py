import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def bubbleSort(arr):
    res = 0
    for i in range(N):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                res += 1
    return res

prac1 = bubbleSort(A[:])
prac2 = bubbleSort(A[::-1])+1
print(min(prac1, prac2))
