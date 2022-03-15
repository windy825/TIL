def fix_post(s):
    answer, stack = '', []
    for i in s:
        if i.isdigit():
            answer +=i
        else:
            if i =='*':
                while stack and stack[-1] =='*':
                    answer += stack.pop()
                stack.append(i)
            else:
                while stack:
                    answer += stack.pop()
                stack.append(i)
    while stack:
        answer += stack.pop()
    return answer


for idx in range(1,11):
    _, s = input(), input()
    stack = []
    for i in fix_post(s):
        if i.isdigit():
            stack.append(int(i))
        else:
            num2, num1 = stack.pop(), stack.pop()
            if i =='+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)
    
    print(f'#{idx} {stack.pop()}') 