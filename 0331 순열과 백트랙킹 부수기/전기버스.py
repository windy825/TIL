def bus_937(now, k, cnt):
    global minn
     
    if minn <= cnt:
        return
    if now + k >= case[0]:  # 지금 위치에서 가진 충전량으로 목적지 도달가능한지 체크
        minn = min(minn, cnt)
        return
    for i in range(case[now], 0, -1):   # 그렇지 않다면, 가진 충전량으로 가능한 지점 방문
        bus_937(now + i, case[now + i], cnt + 1)
 
 
for tc in range(1, int(input())+1):
    case = list(map(int, input().split()))
    minn = case[0]
    bus_937(1, case[1], 0)   # 처음 시작은 1번 인덱스, 종점은 n번 인덱스
    print(f'#{tc} {minn}')