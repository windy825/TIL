for idx in range(1,11):
    input()
    case = [list(map(int,input().split())) for _ in range(100)]
    maxx, answer, adding, adding2 =0, [0,0], [0]*100, [0]*100
 
    for i in range(100):
        adding = [a+b for a,b in zip(adding, case[i])]
        answer[0] +=case[i][i]
    answer+= adding
 
    case = list(map(list,zip(*case)))
    for j in range(100):
        adding2 = [a+b for a,b in zip(adding2, case[j])]
        answer[1] +=case[j][j]
    answer+= adding2
    for v in answer:
        maxx = v if maxx<v else maxx
 
    print(f'#{idx} {maxx}')