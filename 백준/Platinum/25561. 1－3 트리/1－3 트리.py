import sys
input = sys.stdin.readline

T = int(input())

def solve():
    if arr[N-1] > 2:
        return False
    
    left = arr[0]
    for i in range(1, N):
        left -= 2*arr[i]
        if left<0:
            return False
        if arr[i] > arr[i-1]:
            return False
        
        left += arr[i]
    
    if N>1 and arr[-2]<2:
        return False
    return left == 2
    
        

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print("YES" if solve() else "NO")


'''
N의 합이 100만까지기 때문에 O(N)만 가능?
N번 노드는 1,2개밖에 안됨

역순으로 노드를 배치하며 남는 간선이 몇개인지 기록하며 가능 여부 판단 x
-> 남는 간선에 노드를 배치할 때 반복문 돌아야함 : 불가능
 
k번 노드는 k미만 노드와 2개 연결되어야함. (k==N일때 동일 노드 연결 가능 그 외 상위 노드와 연결)
1번 노드부터 2개씩 상위 노드에 연결.
연결 못한 노드는 개수 저장해둠.
이후 2번 노드를 연결 필요한 노드 수에 더하고 3에 대해 적용
최상위에서 4 2 혹은 3 1로 남으면 성공
-> left == 2

'''    
    