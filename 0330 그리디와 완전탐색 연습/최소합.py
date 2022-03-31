direction = [(1,0), (0,1)]

def check(now, total):
    global minn
    
    if now == (n-1, n-1):
        minn = min(minn, total)
    if total > minn:
        return

    for da,db in direction:
        nowa, nowb = now[0], now[1]
        newa, newb = nowa + da, nowb + db
        if 0 <= newa < n and 0 <= newb < n and not visited[newa][newb]:
            visited[newa][newb] = 1
            check((newa,newb), total + case[newa][newb])
            visited[newa][newb] = 0
    

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n)]
    minn = n*n*10

    visited = [[0] * n for _ in range(n)]
    check((0,0), case[0][0])

    print(f'#{tc} {minn}')