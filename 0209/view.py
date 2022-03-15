for idx in range(1,11):   
    long = int(input())
    city = list(map(int,input().split()))
    cnt = 0
    
    for i in range(2,long-2):
        me = city[i]
        line = city[i-2:i] + city[i+1:i+3]
        checking = [ me-x for x in line ]
        adding = checking[0]
        
        for j in checking:
            if adding > j:
                adding = j
        cnt += adding if adding>0 else 0
    
    print(f'#{idx} {cnt}')