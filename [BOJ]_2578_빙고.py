'''
1. 빙고배열, 번호리스트 생성
2. for문으로 번호 리스트 순회하며 해당하는 값 빙고배열에서 0으로 바꾸기
3. 가로, 세로, 대각선 합이 0이 되면 빙고 카운트 +1
4. 카운트가 3이상 되면 그때 for문 i출력
'''

# [1] 빙고 배열, 사회자번호 리스트 생성
bingo = [list(map(int,input().split())) for _ in range(5)]
# change = list(map(list,zip(*bingo))) # 전치행렬
# change = bingo
# change = list(map(list,zip(*change))) # 전치행렬
say = []
for _ in range(5):
    say += list(map(int,input().split()))
print(say)
# [2] 부르는 번호대로 빙고판에 표시해주기
cnt = 0
line1 = 0
line2 = 0
for n in range(25):
    change = bingo
    for i in range(5):
        for j in range(5):
            if say[n] == bingo[i][j]:
                bingo[i][j] = 0
                change = list(map(list, zip(*bingo)))
                break
        print(change)
        print(bingo)
        print()
        # 대각선
        if bingo[i][i] == 0:
            line1 += bingo[i][i]
        if bingo[i][4-i] == 0:
            line2 += bingo[i][4-i]

        # [3] 3선 빙고 확인하기
        if sum(bingo[i])==0 or sum(change[i])==0:
            cnt += 1

    if line1 == 5 or line2 == 5:
        cnt += 1

    if cnt >= 3:
        print(say[n])
        break








