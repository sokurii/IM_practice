'''
- N장 중 3장의 카드를 골라 M을 넘지 않는 최대합
=> N개 중 k개 뽑는 방법 범위 설정 잘 기억하기! 
'''
N,M = map(int,input().split())
cards = list(map(int,input().split()))

tot = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if tot < cards[i]+cards[j]+cards[k] <= M:
                tot = cards[i]+cards[j]+cards[k]

print(tot)


