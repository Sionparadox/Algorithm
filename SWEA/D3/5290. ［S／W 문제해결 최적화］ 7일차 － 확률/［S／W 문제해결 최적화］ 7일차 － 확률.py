T = int(input())
nines = [1]
for i in range(9):
    nines.append(nines[-1]*(9-i))

for t in range(1, T+1):
    N = int(input())
    if N == 1:
        print(f'#{t} 1.00000')
        continue
    if N >10:
        print(f'#{t} 0.00000')
        continue
    
    M = 9*10**(N-1)
    C = 9*nines[N-1]
    print(f'#{t} {C/M:.5f}')