def cbt(n):     # 트리 생성하기 값은 1부터 차례대로 넣기
    tail = 1
    while tail <= n:
        tree[tail] = line[tail-1]
        now = tail
        while now != 1:   # 최소힙을 위해 자리 바꾸기
            if tree[now] > tree[now//2]:
                break
            tree[now], tree[now//2] = tree[now//2], tree[now]
            now //= 2
        tail += 1

def summ(n):   # 조상노드들의 값을 모두 합하는 함수
    summ = 0
    while n != 0:   # 루트노드까지 더한 후, 종료
        summ += tree[n//2]
        n //= 2
    return summ


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    line = list(map(int, input().split()))
    tree = [0] * (n+1)
    cbt(n)
    
    print(f'#{tc} {summ(n)}')