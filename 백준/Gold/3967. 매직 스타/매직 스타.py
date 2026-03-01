import sys
input = sys.stdin.readline

arr = []
for _ in range(5):
    for c in input().rstrip():
        if c == '.':
            continue
        if c == 'x':
            arr.append(0)
        else:
            arr.append(ord(c)-ord('A')+1)

lines = [(0,2,5,7), (0,3,6,10), (1,2,3,4), (1,5,8,11), (4,6,9,11), (7,8,9,10)]
fixed = set()
visited = [False]*13
for i in range(12):
    if arr[i] > 0:
        visited[arr[i]] = True
        fixed.add(i)

def can_magic():
    for a,b,c,d in lines:
        if arr[a]+arr[b]+arr[c]+arr[d] != 26:
            return False
    return True

def backTrack(idx):
    if idx in fixed:
        backTrack(idx+1)
        return
    
    if idx == 12:
        if can_magic():
            chars = [chr(x + ord('A') - 1) for x in arr]
            print("....{}....\n.{}.{}.{}.{}.\n..{}...{}..\n.{}.{}.{}.{}.\n....{}....".format(*chars))
            exit(0)
        return
    
    for i in range(1, 13):
        if visited[i]:
            continue
        visited[i] = True
        arr[idx] = i
        backTrack(idx+1)
        arr[idx] = 0
        visited[i] = False
    
backTrack(0)
    