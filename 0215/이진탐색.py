def searching(start, end, where, cnt):
    m=(start+end)//2 
    if m==where: 
        return cnt 
    if where > m: 
        return searching(m,end,where,cnt+1) 
    else: return searching(start,m,where,cnt+1) 
    

for idx in range(int(input())):
    p,a,b =map(int,input().split()) 
    A = searching(1,p,a,0)
    B = searching(1,p,b,0) 
    
    if A>B: 
        print(f'#{idx+1} B') 
    elif A == B: 
        print(f'#{idx+1} 0') 
    else: 
        print(f'#{idx+1} A')