N = int(input())

bee = 1
cnt = 1

while N > bee:
    bee += 6*cnt
    cnt += 1

print(cnt)