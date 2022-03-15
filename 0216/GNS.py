import sys
sys.stdin = open('a.txt')

for idx in range(1,int(input())+1):
    input()
    case, answer = {"ZRO ":0, "ONE ":0, "TWO ":0, "THR ":0, "FOR ":0, "FIV ":0, "SIX ":0, "SVN ":0, "EGT ":0, "NIN ":0}, ''
    line = input().split()
 
    for wow in line:
        case[wow+' '] +=1
    for x,y in case.items():
        answer += x*y

    print(f'#{idx}',answer.rstrip(),sep='\n')