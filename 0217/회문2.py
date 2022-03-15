for idx in range(1, 11):
    input()
    case = [input() for _ in range(100)]
    case2 = list(map(''.join,zip(*case)))
    cnt, check = 100, False

    while True:
        for i in range(100):
            for j in range(100-cnt+1):
                if case[i][j:j+cnt] == case[i][j:j+cnt][::-1]:
                    check = True
                    break
                elif case2[i][j:j+cnt] == case2[i][j:j+cnt][::-1]:
                    check = True
                    break
        if check:
            print(f'#{idx} {cnt}')
            break
        cnt -=1