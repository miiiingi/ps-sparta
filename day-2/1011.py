import sys

n = int(input())

for i in range(n):
    x, y = list(map(int,sys.stdin.readline().split()))

    distance = y-x-1 # 가야되는 거리
    num = 0 # 작동 횟수
    max_loc = 0
    min_loc = 0
    
    while True:
        max_loc += num+1   
        min_loc += num-1
        if min_loc <= distance <= max_loc :
            num+=1
            print(num+1)
            break
        num+=1


        # min_moving = loc-1
        # max_moving = loc+1
        # if min_moving <= distance <= max_moving :
        #     print(num+1)
        #     break
        # num+=1    
        # loc += max_moving

