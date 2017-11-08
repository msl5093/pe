def fib():
    a, b = 0, 1
    while True:
        yield a
        b = a + b
        yield b
        a = a + b
        if a >= 4000000:
            raise StopIteration

def sumStuff(generatedList):
    evenNums = [n for n in generatedList if n % 2 == 0]
    return sum(evenNums)

fibList = list(fib())
print(sumStuff(fibList))