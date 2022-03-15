for idx in range(1, int(input())+1):
    n = int(input())
    line = [0,1,0]
     
    print(f'#{idx}')
    for _ in range(n):
        print(*line[1:-1])
        line = [0]+[sum(line[i:i+2]) for i in range(len(line)-1)]+[0]