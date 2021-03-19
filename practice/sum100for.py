'''python program to calculate sum of n number and see how much time it takes in for loop and
while loop'''
import time
time.time()
timestamp1 = time.time()

# program starts
number = 100
total = 0

for i in range(1,number+1):
    total = total + i

print("sum is ",total)
# program completed
timestamp2 = time.time()
print("{:.12f}".format(timestamp2-timestamp1))

# While loop
timestamp1 = time.time()

# Sum of natural numbers up to num
num = 100
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

### Program Completed ###

timestamp2 = time.time()
print((timestamp2 - timestamp1))






