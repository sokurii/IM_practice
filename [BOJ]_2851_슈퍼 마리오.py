lst = []
for _ in range(10):
    lst.append(int(input()))

ans= 0
cnt=0
for i in lst:
    cnt += i
    if 100-ans >= abs(100-cnt):
        ans = cnt
print(ans)


'''
그거 그렇게 푸는 거 아닌데.. 의 표본.. => 런타임 에러 남 ㅋㅎ
'''
# 내 코드..였던 것
# cnt = 0
# lst = []
# ans = []
# for _ in range(1,11):
#     cnt += int(input())
#     lst.append(cnt)
#     ans.append(abs(cnt-100))
#
# idx = []
# min_idx = ans[0]
# for i in range(1,10):
#     if ans[i] <= min_idx:
#         min_idx = ans[i]
#         idx.append(i)
#
# print(lst[max(idx)])