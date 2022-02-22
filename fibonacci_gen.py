def fibbonaci(n):
    """
    Takes a number up to which you need to determine the fibonacci numbers
    Returns a generator object
    """
    a, b = 1, 1
    while a <= n:
        yield a
        a, b = b, a + b

to_find = 10
fib = fibbonaci(to_find)

for el in fib:
    if el > to_find:
        break
    else:
        print(el, end=' ')