for idx in range(1,11):
    input()
    case = []
    for _ in range(100):
        line = list(map(int,input().split()))
        i=0
        while i<99:
            x = 1
            if line[i]==line[i+1]==1:
                while i+x <100 and line[i]==line[i+x]==1:
                    x +=1
                line[i] = [i,i+x-1]
                line[i+x-1] = [i+x-1, i]
            i +=x
        case.append(line)                 # 꺽이는 지점을 만나면, 그자리에 이동할 사다리위치의 인덱스를 담았습니다. 
                                          
    case = case[::-1]
    where = [i for i in range(100) if case[0][i] == 2][0]
 
    for i in range(100):
        now = case[i][where]
        if isinstance(now,list):          # 꺽이는 지점의 원소는 리스트로 만들었기 때문에, 해당 원소가 리스트라면
            where = now[1]                # 꺽는점이므로, 리스트의 이동할 지점 인덱스를 사용
 
    print(f'#{idx} {where}')

# 단순하게 순회하며, 꺽는점을 만나면 이동하려고 했으나 재미를 위해 
# 사다리 맵을 바꿔봤습니다.