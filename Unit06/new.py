def fib_sum():
    sum = 0
    a = 1
    b = 2
    while b < 4000000:
        if b % 2 == 0:
            sum += b
        next = a + b
        a = b
        b = next
    return sum

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
def fib_fast(n, a=1, b=2):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        next = a + b
        a = b
        b = next
        return fib_fast(n-1, a, b)

def main():
    
    for n in range(1, 101):
        print("f(",n,") =",fib_fast(n))
    print(fib_sum())
    

main()
        