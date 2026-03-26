import sys
input = sys.stdin.readline


L, K, C = map(int, input().split())
arr = set(map(int, input().split()))
arr.add(0)
arr.add(L)
pos = sorted(list(arr))

min_value = 0
N = len(pos)

for i in range(N-1):
    min_value = max(min_value, pos[i+1]-pos[i])

def check(l):
    if l < min_value:
        return False, 0
    
    cnt = 0
    cut_pos = L
    for i in range(N-2, -1, -1):
      if cut_pos - pos[i] > l:
          cnt += 1
          cut_pos = pos[i+1]
    
    if cnt >C:
        return False, 0
    
    if cnt < C:
        return True, pos[1]
    else:
        return True, cut_pos    


left, right = 1, L
answer = float('inf')
cut = 0

while left<=right:
    mid = (left+right) // 2
    
    flag, p = check(mid)
    
    if flag:
        answer = mid
        cut = p
        right = mid-1
        
    else:
        left = mid+1

print(answer, cut)


'''
통나무를 한번 자르고 자른 조각들을 왼쪽에 붙여서 자르기 -> XX
주어진 위치는 통나무를 두고 그 위치에서만 칼질을 한다는 뜻
pos[i+1] - pos[i] : 간격 << 이 길이를 최소로 해야함
통나무 길이에 대해 이분탐색
해당 길이 이하로 자를 수 있는지 확인
-> 뒤에서부터 mid이하이며 최대 길이가 되도록 자름 (자르는 횟수를 최소화)

'''