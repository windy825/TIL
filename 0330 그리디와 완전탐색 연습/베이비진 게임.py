def run_check(arr):
    global flag
    cnt = 1
    temp = sorted(list(set(arr)))
    for j in range(1, len(temp)):
        cnt = cnt + 1 if temp[j] - temp[j-1] == 1 else 1
        if cnt ==3:
            return 1
    return 0


for tc in range(1, int(input())+1):
    player1, player2, flag = [], [], 0
    line = list(map(int, input().split()))
    
    for i in range(12):
        if flag:
            break
        if i % 2:
            player2.append(line[i])
            player2.sort()
            cnt = 1
            for j in range(1, len(player2)):
                cnt = cnt + 1 if player2[j-1] == player2[j] else 1
                if cnt >= 3 or run_check(player2):
                    flag = 2
                    break
        else:
            player1.append(line[i])
            player1.sort()
            cnt2 = 1
            for j in range(1, len(player1)):
                cnt2 = cnt2 + 1 if player1[j-1] == player1[j] else 1
                if cnt2 >= 3 or run_check(player1):
                    flag = 1
                    break

    print(f'#{tc} {flag}')