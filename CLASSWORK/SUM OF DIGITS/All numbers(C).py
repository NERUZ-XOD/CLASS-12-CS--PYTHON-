number = input("Enter a number (can be negative or decimal): ")

# Initialize sum
digit_sum = 0
digits = []

# Loop through each character
for char in number:
    if char.isdigit():
        digits.append(char)
        digit_sum += int(char)

print("Digits:", digits)
print("Sum of digits:", digit_sum)
