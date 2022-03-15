def fight(line):
    if len(line) <2:         # 분할은 이 조건을 만날때까지 꼐속 분할됩니다.
        return line[0]
     
    middle = (len(line)+1) // 2   # 2 파트로 분할 실시!
    a = line[:middle]
    b = line[middle:]
    a1 = fight(a)
    b1 = fight(b)
 
    key = ( a1[1] - b1[1] ) % 3   # a 기준으로 a값 - b값이 1이거나 0일때만 a가 승리
    if key in {1,0}:
        return a1
    return b1
 
for tc in range(1, int(input())+1):
    n = int(input())
    line = list(map(int,input().split()))
    line = list(zip(range(1,n+1), line))
 
    print(f'#{tc} {fight(line)[0]}')
