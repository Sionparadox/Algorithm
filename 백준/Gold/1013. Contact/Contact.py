import sys
import re
input = sys.stdin.readline

regex = r'(100+1+|01)+'
p = re.compile(regex)
N = int(input())
for _ in range(N):
    _input = input().rstrip()
    if p.fullmatch(_input):
        print('YES')
    else :
        print('NO')