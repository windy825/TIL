t = int(input())
for tc in range(1, t+1):
    수량, 트럭수 = map(int, input().split())

    화물 = list(map(int, input().split()))
    트럭 = list(map(int, input().split()))

    화물.sort(reverse=True)
    트럭.sort(reverse=True)

    운반무게 = 0
    for i in range(트럭수):
        가능무게 = 트럭[i]
        while 화물:
            화물무게 = 화물.pop(0)
            if 가능무게 >= 화물무게:
                운반무게 += 화물무게
                break
    
    print(f'#{tc} {운반무게}')