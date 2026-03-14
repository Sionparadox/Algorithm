import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = 0
    answer = 0
    for i in range(N-1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            answer += max_price-price[i]
    
    print(answer)

'''
뒤에서부터 최댓값 갱신하며 탐색
'''