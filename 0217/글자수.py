for idx in range(1, int(input())+1):
    s1, s2 = set(input()), input()
    answer = 0
    for a in s1:
        cnt =0
        for b in s2:
            if a==b:
                cnt +=1
        answer = cnt if answer<cnt else answer
    print(f'#{idx} {answer}')