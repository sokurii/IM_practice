lst = []
for _ in range(10):
    a = int(input())
    lst.append(a%42)

ans = []
for i in lst:
    if ans and i in ans:
        pass
    else:
        ans.append(i)

print(len(ans))