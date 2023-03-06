'''
M초에 K개 만드는 붕어빵
사람이 t초에 온다면, 사람수(cnt)보다 t시간에 만들어진 *k개 붕어빵이 많아야 한다
t초에 만들어지는 붕어빵 = t//M * k
'''

# 한 번이라도 불가능이 걸리면 break

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    lst = list(map(int,input().split()))

    lst.sort()
    cnt = 0
    ans = 'Possible'
    for t in lst:
        cnt += 1
        if (t//M)*K < cnt:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')