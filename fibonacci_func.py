def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        next_num = fib[i - 1] + fib[i - 2]
        fib.append(next_num)
    return fib[:n]