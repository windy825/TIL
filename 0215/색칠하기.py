for idx in range(1, int(input())+1):
    case = [[0]*10 for _ in range(10)]

    for i in range(int(input())):
        a,b,aa,bb,color = map(int,input().split())
        for x in range(a,aa+1):
            for y in range(b,bb+1):
                case[x][y] +=color
    cnt = 0
    for x in range(10):
        for y in range(10):
            if case[x][y]==3:
                cnt +=1

    print(f'#{idx} {cnt}')