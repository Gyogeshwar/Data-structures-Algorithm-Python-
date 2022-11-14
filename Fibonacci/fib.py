def fib():
    a, b = 1, 1
    while (True):
        yield a
        a, b = b, a+b

for index , x in enumerate(fib()):
    if index is 10:
        break
    print("%s" % x)