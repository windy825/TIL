t = int(input())
for tc in range(1, t+1):
    n = int(input())
    case = [list(map(int, input().split()))for _ in range(n)]
    case.sort(key= lambda x : x[1])

    next, cnt = case[0][1], 1
    for i in range(1,n):
        if next <= case[i][0]:
            cnt += 1
            next = case[i][1]
    
    print(f'#{tc} {cnt}')