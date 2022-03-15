for idx in range(1, int(input())+1):
    stack, answer = [], 1
    line = input()

    for i in line:
        if i in {'(', '{'}:
            stack.append(i)
        elif i == ')':
            if stack and stack.pop() == '(':
                pass
            else:
                answer =0
                break
        elif i == '}':
            if stack and stack.pop() == '{':
                pass
            else:
                answer =0
                break
    if stack:
        answer =0

    print(f'#{idx} {answer}')