'''
스위치 21번 부터 줄바꿈 해야 하더라..
'''
N = int(input())
light = [0] + list(map(int,input().split()))
num = int(input())
for _ in range(num):
    g,n = map(int,input().split())

    if g == 1:                  # 남학생
        for i in range(1,N+1):
            if i%n == 0:
                light[i] = 1 if light[i] == 0 else 0

    else:                       # 여학생
        light[n] = 1 if light[n] == 0 else 0
        k = 1
        while 1 <= n-k and n+k <= N and light[n-k] == light[n+k]:
            light[n-k] = 1 if light[n-k] == 0 else 0
            light[n+k] = 1 if light[n+k] == 0 else 0
            k += 1

for i in range(1,N+1):
    print(light[i],end=' ')
    if i % 20 == 0:
        print()



