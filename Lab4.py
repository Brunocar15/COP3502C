def fibonacci(number):
    
    for i in range(number):
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

def print_prime_factors (N):
     i=2
     print(f"{N} = ", end = "")
     first_factor = True
     while N>1:
        while N!=1:
            if not first_factor:
                 print(" * ", end="")
            if N%i == 0 and is_prime(i) :
                print(i, end="")
                N=N//i
                first_factor = False
            else:
                i += 1
                first_factor = True
     return ""
print(print_prime_factors(24))
