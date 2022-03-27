t = int(input())
for tc in range(1, t+1):
    target = float(input())

    answer, cnt = '', 0
    while target != 0.0 and cnt < 12:     # 대상이 0이 안 되거나 12자릿수를 안 넘길 동안 반복
        target *= 2
        answer += '1' if target >= 1 else '0'
        target -= 1 if target >= 1 else 0
        
        cnt += 1
    answer = answer if not target else 'overflow'  # 만약 대상이 0이 아니라면 12자리 이상이 필요함.
    
    print(f'#{tc} {answer}') 