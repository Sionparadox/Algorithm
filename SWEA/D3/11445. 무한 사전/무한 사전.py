TC = int(input())
for tc in range(1, TC+1):
    A = input().strip()
    B = input().strip()
    print(f"#{tc} {'N' if A+'a' == B else 'Y'}")