for idx in range(int(input())):
    input()
    line = [0]*10
    for num in input():
        line[int(num)] +=1
    
    cnt=back = 0
    for i in line:
        if i>cnt: cnt=i
    for i in range(10):
        if line[::-1][i] ==cnt:
            back =i
            break

    print(f'#{idx+1} {9-back} {cnt}')