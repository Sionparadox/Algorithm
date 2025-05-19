import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

arr = []
while True:
    line = input()
    if not line:
        break
    arr.append(int(line.strip()))

def postorder(start, end):
    if start > end: return
    
    root = arr[start]
    idx = start+1
    while idx <= end and arr[idx] < root:
        idx += 1
    
    postorder(start+1, idx-1)
    postorder(idx, end)
    print(root)

postorder(0, len(arr)-1)