import sys
input = sys.stdin.readline

N = int(input())
shortcuts = set()
for _ in range(N):
    str = input().strip()
    words = str.split(' ')
    flag = False
    for i in range(len(words)):
        word = words[i]
        if word[0].lower() not in shortcuts:
            shortcuts.add(word[0].lower())
            words[i] = f'[{word[0]}]{word[1:]}'
            flag = True
            break
    if not flag:
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                if word[j].lower() not in shortcuts:
                    shortcuts.add(word[j].lower())
                    words[i] = f'{word[:j]}[{word[j]}]{word[j+1:]}'
                    flag = True
                    break
            if flag:
                break
    print(' '.join(words))
        