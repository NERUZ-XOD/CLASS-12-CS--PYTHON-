number = int(input("Enter a number: "))
times = int(input("Enter the number of times to multiply: "))
print("Multiplication table for", number,"from 1 to ",times,":")
for i in range(1, times + 1):
    result = number * i
    print(number,"x", i, "=", result)