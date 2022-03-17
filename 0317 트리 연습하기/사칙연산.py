# 후위 순회를 통해, 자식노드들의 값들을 이용해서 부모노드에 저장된 연산기호를 처리하기

def post(x):
    if len(case[x]) == 2:     # 자식이 없는 단말노드라면, 저장된 값 리턴
        return int(case[x][1])
    else:                     # 자식이 있는 부모노드라면, 자식노드들의 값을 받아서 연산처리
        oper = case[x][1]
        left = post(int(case[x][2]))
        right = post(int(case[x][3]))
        if oper == '+':
            return left + right
        elif oper == '-':
            return left - right
        elif oper == '*':
            return left * right
        else:
            return left / right
        

for tc in range(1, 11):
    n = int(input())
    case = [[None]] + [input().split() for _ in range(n)]  # 각 인덱스마다 노드번호가 매칭

    print(f'#{tc} {post(1):.0f}')