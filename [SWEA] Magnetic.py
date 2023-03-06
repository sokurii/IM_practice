'''
* 빈칸(무시), 1, 2의 경우
=> 파란색(2)을 찾고 직전값이 빨간색(1)인 경우 교착!
=> 직전 색깔을 갱신 <- prev

[1] 열을 행으로 처리 (전치행렬)
[2] arr의 lst를 하나씩 꺼내오며 조사하기
    for lst in arr:
        prev = 0
        for n in lst:
            if n :  # 0 아닌 경우만  처리
                if n == 2 and prev == 1: (교착상태)
                    ans = 1
                prev = n
'''

T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    # 전치행렬 만들기
    arr_t = list(zip(*arr))
    for lst in arr_t:
        prev = 0
        for n in lst:
            if n :
                if n==2 and prev == 1:
                    ans += 1
                prev = n

    print(f'#{tc} {ans}')