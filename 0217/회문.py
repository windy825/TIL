for idx in range(1,int(input())+1):
    n,m = map(int,input().split())
    case = [input() for _ in range(n)]
    case2 = list(map(''.join,zip(*case)))

    for i in range(n):
        for j in range(n-m+1):
            if case[i][j:j+m] == case[i][j:j+m][::-1]:
                print(f'#{idx} {case[i][j:j+m]}')                
                break
            
            elif case2[i][j:j+m] == case2[i][j:j+m][::-1]:
                print(f'#{idx} {case2[i][j:j+m]}')                
                break