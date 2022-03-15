for idx in range(1, int(input())+1):
    s1, s2 = input(), input()
    print(f'#{idx} {1 if s1 in s2 else 0}')