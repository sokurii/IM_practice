email = input()
long = len(email)

lst = []
for r in range(1,long+1):
    for c in range(1,long+1):
        if r<=c and r*c == long:
            lst.append((r,c))

row = lst[-1][0]
ans = ''
for i in range(row):
    for e in range(long):
        if e % row == i:
            ans += email[e]
print(ans)