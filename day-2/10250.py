import sys
iter = int(input())
for i in range(iter):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h
    room = n // h + 1
    if floor == 0:
        floor = h
        room -= 1
    print(floor * 100 + room)