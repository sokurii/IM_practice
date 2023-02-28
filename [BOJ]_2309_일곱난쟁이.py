'''
- 가능한 정답이 여러개라면, 아무거나 출력
- 난쟁이의 키는 오름차순
- 9명 중 7명을 뽑아 합이 100

=> 난쟁이 7명을 뽑기 보다는, 2명을 뽑아낸다.
=> 전체 합에서 2명을 뺀 값이 100이라면 추출 성공.
'''
n = 9
height = []
# [1] 입력 받아 리스트에 넣기
for _ in range(n):
    height.append(int(input()))

# [2] 2명을 뽑아 전체 합에서 두 명의 키를 뺀 값이 0이라면, 그 두명의 키를 0으로
for i in range(0,n-1):
    for j in range(i+1,n):
        if sum(height) - (height[i]+height[j]) == 100:
            height[i],height[j] = 0,0

# [3] 리스트 오름차순 후 한 명씩 출력
height.sort()
for i in height[2:]:
    print(i)