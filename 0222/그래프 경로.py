for idx in range(1, int(input())+1):
    v, e = map(int, input().split())
    lines = [tuple(map(int, input().split())) for _ in range(e)]
    start, end = map(int, input().split())
    
    stack, visited = [start], [0]*(v+1)
    
    while stack:
        now = stack.pop()
        visited[now] = 1
        for x,y in lines:
            if x == now and not visited[y]:
                stack.append(y)
    
    print(f'#{idx} {visited[end]}')