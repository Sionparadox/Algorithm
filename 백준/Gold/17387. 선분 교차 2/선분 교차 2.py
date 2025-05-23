import sys
input = sys.stdin.readline
EPS = 1e-9 

A = list(map(int, input().split()))
B = list(map(int, input().split()))
if A[0] > A[2]:
    A = A[2:]+A[:2]
elif A[0] == A[2] and A[1] > A[3]:
    A[1],A[3] = A[3], A[1]
if B[0] > B[2]:
    B = B[2:]+B[:2]
elif B[0] == B[2] and B[1] > B[3]:
    B[1],B[3] = B[3], B[1]


def normalize(line, pos, newX):
    if line[0] == line[2] : 
        return line[pos*2+1]
    d = (line[3]-line[1])/(line[2]-line[0])
    return d*(newX-line[pos*2])+line[pos*2+1]

def isCross(A, B):
    if A[2]<B[0] or B[2]<A[0]:
        return False
    if A[0]<B[0]:
        newY = normalize(A, 0, B[0])
        A[0] = B[0]
        A[1] = newY
    elif A[0]>B[0]:
        newY = normalize(B, 0, A[0])
        B[0] = A[0]
        B[1] = newY
    
    if A[2]<B[2]:
        newY = normalize(B, 1, A[2])
        B[2] = A[2]
        B[3] = newY
    elif A[2]>B[2]:
        newY = normalize(A, 1, B[2])
        A[2] = B[2]
        A[3] = newY

    if abs(A[1] - B[1]) < EPS or abs(A[3] - B[3]) < EPS:
        return True
    
    if A[0] == A[2]:
        if B[1] <= A[1] <= B[3] or A[1] <= B[1] <= A[3]:
            return True
        else :
            return False
    
    if (A[1] < B[1] and A[3] > B[3]) or (A[1] > B[1] and A[3] < B[3]):
        return True

    return False
     
print(1 if isCross(A, B) else 0)