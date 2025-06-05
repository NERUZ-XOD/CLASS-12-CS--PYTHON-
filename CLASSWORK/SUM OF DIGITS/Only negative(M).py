number = int(input("Enter the number : "))
sum = 0
digits = list(str(number))
while number != 0:
    sum += number % 10
    number = number // 10
print('Digits: ',digits)
print('Sum: ',sum)
