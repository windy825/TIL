answer = [1,1] * 35
for i in range(2,31): #증가량1일때 전 에서 1가지씩, 증가량2일때 전전 에서 2가지씩
    answer[i] = answer[i-1] + answer[i-2]*2

for idx in range(1, int(input())+1):
    target = int(input())//10
    
    print(f'#{idx} {answer[target]}')