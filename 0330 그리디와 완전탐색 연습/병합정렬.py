def merge(s, e):
    global cnt
    
    if s >= e:
        return [line[s]]

    mid = (s+e+1) // 2
    left = merge(s, mid-1)
    right = merge(mid, e)

    result, i, j = [], 0, 0
    while i != len(left) and j != len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if i != len(left):
        result += left[i:]
        cnt += 1
    elif j != len(left):
        result += right[j:]

    return result


for tc in range(1, int(input())+1):
    n = int(input())
    line = list(map(int, input().split()))
    
    cnt = 0
    line = merge(0, n-1)
    print(f'#{tc} {line[n//2]} {cnt}')