# 1. FOR LOOP with range
print("For loop with range:")

for i in range(1, 6):
    print(i)


# 2. FOR LOOP with list
print("\nFor loop with list:")

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# 3. WHILE LOOP example
print("\nWhile loop example:")

count = 1

while count <= 5:
    print(count)
    count += 1   # important to avoid infinite loop


# 4. BREAK example
print("\nBreak example:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 5. CONTINUE example
print("\nContinue example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)