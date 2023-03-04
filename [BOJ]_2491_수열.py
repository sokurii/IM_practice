'''
연속하면서 커지거나 작아지는
'''
N = int(input())
lst = list(map(int,input().split()))

cnt1 = 1
cnt2 = 1
mx = 1

for i in range(N-1):
    if lst[i] <= lst[i+1]:
        cnt1 += 1
    else:
        cnt1 = 1
    if cnt1 > mx:
        mx = cnt1


for i in range(N - 1):
    if lst[i] >= lst[i+1]:
        cnt2 += 1
    else:
        cnt2 =1
    if cnt2 > mx:
        mx = cnt2

print(mx)