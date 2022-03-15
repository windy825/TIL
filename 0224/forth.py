def checking(line):
    stack = []
    for i in line:
        if i =='.':            # 종료신호 받았는데, 스텍에 1개만 있는게 아니면 오류
            if len(stack) != 1:
                return 'error'
            return stack[0]
        elif i in '+-*/':      # 연산자들은 스텍에 2개이상 들어있어야 연산 가능
            if len(stack) < 2:
                return 'error'
            num2, num1 = int(stack.pop()), int(stack.pop())
            if i =='+':
                stack.append(num1 + num2)
            elif i =='-':
                stack.append(num1 - num2)
            elif i =='/':
                stack.append(num1 // num2)
            else:
                stack.append(num1 * num2)
        else:
            stack.append(i)
    return stack[0]
     
for tc in range(1, int(input())+1):
    line = input().split()
    print(f'#{tc} {checking(line)}')