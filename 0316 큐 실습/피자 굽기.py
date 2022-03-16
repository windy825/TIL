t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    line = [[x,cheese] for x, cheese in enumerate(list(map(int, input().split())),start=1)]
                                                    # [피자번호, 치즈양] 으로 저장
    case, wait = line[:n], line[n:]     # 화덕에 크기만큼 나눠서 시작합니다. 
                                        # 오른쪽이 예비 피자
    while len(case) != 1:    # 1개가 남을때 까지
        case[0][1] //=2      # 첫 피자의 치즈양을 확인 (//2 연산 후 확인하기)
        if not case[0][1]:   # 치즈가 0이라면
            if wait:            # 만약 예비피자가 있다면 교체 후 회전하기
                case[0] = wait.pop(0)
                case.append(case.pop(0))
            else:               # 없다면 그자리의 피자를 빼고, 회전은 안합니다.
                case.pop(0)
     
    print(f'#{tc} {case[0][0]}')