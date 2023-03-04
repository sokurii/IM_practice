'''
어! 이거 달팽이 숫자다.
'''
C, R = map(int,input().split())
N = int(input())

# 자리 배정 못하는 경우
if C*R < N:
    print(0)

# 자리배정
else:
    # [1] 주변을 1로 둘러싼 배열 생성. 범위 체크 필요 없음
    arr = [[1]*(C+2) for _ in range(R+2)]
    for i in range(1,R+1):
        arr[i][1:C+1] = [0]*C
    # arr = [[1]*(C+2)] + [[1]+[0]*C+[1] for _ in range(R)] + [[1]*(C+2)]

    # [2] 초기값 설정
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    sr, sc, k = 1, 1, 0

    # [3] 번호 찍어주기
    for n in range(1,N):
        arr[sr][sc] = n
        nr,nc = sr+dr[k], sc+dc[k]
        if arr[nr][nc] == 0:    # 비어 있으면 이동 가능
            sr,sc = nr,nc
        else:                   # 범위 밖이나 이미 이동한 위치
            k = (k+1)%4       # 방향 꺾기
            sr,sc = sr+dr[k], sc+dc[k]

    print(f'{sc} {sr}')
