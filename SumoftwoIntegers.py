# TypeError: 'int' object is not iterable in sum(a,b):
    # sum(iterable, start=0)
    # - iterable: This is the iterable (e.g., list, tuple, etc.) whose elements you want to sum.
    # - start (optional): This is an optional parameter that represents the initial value of the sum. The default is 0.




def getSum( a: int, b: int) -> int:
    inp = [a,b]
    result =sum(inp)
    return result
    
print(getSum(1,2))
        