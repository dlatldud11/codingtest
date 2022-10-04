# 카카오 2022 블라인드 코딩테스트 k진수에서 소수 개수 구하기
def solution(n, k):
    answer = 0
    prime = makeK(n,k)

    prime_split = prime.split('0')

    for j in range(len(prime_split)):
        if len(prime_split[j]) > 0:
            if isPrime(int(prime_split[j])):
                answer += 1

    return answer

# 소수인지 판별하는 함수
# def isPrime(x):
#     if x < 2:
#         return False

#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

# n이 소수인지 판정
def isPrime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

#  k진수 만들어주는 함수
def makeK(num_n, num_k):
    num_return = ''
    while(num_n > 0):
        num_return = str(num_n % num_k) + num_return
        num_n = num_n // num_k
        # print(num, n)
    return num_return

    # print(s[::-1])
