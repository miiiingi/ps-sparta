# 네비게이터 : 김민기
# 드라이버 : 이주호
# 스펙테이터 : 김주원

"""
while True:
    n = int(input())
    if(n == 0):
        break
    else:
    
    소수인지 판별할것.

    소수인지 판별은 어떻게할까? 만약 A라는 수에 대한 소수가 있나를 판별한다면 실질적으로 A**0.5에 대해서만 알아보면 되고, 0,1은 소수아니니까 알 필요가 없다.0과
    
    n부터 2n까지 소수인지를 판별해서 소수라면 count를 증가시킨다

def prime()e
"""
import sys
def sieve_of_eratosthenes(n):
    # 2부터 n까지의 숫자를 포함하는 리스트 생성
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체 알고리즘 적용
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    # 소수만을 담은 리스트 생성
    result = [num for num in range(2, n + 1) if primes[num]]
    return result

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        n = int(n)
        n_list = sieve_of_eratosthenes(n) 
        n2_list = sieve_of_eratosthenes(2 * n) 
        print(len(set(n2_list) - set(n_list)))