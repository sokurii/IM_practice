'''
-arr[i][j] = 1 개수 셀 때 행에서 바로 열 슬라이싱 하는 연습!
'''

N= int(input())
paper = [[0]*100 for _ in range(100)]

for _ in range(N):
    c, r = map(int,input().split()) # 열, 행
    for pr in range(r,r+10):
        paper[pr][c:c+10] = [1]*10

cnt = 0
for lst in paper:
    cnt += sum(lst)
print(cnt)