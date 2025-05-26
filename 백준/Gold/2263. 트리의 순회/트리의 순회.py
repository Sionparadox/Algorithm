import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorderIndex = {val:idx for idx, val in enumerate(inorder)}

answer = []
def searchRoot(inStart, inEnd, poStart, poEnd):
    if inStart > inEnd or poStart > poEnd:
        return
    root = postorder[poEnd]
    answer.append(root)
    
    rootIdx = inorderIndex[root]
    leftSize = rootIdx-inStart
    searchRoot(inStart, rootIdx-1, poStart, poStart+leftSize-1)
    searchRoot(rootIdx+1, inEnd, poStart+leftSize, poEnd-1)


searchRoot(0, N-1, 0, N-1)
print(' '.join(map(str, answer)))
'''
inorder : left root right
postorder : left right root
preorder : root left right

postorder의 끝은 root이므로 해당 루트 위치를 inorder에서 찾아서 left, right 서브트리로 나눔.
해당 서브트리들에 대해서 다시 위 과정을 반복(재귀)
'''