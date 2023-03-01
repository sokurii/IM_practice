'''
1. 가로, 세로 입력받은 길이를 각각 리스트에 담는다
2. 오름차순 정렬한다
3. 자신의 앞 요소를 차감한 값을 새로 저장한다
4. 최대 길이끼리 곱한 값 출력
'''
c, r = map(int,input().split())
N = int(input())

c_lst = [0,c]
r_lst = [0,r]

for _ in range(N):
    k, n = map(int,input().split())
    if k == 1:
        c_lst.append(n)
        c_lst.sort()
    else:
        r_lst.append(n)
        r_lst.sort()

# 가로
max_c = 0
for i in range(1,len(c_lst)):
    if c_lst[i]-c_lst[i-1] > max_c:
        max_c = c_lst[i]-c_lst[i-1]
# 세로
max_r = 0
for i in range(1,len(r_lst)):
    if r_lst[i]-r_lst[i-1] > max_r:
        max_r = r_lst[i]-r_lst[i-1]

print(max_c*max_r)