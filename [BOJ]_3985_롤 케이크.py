'''
이렇게 안 풀어도 될 문제를 이렇게 푼 것 같다
=> 기대되는 리스트와, 실제로 받은 리스트를 각각 만들었어도 될 듯
=> 문어박사님 강의 들어보기
'''

L = int(input())
N = int(input())
cake = [0 for _ in range(L+1)]

ans1 = []   # 기대 방청객 번호
ans2 = []   # 실제 방청객 번호
for i in range(1,N+1):
    s,t = map(int,input().split())
    ans1.append(t-s)

    for n in range(s,t+1):  # 케이크 나눔
        if cake[n] == 0:
            cake[n] = i
    ans2.append(cake.count(i))


print(ans1.index(max(ans1))+1)
print(ans2.index(max(ans2))+1)

