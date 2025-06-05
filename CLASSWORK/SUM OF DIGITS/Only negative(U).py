number = int(input("Enter the number : "))
sum = 0
digits = list(str(number))
for i in digits:
    sum += int(i)
print('Digits: ',digits)
print('Sum: ',sum)
