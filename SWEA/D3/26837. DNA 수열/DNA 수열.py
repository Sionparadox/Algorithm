from collections import Counter
TC = int(input())
for _ in range(TC):
    N, S = input().split()
    N = int(N)
    AT = CG = 0
    counter = Counter()
    counter[(0, 0)] = 1
    answer = 0
    
    for ch in S:
        if ch == 'A':
            AT += 1
        elif ch == 'T':
            AT -= 1
        elif ch == 'C':
            CG += 1
        else:
            CG -= 1
        
        answer += counter[(AT, CG)]
        counter[(AT, CG)] += 1
    
    print(answer)