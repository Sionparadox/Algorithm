from sys import stdin
input = stdin.readline
N = int(input())
a,b,c = map(int, input().split())

prevMin = [a,b,c]
prevMax = [a,b,c]

for _ in range(N-1): 
    l,c,r = map(int, input().split())
    currMin = [min(prevMin[0],prevMin[1]) + l,
    min(prevMin[0],prevMin[1],prevMin[2]) + c,
    min(prevMin[1],prevMin[2])+ r]
    
    currMax = [max(prevMax[0],prevMax[1]) + l,
    max(prevMax[0],prevMax[1],prevMax[2]) + c,
    max(prevMax[1],prevMax[2])+ r]
    
    prevMin = currMin
    prevMax = currMax


print(max(prevMax), min(prevMin))