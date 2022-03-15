for idx in range(1, int(input())+1):
    n,m = map(int,input().split())
    case = [list(map(int,input().split())) for _ in range(n)]
    answer = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            adding = 0
            for a in range(m):
                for b in range(m):
                    adding +=case[i+a][j+b]
            answer = adding if adding > answer else answer
    print(f'#{idx} {answer}')