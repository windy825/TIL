for idx in range(int(input())):
    n = int(input())
    case = [[0]*n for _ in range(n)]
    cnt, x, y, adding = 0, 0, -1, 1
 
    while n>0:
        for _ in range(n):
            cnt +=1
            y +=adding
            case[x][y] = cnt
        n-=1
        for _ in range(n):
            cnt +=1
            x +=adding
            case[x][y] = cnt
        adding = -adding
 
    print(f'#{idx+1}')
    for line in case:
        print(*line)