for idx in range(1,int(input())+1):
    input()
    arr = list(map(int,input().split()))
    maxx=minxx =arr[0]
    for i in arr:
        if i>maxx:
            maxx=i
        elif i<minxx:
            minxx=i
    print(f'#{idx} {maxx-minxx}')