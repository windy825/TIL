for idx in range(int(input())):
    k,n,_ = map(int,input().split())
    line = [0]*n
    for i in input().split():
        line[int(i)] +=1
    now, chrg = 0, 0
    while now + k < n:
        for i in range(k,0,-1):
            if line[now+i]:
                chrg +=1
                now +=i
                break
        else:
            chrg = 0
            break
    print(f'#{idx+1} {chrg}')