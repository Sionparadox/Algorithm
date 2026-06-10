TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]
    word_set = set(words)
    answer = 0
    base = 0
    for word in words:
        if word not in word_set:
            continue
        flipped = word[::-1]
        if word == flipped:
            base = M
        elif flipped in word_set:
            answer += M*2
            word_set.remove(flipped)
    print(f'#{tc} {base+answer}')