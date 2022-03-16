direction = [(-1,0), (0,-1), (1,0), (0,1)]  # 4방향 탐색
 
for _ in range(10):
    tc = int(input())
    case = [list(map(int, list(input()) )) for _ in range(16)]  # 미로를 받아줍니다.
    answer = 0
 
    stack = [(1,1)]   # 출발 위치를 넣고 시작
    while stack:
        if (13,13) in set(stack):   # 다음 갈수 있는 후보들 중에 도착지점이 있으면 탐색 완료
            answer = 1
            break
         
        nowa,nowb = stack.pop(0)
        case[nowa][nowb] = 1
        for da,db in direction:     # 4 방향을 탐색하면서, 후보를 찾습니다. 
            newa = nowa + da
            newb = nowb + db
            if case[newa][newb] in {0,3}:  # 비어있거나, 목적지인 3이라면 후보에 포함
                stack.append((newa,newb))
     
    print(f'#{tc} {answer}')  # 만약 모두 탐색해도 갈 수 없다면 처음에 할당된 0 반환