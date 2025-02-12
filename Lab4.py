def fibonacci(number):
    if number == 1:
        return 0
    elif number ==2:
        return 1
    return fibonacci(number-1)+fibonacci(number-2)

def is_prime(N):
    M = N
    division_count=0
    for i in range(1, N+1):
         if N%i == 0:
              division_count += 1

    if N == 1 or N <= 0:
         return False      
    elif ((N % M == 0) and (N % 1 ==0)) and (division_count <= 2):
            return True
    else:
         return False