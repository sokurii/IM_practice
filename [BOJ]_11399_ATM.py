N = int(input())
lst = list(map(int,input().split()))
lst.sort()
ans = 0
cnt = 0

for i in lst:
    cnt += i
    ans += cnt

print(ans)





