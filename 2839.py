# 네비게이터 : 김주원\n",
# 드라이버 : 이주호\n",
# 스펙테이터 : 김민기\n",

# 네비 
# 1. 입력값을 든 나눈 몫을 a 에저장
# 2. a번 반복 for문 > n에서 씩 빼주는 반복문 작성 횟수를 체크해주는 변수 i 생성\n",
#  3빼준값을 5로 나누었을 때 나누어지는가? yes > (몫 + i )리턴
# no 

# 비커에 물을 퍼낸다 5짜리 3짜리
# 5로 하는게 편하니 5로 맞출 수 있는지 계속 확인
# "그 전까지 3으로 퍼냄
# "난 안힘드니까 컴터한테 계속 시켜야지

n = int(input())
result = 0
while n >= 0:
    if n%5==0:
        result += (n//5)
        print(result)
        break
    n-=3
    result+=1
else:
    result = -1
    print(result)