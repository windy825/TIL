def qqqqqq(cnt, total):
    global minn
     
    if (n-cnt) + total >= minn:   # 남은 물건을 가장 싼 가격으로 하여도 
        return                    # 현재 최소값보다 크다면 가지치기
    if cnt == n:
        minn = min(minn, total)
 
    for i in range(n):
        if not visited[i]:   # 순열
            visited[i] = 1
            qqqqqq(cnt + 1, total + case[cnt][i])
            visited[i] = 0 
 
 
for tc in range(1, int(input())+1):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
 
    minn = 99 * n * n
    for i in range(n):  # 처음 선택하는 공장을 고른 후 탐색 시작 (윗 함수에 합쳐도 됩니다 사실)
        visited[i] = 1
        qqqqqq(1, case[0][i])
        visited[i] = 0
     
    print(f'#{tc} {minn}')