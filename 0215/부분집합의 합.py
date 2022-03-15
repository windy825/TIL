for idx in range(1, int(input())+1):
    n,k = map(int,input().split())
    answer = 0
    for num in range(2**12):
        sum = cnt = 0
        for i in range(12):
            if num & (1<<i):
                sum += i+1
                cnt += 1        
        if sum==k and cnt==n:
            answer +=1
            
    print(f'#{idx} {answer}')