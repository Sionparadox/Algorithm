S = input()

for i in range(ord('a'),ord('z')+1):
    key = S.find(chr(i))
    print(key,end=" ")