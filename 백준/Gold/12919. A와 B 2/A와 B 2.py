import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

S = input().strip()
T = input().strip()

def find(str):
    if str == S:
        print(1)
        exit(0)
    if len(str) <= len(S):
        return;
    
    if str[-1] == 'A':
        find(str[:-1])
    if str[0] == 'B':
        find(str[:0:-1])
find(T)
print(0)
    