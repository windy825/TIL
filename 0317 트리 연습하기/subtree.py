# 서브트리의 노드 개수 구하기 문제

def check(x):
    global cnt  # 조건에 맞는 노드를 탐색할때 마다 1씩 카운트
    cnt +=1            
    for i in range(0, len(line), 2):
        if x == line[i]:   # 요구조건에 충족되는 서브트리의 구성노드라면 함수 호출
            check(line[i+1])

t = int(input())
for tc in range(1, t+1):
    e, start = map(int, input().split())
    line = list(map(int,input().split()))
    cnt = 0
    check(start)

    print(f'#{tc} {cnt}')