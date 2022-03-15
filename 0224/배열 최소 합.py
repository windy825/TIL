def dfs(idx, summ):  
    global minn      

    if idx == n:               # 끝까지 탐색 다했으면, 조건에 맞는지 확인
        if summ < minn:        # 다 완료 후 최소인지 아닌지 확인
            minn = summ
        return

    if summ >= minn:  # 가지치기, 가망없으면 버리기
        return

    for i in range(n): 
        if check[i]:
            check[i] = False  # 재사용 못하게 막고, 하위 깊이 생성 및 탐색
            dfs(idx+1, summ + case[idx][i])
            check[i] = True   # 하위 깊이들을 다 탐색했으면 다시 돌아가기 위해 재사용 허가
 
for tc in range(1, int(input())+1):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n)]
    check, minn = [True] * n, 1000
 
    dfs(0,0)
    print(f'#{tc} {minn}')