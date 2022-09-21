# Exercise №1
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = input('Enter action +  -  *  / : ')
if c == '+':
    print(f'Answer: {a + b}')
elif c == '-':
    print(f'Answer: {a - b}')
elif c == '*':
    print(f'Answer: {a * b}')
elif c == '/':
    print(f'Answer: {a / b}')
print()

# Exercise №2

a = int(input('Enter the number: '))
b = 1
while b ** 2 < a:
    print(b ** 2, end=' ')
    b += 1
print()

# Exercise №3
print()
a = int(input('Enter the number: '))
simple = True
b = 2
while b < a:
    if a % b == 0:
        simple = False
    b += 1
if simple:
    print("it's a simple number")
else:
    print("It's not simple number")

