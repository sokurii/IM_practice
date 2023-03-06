def solve(arr):
    # [1] 가능한 모든 시작 위치
    for i in range(N):
        for j in range(N):
            # [2] 4방향 순서대로 체크
            for di, dj in ((-1,1),(0,1),(1,1),(1,0)):
                # [3] 해당 방향으로 뻗어 나가면서 4까지 곱해주기
                for mul in range(5):   # 0인 경우 i, j
                    # next i, j
                    ni, nj = i + di*mul, j + dj*mul
                    #  범위를 벗어났거나 범위내 지만 돌이 아닌 경우
                    if 0<= ni <N and 0<=nj<N and arr[ni][nj] == 'o':
                        pass #  오목 성공
                    else:
                        break # 다음 방향으로
                else: # for문 다섯 번 다 돌았을 경우. 즉 5개가 돌인 경우
                    return 'YES'
    return 'NO'




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    ans = solve(arr)
    print(f'#{tc} {ans}')





