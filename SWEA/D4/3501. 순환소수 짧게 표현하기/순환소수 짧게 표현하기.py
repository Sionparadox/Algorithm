TC = int(input())
for tc in range(1, TC+1):
    p, q = map(int, input().split())
    if p%q == 0:
        print(f'#{tc} {p//q}')
        continue
    quotient = p//q
    
    r = p%q
    remains = {}
    idx = 0
    res = []
    while r not in remains:
        remains[r] = idx
        p = r*10
        r = p%q
        res.append(p//q)
        idx += 1
    
    start = remains[r]
    repeated = ''
    if r != 0:
        repeated = '('+''.join(map(str, res[start:]))+')'
    print(f"#{tc} {quotient}.{''.join(map(str, res[:start]))}{repeated}")