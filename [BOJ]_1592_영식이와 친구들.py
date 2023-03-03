'''
원형으로 게임을 한다는 말에 원형큐에 사로잡혔었다.
인덱스에 사람 수(N)만큼 나눈 나머지로 계산하는 것이 반복의 포인트
(이렇게 해야 시계방향 L만큼, 반시계 방향 L만큼 이동할 수 있음)
델타 검색 할 때도 배웠던 방법인데..공부하자
'''

N,M,L = map(int,input().split()) # 인원, 제한횟수, 방향
player = [0 for _ in range(N)]     # 공 받은 횟수 리스트

cnt = 0
p = 0   #1 번 부터 시작
player[p] = 1

while True:
    if player[p] == M:
        break

    if player[p] % 2:
        p = (p+L)%N
    else:
        p = (p-L)%N

    player[p] += 1
    cnt += 1

print(cnt)

