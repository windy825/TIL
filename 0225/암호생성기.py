def func(line):
    cnt = 0
    while True:
        move = 0
        for i in range(8):          # 8번을 돌면서 각 위치마다 알맞은 수(1~5) 를 계속 빼줍니다
            if cnt ==5:
                cnt = 0
            cnt +=1
            move +=1
            line[i] -= cnt
            if line[i] <= 0:       # 한번이라도 음수나 0이 나오게 되면 함수가 종료되고 몇번 이동했는지 반환합니다.
                line[i] =0
                return move
        
for tc in range(1,11):
    tc = input()
    line = list(map(int, input().split()))
    num = func(line)
    [line.append(line.pop(0)) for _ in range(num)]  # 반환된 이동횟수를 통해 배열을 회전시킵니다.

    print(f'#{tc}', *line)