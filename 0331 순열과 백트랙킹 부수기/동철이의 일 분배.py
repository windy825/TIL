def work(cnt, total):
    global maxx
 
    if total <= maxx:  # 가지치기 
        return
    if cnt >= n:
        maxx = max(maxx, total)
    else:
        for i in range(n):
            if not visited[i]:   # 순열처럼 모든 경우를 따지기 위해서
                visited[i] = 1
                work(cnt + 1, total * case[cnt][i])
                visited[i] = 0
 
 
for tc in range(1, int(input())+1):
    n = int(input())
    case = [list(map(lambda x : int(x)*.01, input().split())) for _ in range(n)]
                                # 입력받을때, /100을 처리해서 받기
    maxx = 0
    visited = [0] * n
    for i in range(n):
        if case[0][i]:
            visited[i] = 1
            work(1, case[0][i])
            visited[i] = 0
     
    print(f'#{tc} {maxx * 100:.6f}')