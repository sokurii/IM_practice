'''
배열을 순회하며 연속하는 1의 개수가 k개인 것들 세어주기

* 0을 또는 배열의 끝(마지막 열)을 만나기까지  cnt 했던 값 뽑아주기
이 끝을 단순하게 계산하기 위해 배열의 행과 열에 0을 추가해주서
그냥 0을 만났을 때 cnt 뽑아내며 어디에 단어가 들어갈 수 있을 지 계산

* 세로의 경우 전치행렬 활용하기

if != 0 : cnt +=1
else:
    if cnt == K:
        ans += 1
    정답 확인 후 cnt 초기화
'''
def count(arr):
    ret = 0
    for lst in arr: # 배열 안 리스트를 하나씩 순회한다
        cnt= 0      # 각 행당 cnt 초기화
        for j in range(len(lst)):
            if lst[j]:  # 값이 0이 아닌 경우(즉, 1인 경우)
                cnt += 1
            else:
                if cnt == K : # 글자길이만큼 세어 진다면 +1
                    ret += 1
                cnt = 0       # 그렇지 않으면 cnt = 0
    return ret

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split()))+[0] for _ in range(N)]+[[0]*(N+1)]
    arr_t = list(map(list,zip(*arr)))

    ans = count(arr) + count(arr_t)
    print(f'#{tc} {ans}')

