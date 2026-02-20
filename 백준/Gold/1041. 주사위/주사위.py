import sys
input = sys.stdin.readline

N = int(input())
faces = list(map(int, input().split()))
if N==1:
    print(sum(faces)-max(faces))
    exit(0)
face1 = min(faces)
face2 = float('inf')
face3 = float('inf')

for i in [0, 5]:
    for j, k in ((1,2),(2,4),(4,3),(3,1)):
        face3 = min(face3, faces[i]+faces[j]+faces[k])

for i in range(5):
    for j in range(i+1, 6):
        if i+j != 5:
            face2 = min(face2, faces[i]+faces[j])

answer = face3*4
answer += face2 * (N*8-12)
answer += face1 * (5*(N**2) - 16*N + 12)
print(answer)

'''
한 면의 크기 : N^2
꼭지점부분, 모서리부분, 면부분으로 나뉨: 각각 보이는 면이 3,2,1

3면 보이는 주사위 : 4개
2면 보이는 주사위 : (N-1)*4 + (N-2)*4 = (2N-3)*4 = 8N-12
1면 보이는 주사위 : ((N-2)^2 + (N-2))*4 + (N-2)^2 = (N-2)(N-1)*4 + (N-2)(N-2) 
                    = 4N^2-12N+8 + N^2-4N+4  = 5N^2 - 16N + 12

3면일 때 나올 수 있는 값 : 8개
2면일 때 나올 수 있는 값 : 12개
1면일 때 나올 수 있는 값 : 6개
'''