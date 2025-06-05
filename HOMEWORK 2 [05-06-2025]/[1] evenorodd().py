def evenorodd(n):
    if n % 2 == 0:
        return 0
    else:
        return 1
    
number = int(input("Enter a number: "))
result = evenorodd(number)
print(result)