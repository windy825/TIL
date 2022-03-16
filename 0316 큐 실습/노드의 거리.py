# 깊이를 나타내는 배열을 사용하여, 매 탐색마다 해당 깊이를 입력 후 넘어갑니다.
# 현재 위치에서 다음 노드를 탐색할때, 해당 탐색된 노드의 깊이는, 현재 깊이 +1 방식

t = int(input())
for tc in range(1, t+1):
    v, e = map(int,input().split())
    case, level = {n : [] for n in range(1,v+2)}, [0] * (v+1)

    for _ in range(e):     # 양뱡향 간선 이기에, 딕셔너리 에서 둘다 체크하며 경로 기입
        a,b = map(int,input().split())
        case[a].append(b)
        case[b].append(a)
    s, e = map(int,input().split())

    stack = [s]   # 출발위치를 넣은채 탐색
    while stack:
        now = stack.pop()   # dfs
        if now == e:
            break
        for next in case[now]:     # 딕셔너리 키에 현재 위치를 넣고, 값 중에 방문 안한 값을
            if not level[next]:    # 탐색할 노드로 선정
                level[next] = level[now] + 1
                stack.append(next)
    
    print(f'#{tc} {level[e]}')