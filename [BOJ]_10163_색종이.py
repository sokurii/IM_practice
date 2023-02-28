arr = [[0]*1001 for _ in range(1001)]
N = int(input())
for n in range(1,N+1):
    c,r,w,h = map(int,input().split()) # 열, 행, 너비(열), 높이(행)
    # [문어박사님] 행은 그대로, 열을 필요한 만큼 슬라이싱
    for i in range(r,r+h):
        arr[i][c:c + w] = [n] * w
    # arr[i][j]로 찾는 전형적인 방법
    # for i in range(r,r+h):
    #     for j in range(c,c+w):
    #         arr[i][j] = n



# [문어박사님] cnts: 빈도수 배열 사용해서, arr한번만 순회
cnts = [0]*(N+1)
for lst in arr:
    for n in lst:
        cnts[n] += 1
print(*cnts[1:],sep='\n')


# [내 방법] 색종이 개수별로 전체 배열 순회 : 시간 오래 걸림
# for n in range(1,N+1):
#     ans = 0
#     for lst in arr:
#         ans += lst.count(n)
#     print(ans)






