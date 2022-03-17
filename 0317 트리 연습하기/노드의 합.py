# 후위 순회를 통해 자식노드들의 합을 부모노드의 값으로 설정하기


def post(x):
    global n

    if x <= n:      # 후위순회 순서에 맞춰 트리 탐색
        post(x*2)     # 좌측 노드
        post(x*2 + 1)   # 우측 노드
        if not tree[x]:   # 만약 아직 값이 없는, 부모노드이면 값 처리
            tree[x] = tree[x*2] + tree[x*2 + 1]


t = int(input())
for tc in range(1, t+1):
    n, m, target = map(int, input().split())

    tree = [0] * (n*2 + 1)
    for _ in range(m):               # 단말노드의 값을 각 트리의 위치마다 반영
        node, value = map(int, input().split())
        tree[node] = value
    
    post(1)
    print(f'#{tc} {tree[target]}')