import sys
input = sys.stdin.readline

T = int(input())
 
def solve(pre_start, pre_end, in_start, in_end):
    if pre_start > pre_end or in_start > in_end:
        return 
    
    root = preorder[pre_start]
    idx = find_idx[root]
    left_size = idx-in_start
    # left
    solve(pre_start+1, pre_start+left_size, in_start, idx-1)
    # right
    solve(pre_start+left_size+1, pre_end, idx+1, in_end)
    #root
    answer.append(root)

for _ in range(T):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    find_idx = {}
    for i in range(N):
        find_idx[inorder[i]] = i
    answer = []
    solve(0, N-1, 0, N-1)
    print(' '.join(map(str, answer)))
    
'''
전위 순회 : root, left, right
중위 순회 : left, root, right
루트찾기 : 전위 순회는 루트가 항상 맨 앞임.
트리 나누기 : 찾은 루트를 기준으로 중위순회에서 왼쪽트리, 오른쪽 트리를 나눔
나눠진 트리에 대해 다시 루트를 찾음. 
반복

'''