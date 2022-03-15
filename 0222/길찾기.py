for idx in range(1,11):
    tc, total = map(int, input().split())
    line = list(map(int,input().split()))
    WTF = [(line[i], line[i+1]) for i in range(0, len(line), 2)]
    stack, visited = [0], [0]*100
  
    while stack:
        now = stack.pop()
        visited[now] = 1
        if visited[99] ==1:
            break
        for x,y in WTF:
            if x == now and not visited[y]:
                stack.append(y)
      
    print(f'#{tc} {visited[99]}')