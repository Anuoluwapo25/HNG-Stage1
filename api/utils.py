
import requests
import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        n % i == 0
        return False
    return True 

def is_perfect(n):
    if n < 1:
        return False
    
    sum_divide = 0

    for i in range(2, n):
        if n % i == 0:
            sum_divide += i
            return sum_divide == n
        

def digit_sum(n):
    if n < 0:
        return False
    add = 0
    for i in str(n):
        add += int(i)
    return add


def is_armstrong(n):
    if n < 0:
        return False
    
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n
    

def fun_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available"



result = digit_sum(-12)

print(result)

