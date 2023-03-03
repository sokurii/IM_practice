N = int(input())

for _ in range(N):
    ans = 0
    cnt = 0
    test = input()

    for t in test:
        if t == 'O':
            cnt+=1
            ans += cnt
        else:
            cnt = 0

    print(ans)
