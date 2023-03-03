N = int(input())
ans = 0

for r in range(1,N+1):
    for c in range(r,N+1):
        if r*c <= N:
            ans += 1

print(ans)