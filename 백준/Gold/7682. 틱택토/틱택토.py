import sys
input = sys.stdin.readline
lines = ['012', '345', '678', '036', '147', '258', '048', '246']

def isLine(shape):
    res = []
    for line in lines:
        idx = list(map(int, line))
        if all(game[x] == shape for x in idx):
            res.append(line)
    return res

def isValid(game):
    xc = game.count('X')
    oc = game.count('O')
    
    # X개수는 O와 같거나 하나 더 많아야함
    if xc != oc and xc != oc + 1:
        return False
        
    X = isLine('X')
    O = isLine('O')
    LX, LO = len(X), len(O)
    
    # 빙고가 만들어지지 않을 때
    if LX == 0 and LO == 0:
        # 끝까지 했으면 가능, 아니면 불가능
        return xc + oc == 9
        
    # 둘다 빙고가 되면 불가능
    if LX != 0 and LO !=0:
        return False
    
    
    if LX:
        if xc != oc + 1:
            return False
        if LX > 1:
            temp = set('012345678')
            for xline in X:
                temp &= set(xline)
            if len(temp) != 1:
                return False
        return True
    
    if LO:
        if xc != oc:
            return False
        if LO > 1:
            temp = set('012345678')
            for oline in O:
                temp &= set(oline)
            if len(temp) != 1:
                return False
        return True
    
    return False

while True:
    game = input().strip()
    if game == 'end':
        break
    print('valid' if isValid(game) else 'invalid')

