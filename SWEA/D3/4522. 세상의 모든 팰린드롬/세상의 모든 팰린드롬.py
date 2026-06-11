TC = int(input())
for tc in range(1, TC+1):
    word = input()
    L = len(word)
    flag = True
    for i in range(L//2):
        if word[i] == word[L-i-1]:
            continue
        if word[i] == '?' or word[L-i-1] == '?':
            continue
        flag = False
        break
    print(f"#{tc} {'Exist' if flag else 'Not exist'}")