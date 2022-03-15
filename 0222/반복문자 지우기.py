for idx in range(1, int(input())+1):
    stack = []
    
    for char in input():
        while stack and stack[-1] == char:
            stack.pop()
            break
        else:
            stack.append(char)
    
    print(f'#{idx} {len(stack)}')