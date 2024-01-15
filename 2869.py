a, b, v= list(map(int, input().split(' ')))

if (v - a) % (a - b) == 0:
    print((v - a) // (a - b) + 1)
else:
    print((v - a) // (a - b) + 1 + 1)

# 방정식을 이용한풀이
# x = day
# v = ax -(b(x-1))
# v = ax -bx +b

# x =(v - b) / (a-b)

# x =result 
# if x == int(x):
#     print(int(x))
# else:
#     print(int(x)+1)