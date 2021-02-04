import time

def constant_order():
    start_time = time.time_ns()
    n = 7000
    answer = "Impar"
    if n % 2 == 0 :
        answer = "Par"
    end_time = time.time_ns()
    print("El tiempo es igual:", end_time - start_time)
    return answer

def linear_order():
    return ("hola")

def quadratic_order():
    return ("Chao")
