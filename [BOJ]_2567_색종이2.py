'''
0으로 둘러 쌓은 배열을 만들어 ni,nj 범위설정을 할 필요가 없었다!
계속 이 부분 때문에 테케는 맞고 답은 틀리게 나온듯 하다. 
'''
N = int(input())
paper = [[0]*102 for _ in range(102)]

for _ in range(N):
    C, R = map(int,input().split())
    for r in range(R,R+10):
        for c in range(C,C+10):
            paper[r][c] = '*'
cnt = 0

for i in range(1,101):
    for j in range(1,101):
        if paper[i][j] == '*':
            for d in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = i+d[0], j+d[1]
                if paper[ni][nj] == 0:
                    cnt += 1

print(cnt)

