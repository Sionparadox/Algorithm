TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    words = set()
    for _ in range(N):
        words.add(input())
    answer = sorted(words, key=lambda x:(len(x), x))
    print('#%d'%tc)
    print('\n'.join(answer))