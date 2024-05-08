# Write your solution to exercise 1 here
from statistics import mode
numbers = []
count = 0
sum = 0
repeated_numbers = []

while True:
    number = int(input("Type in a number: "))
    if number == 0:
       break
    numbers.append(number)
    count += 1
    sum += number
        
    if number in numbers:
        repeated_numbers.append(number) 
 
print (f"Biggest: {max(numbers)}")
print (f"Smallest: {min(numbers)}")
print (f"Number of numbers: {count}")
print (f"Sum: {sum}")
print (f"Most repeated: {mode(repeated_numbers)}")

