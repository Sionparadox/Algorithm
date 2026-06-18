def merge(a1, a2):
    result = []
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1
    while i < len(a1):
        result.append(a1[i])
        i += 1
    while j < len(a2):
        result.append(a2[j])
        j += 1
    return result

def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    sorted_nums = merge_sort(nums)
    print(f'#{tc} {sorted_nums[N // 2]} {cnt}')
