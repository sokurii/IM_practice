N,M,L = map(int,input().split()) # 인원, 제한횟수, 방향
player = [i for i in range(1,N+1)]  # 참여하는 친구들
score = [0 for _ in range(N+1)]     # 공 받은 횟수 리스트
score[1] = 1
cnt = 0

for n in range(L):
    ball = player.pop(0)
    player.append(ball)
    print(player)


