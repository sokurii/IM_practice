'''
- 스프레이는 + 또는 x 형태로 분사됨
- M 세기로 분사하면 노즐 중심으로 M칸 파리 퇴치
- 한 번에
'''
dp = [(-1,0),(1,0),(0,-1),(0,1)]    # '+' 방향
dm = [(-1,-1),(-1,1),(1,-1),(1,1)]  # 'x' 방향

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    sky = [list(map(int,input().split())) for _ in range(N)]

    # [1] '+' 방향 스프레이
    max_v = 0
    for i in range(N):
        for j in range(N):
            sum_p = sky[i][j]
            for k in dp:
                for m in range(1,M):    # 분사 세기만큼 설정
                    ni,nj = i+k[0]*m, j+k[1]*m
                    if 0<=ni<N and 0<=nj<N:
                        sum_p += sky[ni][nj]
            if sum_p > max_v:
                max_v = sum_p

    # [1] 'x' 방향 스프레이
    for i in range(N):
        for j in range(N):
            sum_m = sky[i][j]
            for k in dm:
                for m in range(1,M): # 분사 세기만큼 설정
                    ni,nj = i+k[0]*m, j+k[1]*m
                    if 0<=ni<N and 0<=nj<N:
                        sum_m += sky[ni][nj]
            if sum_m > max_v:
                max_v = sum_m

    print(f'#{tc} {max_v}')
