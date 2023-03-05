T = int(input())
for tc in range(1,T+1):
    C,P = map(int,input().split())
    code = list(map(int,input().split()))
    pw = list(map(int,input().split()))

    cnt = 0
    for i in range(P):
        if pw[i] in code:
            c = code.index(pw[i])
            code = code[c+1:]
            pw[i] = 0
            cnt += 1

    if cnt == P and sum(pw)==0:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')

