N= int(input())
for _ in range(N):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A = A[1:]
    B = B[1:]

    for i in range(4,0,-1):
        if A.count(i) > B.count(i):
            print('A')
            break
        elif A.count(i) < B.count(i):
            print('B')
            break
        # 마지막까지 break 안되었으면 무승부
    else:
        print('D')

'''
<for ~ else 문>
- else는 for반복문 마지막 요소까지 성공적으로 다 돌았을 때 실행한다
- 문제에서는 if~, elif~ 다 돌았을 때 else를 실행(정상종료)
- 하지만 break를 만나면 else는 수행되지 않고 for문 완전히 빠져 나감(강제종료)
'''