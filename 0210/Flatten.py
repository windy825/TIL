for idx in range(1, 11):
    move = int(input())
    box = list(map(int,input().split()))
    maxx, minn = 0,0
    while move:
        for i in range(len(box)):
            maxx = i if box[maxx] < box[i] else maxx
            minn = i if box[minn] > box[i] else minn
        if box[maxx] - box[minn] <=1:
            break
        box[maxx] -=1
        box[minn] +=1
        move -=1
    for i in range(len(box)):
        maxx = i if box[maxx] < box[i] else maxx
        minn = i if box[minn] > box[i] else minn
    print(f'#{idx} {box[maxx] - box[minn]}')