'''
높이 값들만 보면서 비교하고 싶은 거니까,
[1] 너비부분을 인덱스로 하는 리스트 만들어서 저장해주기!!!
=> 2번 인덱스에 4를 저장 ( 2번째 좌표의 높이는 4)

[2] 왼쪽 (mx_idx 포함)
: 기둥의 끝에서부터(2번 인덱스) 증가시키며
자기보다 큰 값(4번 인덱스) 만나기 전까지 해당 높이(4)를 더해준다!
mx <- 0, ans<-0
for i (0,mx_idx+1):
mx <= max(mx,lst[i]
ans += mx

'''
N = int(input())
lst = [0]*1001
mx_idx = 0
mx = 0
for _ in range(N):
    L, H = map(int,input().split())

    # L위치에 H 기록
    lst[L] = H
    # [1] mx_idx 구하기
    if mx < H:
        mx_idx,mx = L,H

# [2-1] 왼쪽 끝 부터 처리
ans = 0
mx = 0
for i in range(mx_idx+1):
    mx = max(mx,lst[i])
    ans += mx

# [2-2] 오른쪽 끝 부터 처리
mx = 0
for i in range(1000,mx_idx,-1):
    mx = max(mx, lst[i])
    ans += mx

print(ans)
