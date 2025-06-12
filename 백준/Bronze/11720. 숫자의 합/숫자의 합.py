N = int(input())
num = int(input())
sum = 0
for i in range(N):
    sum += num % 10
    num = num // 10
print(sum)