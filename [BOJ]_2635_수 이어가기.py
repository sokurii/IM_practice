'''
산으로 가고 있어서 검색 후 공부했다
(+0,+1 부터 시작해서 부호 바꾸고 점점 커지는..)
'''
N = int(input())
ans = []

for i in range(1,N+1):
    left = N
    right = i
    lst = [N,i]

    while True:
        next = left - right
        if next >= 0:       # 양수일 때
            lst.append(next)
            left = right
            right = next
        else:               # 음수일 때
            if len(lst) > len(ans):
                ans = lst
            break

print(len(ans))
print(*ans)

