'''
문제를 잘 읽자
 x y p q 로 표현된다. 단 항상 x<p, y<q 이다
 => 항상 1번 사각형이 2번 사각형보다 왼쪽에 위치한다.. 이 부분 생각 안하고 풀었다.
'''

ans = 0
for _ in range(4):
    sc1,sr1,ec1,er1, sc2,sr2,ec2,er2 = map(int,input().split())

    c_lst = [sc1,ec1,sc2,ec2]
    dc = max(c_lst)-min(c_lst)

    r_lst = [sr1,er1,sr2,er2]
    dr = max(r_lst)-min(r_lst)

    ans = 0
    # 면
    if (ec1-sc1)+(ec2-sc2) > dc and (er1-sr1)+(er2-sr2) > dr:
        ans = 'a'
    # 선
    elif (ec1-sc1)+(ec2-sc2) == dc and (er1-sr1)+(er2-sr2) > dr:
        ans = 'b'

    elif  (ec1-sc1)+(ec2-sc2) > dc and (er1-sr1)+(er2-sr2) == dr:
        ans = 'b'
    # 점
    elif  (ec1-sc1)+(ec2-sc2) == dc and (er1-sr1)+(er2-sr2) == dr:
        ans = 'c'
    # 공백
    else:
        ans = 'd'

    print(ans)
