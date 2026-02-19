import sys
input = sys.stdin.readline

W,H,f,c,x1,y1,x2,y2 = map(int, input().split())

cells = W*H
xf = min(f, W-f)

h = y2-y1
w = x2-x1
if xf>x1:
    w += min(xf,x2)-x1
answer = cells-w*h*(c+1)
print(answer)
    


'''
2f>W라면 접히지 않는 부분과 접힌 부분의 경계 : W-f
'''
