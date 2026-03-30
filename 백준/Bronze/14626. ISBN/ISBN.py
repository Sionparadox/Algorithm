import sys
input = sys.stdin.readline

N = input().strip()

tot = 0
missing = 1
for i in range(13):
    k = (i%2)*2+1
    if N[i] =='*':
        missing = k
        continue
    tot += int(N[i])*k

for x in range(10):
    if (tot+missing*x) % 10 == 0:
        print(x)
        break