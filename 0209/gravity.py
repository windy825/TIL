for idx in range(1, int(input())+1):
    n = int(input())
    line = list(map(int,input().split()))
    
    maxx = 0
    for i in range(n):
        me, cnt = line[i], n-i
        for j in line[i:]:
            if me <=j:
                cnt-=1
        if maxx <cnt:
            maxx =cnt
    
    print(f'#{idx} {maxx}')