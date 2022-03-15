for idx in range(1, int(input())+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    minn,maxx=10000*m, 3

    for i in range(n-m+1):
        sum=0
        for j in range(i,i+m):
            sum +=arr[j]
        if sum < minn:
            minn =sum
        if sum > maxx:
            maxx =sum

    print(f'#{idx} {maxx-minn}')