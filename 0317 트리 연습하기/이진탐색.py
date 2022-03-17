# 중위 순회를 통해, 값 처리하기

def in_order(x):
    global num  # 1씩 증가시키면서 노드의 값으로 지정

    if line[1] and line[n//2]:  # 찾아야 할 값이 탐색되었으면 종료
        return
    if x <= n:
        in_order(x*2)   # 좌측 자식 탐색
        line[x] = num   # 부모
        num +=1
        in_order(x*2 + 1) # 우측 자식 탐색


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    line, num = [0] * (n+1), 1    # 노드배열, num은 노드마다 들어갈 값
    
    in_order(1)
    print(f'#{tc} {line[1]} {line[n//2]}')