'''
N*N 크기의 하늘에 별자리가 찍혀 있다.
촬영 가능 영역은 초점(A,B)를 중심으로 K*K 영역만큼.
카메라를 확대했을 때 모든 별을 찍을 수 있다면 : 확대 횟수 +1,  촬영 영역 -2

1. 하늘에 위치한 별의 개수와 카메라 범위 내 별의 개수를 비교한다
2. 만약 개수가 일치한다면 확대 횟수 +1, 촬영 영역 -2 하고 반복문 계속 실행
3. 만약 개수가 불일치한다면 반복 break

'''
T = int(input())
for tc in range(1, T+1):
    N, K, A, B = map(int, input().split())
    space = [list(input().split()) for _ in range(N)]

    # [1] 별의 개수 세기
    star = 0
    for i in range(N):
        for j in range(N):
            if space[i][j] == '*':
                star += 1


    # [2] 렌즈 범위 내 별의 개수 세기
    zoom = -1    # 확대 횟수
    while True:
        k = K // 2
        cnt = 0
        for r in range(A - k, A + k + 1):
            for c in range(B - k, B + k + 1):
                if 0 <= r < N and 0 <= c < N:
                    if space[r][c] == '*':
                        cnt += 1

        if star == cnt:
            zoom += 1
            K -= 2

        elif star != cnt:
            break

    print(f'#{tc} {zoom}')








