n1 = 0         
n2 = 100       

# Part a: All squares less than n2
print("All squares less than n2:")
while n1 * n1 < n2:
    print(n1 * n1, end=' ')
    n1 += 1
print("\n")  

# Part b: All positive numbers divisible by 10 and less than n2
print("All positive numbers divisible by 10 and less than n2:")
n3 = 10         
while n3 < n2:
    print(n3, end=' ')
    n3 += 10
print("\n")  

# Part c: All powers of two less than n2
print("All powers of two less than n2:")
n4 = 1         
while n4 < n2:
    print(n4, end=' ')
    n4 *= 2


print("\n") 
print("\n") 
print("\n") 
# Part 2A Sum of all even numbers between 2 and 100
print("start of part 2")
n1 = 2
n2 = 100
sum_even = 0
print("Sum of all even numbers between 2 and 100:")
while n1 <= n2:
    sum_even += n1
    n1 += 2
print(sum_even)

print("\n") 
# part 2B Sum of all squares between 1 and 100
n1 = 1 
n2 = 100
sum_squares = 0
print("Sum of all squares between 1 and 100:")
while n1 <= n2:
    sum_squares += n1 * n1
    n1 += 1
print(sum_squares)
print("\n")

# Part 2C Sum of all odd numbers between a and b
a = 1
b = 100
sum_odd = 0
print("Sum of all odd numbers between a and b:")
while a <= b:
    if a % 2 != 0:  # Check if the number is odd
        sum_odd += a
    a += 1
print(sum_odd)
print("\n")

# Part 2D Sum of all odd digits of n
n = 1234567890
sum_odd_digits = 0
print("Sum of all odd digits of n:")
while n > 0:
    digit = n % 10 
    if digit % 2 != 0:  
        sum_odd_digits += digit
    n //= 10  
print(sum_odd_digits)
print("\n")

print("part 3")
# Part 3A sum of all even numbers between 2 and 100
n1 = 2
n2 = 100
sum_even = 0
print("Sum of all even numbers between 2 and 100:")
while n1<= n2:
    sum_even += n1
    n1 += 2
print(sum_even)
print("\n")

#part 3B sum of all squares between 1 and 100
n1 = 1
n2= 100
sum_squares = 0
print("Sum of all squares between 1 and 100:")
while n1 <= n2:
    sum_squares += n1 * n1
    n1 += 1
print(sum_squares)
print("\n")

# Part 3C powers from 2^0 to 2^20
n1 = 0
n2 = 20
print("Powers of 2 from 2^0 to 2^20:")
while n1 <= n2:
    print(2 ** n1, end=' ')
    n1 += 1
print("\n")

# Part 3D sum of all odd numbers a and b, where a and b are inputs
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
sum_odd = 0
print(f"Sum of all odd numbers between {a} and {b}:")
while a <= b:
    if a % 2 != 0:  # Check if the number is odd
        sum_odd += a
    a += 1
print(sum_odd)
print("\n")

# Part 3E sum of all odd digits of input
n = int(input("Enter an integer (n): "))
sum_odd_digits = 0
print(f"Sum of all odd digits of {n}:")
while n > 0:
    digit = n % 10  # Get the last digit
    if digit % 2 != 0:  # Check if the digit is odd
        sum_odd_digits += digit
    n //= 10  # Remove the last digit
print(sum_odd_digits)
print("\n")

print("part 4 ")
# smallest and largest number from user input
n = int(input("Enter the number of integers you want to input: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    smallest = float('inf')
    largest = float('-inf')
    for i in range(n):
        num = int(input(f"Enter integer {i + 1}: "))
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
    print("\n")

    # part 4b the number of even and odd inputs
    n = int(input("Enter the number of integers you want to input: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        even_count = 0
        odd_count = 0
        for i in range(n):
            num = int(input(f"Enter integer {i + 1}: "))
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        print(f"The number of even integers is: {even_count}")
        print(f"The number of odd integers is: {odd_count}")
        print("\n")

    # part 4c cumulative totals 
    n = int(input("Enter the number of integers you want to input: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        cumulative_total = 0
        for i in range(n):
            num = int(input(f"Enter integer {i + 1}: "))
            cumulative_total += num
            print(f"Cumulative total after {i + 1} inputs: {cumulative_total}")
        print("\n")

    # part 4d all adjacent duplicates
    n - int(input("enter the number of integers you want to unput:"))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        previous_num = None
        duplicates = []
        for i in range(n):
            num = int(input(f"Enter integer {i + 1}: "))
            if previous_num is not None and num == previous_num:
                duplicates.append(num)
            previous_num = num
        if duplicates:
            print("Adjacent duplicates found:", duplicates)
        else:
            print("No adjacent duplicates found.")
        print("\n")

    print("part 5")

 # part 5A : smallest and largest number from user input
n = int(input("Enter the number of integers you want to input: "))
if n <= 0:
    print("Please enter a positive integer.")
else: 
    smallest = float('inf')
    largest = float('-inf')
    for i in range(n):
        num = int(input(f"Enter integer {i + 1}: "))
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
    print("\n")

    