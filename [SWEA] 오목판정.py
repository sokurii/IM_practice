'''
-오목인 돌을 1로, 아닌 곳은 0으로 바꾸기
-연속한 1의 개수가 5 이상인 경우 yes 출력
'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    game = [list(input()) for _ in range(N)]
    ans = 'NO' # 오목 판정 기본값을 no로 설정

    # [1] 돌이 있는 경우 1, 아닌 경우 0으로 바꾸어 준다
    for lst in game:
        for d in range(N):
            if lst[d] == 'o':
                lst[d] = 1
            else:
                lst[d] = 0

    # [2-1] 가로 오목 판정
    for row in game:
        for i in range(N-4):
            for k in range(i+5,N+1):  # 연속하는 오목이 5 이상
                if row[i:k].count(1) >= len(row[i:k]):
                    ans = 'YES'


    # [2-2] 세로 오목 판정 (전치행렬)
    col_game = list(map(list, zip(*game)))
    for col in col_game:
        for i in range(N-4):
            for k in range(i+5,N+1):  # 연속하는 오목이 5 이상
                if col[i:k].count(1) >= len(col[i:k]):
                    ans = 'YES'


    # [2-3] 대각선 오목 판정
    line1 = 0
    line2 = 0
    for i in range(N):
        line1 += game[i][i]
        line2 += game[i][N-1-i]

    if line1 >= 5 or line2 >= 5:
        ans = 'YES'

    print(f'#{tc} {ans}')


