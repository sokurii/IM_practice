'''
- 빈 스트에 한 명씩 인덱스 번호(줄 순서)를 넣어주며 삽입
=> list.insert(인덱스,값)메서드를 알게 되었다!
'''

T = int(input())
num = list(map(int,input().split()))

line = []
for i in range(T):
    line.insert(i-num[i],i+1)

for p in line:
    print(p, end=' ')

