def check(s,e, target):
    global cnt
    flag = -1  # 방향을 넣어주는 것 1은 오른쪽, 0은 왼쪽
 
    while True:
        mid = (s + e) // 2
        if a[mid] == target:
            cnt += 1
            return
        if a[mid] < target: 
            if flag == 1:  # 이전에 같은 방향이었다면 무효
                return
            flag = 1
            s = mid+1
        else:
            if flag == 0:  # 이전에 같은 방향이었다면 무효
                return
            flag = 0
            e = mid-1
     
 
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
 
    temp, cnt = set(a), 0    # 리스트에서의 in 보다 해쉬함수가 적용된 set 자료형에서 in 쓰기
    for target in b:         # O(N) -> O(1)
        if target in temp:
            check(0,n-1, target)
     
    print(f'#{tc} {cnt}')
