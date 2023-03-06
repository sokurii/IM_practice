'''
[첫번째 방법]
중간값(N//2)를 찾아서 i<= 중간값인 경우와 else 인 경우 나눠서 생각
i<=중간값 : 점점 증가하는 , else : 점점 감소하는.. => 이들의 누적 합을 구해 준다.

'''
T = int(input())
for tc in range(1,T+1):
    N= int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    m = N//2
    ans = 0
    for i in range(N):
        if i <= m:
            for j in range(m-i,m+i+1):
                ans += arr[i][j]
        else:
            for j in range(i-m,N-(i-m)):
                ans += arr[i][j]

    print(f'#{tc} {ans}')
