def sorting(l, h):     # 메인
    if h <= l:
        return
    m = deviding(l, h)
    sorting(l, m-1)
    sorting(m, h)
 
 
def deviding(l, h):    # 피벗은 중심값을 기준으로 설정하기
    pivot = arr[(l + h) // 2]
    while l <= h:
        while arr[l] < pivot:
            l += 1
        while arr[h] > pivot:
            h -= 1
        if l <= h:
            arr[l], arr[h] = arr[h], arr[l]
            l, h = l + 1, h - 1
    return l
 
for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
 
    sorting(0, n-1)
    print(f'#{tc} {arr[n//2]}')