for idx in range(1,11):
    input()
    case = [input().split() for _ in range(100)]
    minn = [0,10000]

    for start in range(100):
        if case[0][start] == '1':   # 스타트 지점을 찾습니다.
            pointer = start
            cnt = 0
            for row in range(100):
                if 0<start and case[row][start-1] =='1':           # 왼쪽 가능하면 왼쪽 가면서 카운트
                    while 0<start and case[row][start-1] =='1':
                        start -=1
                        cnt +=1
                elif start<99 and case[row][start+1] =='1':        # 오른쪽 가능하면 오른쪽 가면서 카운트
                    while start<99 and case[row][start+1] =='1':
                        start +=1
                        cnt +=1
                cnt+=1
            
            if cnt <= minn[1]:       # 매 경로가 끝날때 마다, 지금 가진 값보다 작다면 갱신
                minn = [pointer,cnt]
            
    print(f'#{idx} {minn[0]}')