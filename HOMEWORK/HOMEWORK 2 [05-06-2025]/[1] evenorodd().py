''' [1] Write a function evenorodd(n) which accepts an argument n and 
        returns the value 0 if n is an even number, 1 otherwise      '''

def evenorodd(n):
    if n % 2 == 0:
        return 0
    else:
        return 1
    
number = int(input("Enter a number: "))
result = evenorodd(number)
print(result)