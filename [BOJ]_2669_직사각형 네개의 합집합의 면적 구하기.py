arr = [[0]*100 for _ in range(100)]

for _ in range(4):
    c1,r1,c2,r2 = map(int,input().split())

    for i in range(r1,r2):
        for j in range(c1,c2):
            arr[i][j] = 1

ans = 0
for lst in arr:
    ans += sum(lst)

print(ans)