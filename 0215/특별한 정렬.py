for idx in range(1, int(input())+1):
    long = int(input())
    line = list(map(int,input().split()))
    
    for i in range(long):
        min_idx = i
        for j in range(i+1, long):
            if line[min_idx] > line[j]:
                min_idx = j
        line[i], line[min_idx] = line[min_idx], line[i]
    
    new = []
    for i in range(5):
        new.extend([line[long-i-1],line[i]])

    print(f'#{idx} ',end='')
    print(*new)