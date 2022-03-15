def check(case):    
    where_r_u = [(1,0), (-1,0), (0,1), (0,-1)]   # 움직일 4 방향들 설정 
    stack = [start]
 
    while stack:
        a,b = stack.pop()
        case[a][b] = '1'          # 방문했으면 다시 안가도록 '1' (벽) 표시
        for xx, yy in where_r_u:  # 주위 4방향 탐색하면서 '1' (벽) 아니면 다 가능하다고 판단하여 스택에 추가
            newa, newb = a+xx, b+yy
            if 0<= newa <n and 0<= newb <n and case[newa][newb] !='1':
                stack.append((newa, newb))
                if (newa, newb) == end:  # 만약 가능한 방향 중에 도착방향이 있다면 더 탐색 안하고 중단
                    return 1
    return 0
 
for tc in range(1, int(input())+1):
    n = int(input())
    case = [list(input()) for _ in range(n)]
 
    start, end = (0,0), (0,0)
    for i in range(n):           # 시작, 도착 위치를 찾기위한 코드
        for j in range(n):
            start = (i,j) if case[i][j]=='2' else start
            end = (i,j) if case[i][j]=='3' else end
     
    print(f'#{tc} {check(case)}')