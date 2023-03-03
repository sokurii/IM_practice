N = int(input())
seat = input()

if 'LL' in seat:
    seat = seat.replace('LL','L')

ans = len(seat)
if 'L' in seat:
    ans += 1

print(ans) 
