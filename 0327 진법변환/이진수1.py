t = int(input())
for tc in range(1, t+1):
    n, line = input().split()
    
    answer = ''
    for i in line:
        num_10 = int(i,16)   # 10진수로 변환
        num_2 = ''
        while num_10:        # 2진수로 변환
            num_2 = str(num_10 % 2) + num_2
            num_10 //= 2
        
        answer += num_2.zfill(4)   # 4자리를 유지하기 위해 빈곳은 0으로 채우기
    
    print(f'#{tc} {answer}')