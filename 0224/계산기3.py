for tc in range(1,11):
    n = int(input())
    line = input()
 
    stack, post_fix = [], ''
    for i in line:
        if i.isdigit():       # 숫자면 일단 담기
            post_fix +=i
        elif i =='*':                       # 해당 연산자보다 우선순위가 이상일때만 빼주기
            while stack and stack[-1] =='*':
                post_fix +=stack.pop()
            stack.append(i)
        elif i ==')':
            while stack[-1] !='(':
                post_fix +=stack.pop()
            stack.pop()
        else:
            if i =='+':                     # 해당 연산자보다 우선순위가 이상일때만 빼주기, 괄호를 만나면 스탑하기
                while stack and stack[-1] !='(':
                    post_fix +=stack.pop()
                stack.append(i)
            else:
                stack.append(i)
    while stack:                    # 처리가 끝나고 남은 연산자들은 뒤에 다 붙이기
        post_fix +=stack.pop()
     
    stack = []
    for j in post_fix:
        if not j.isdigit():
            num2, num1 = int(stack.pop()), int(stack.pop())
            if j =='*':
                stack.append(num1 * num2)
            elif j =='+':
                stack.append(num1 + num2)
        else:
            stack.append(j)
    print(f'#{tc} {stack[0]}')