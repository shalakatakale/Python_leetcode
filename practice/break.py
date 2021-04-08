# break example
max = 3
x = int(input("How many candies do you want?\n"))
i = 1
while i <= x:
    if i > max:
        print('Out of stock')
        break
    print('candy', i)
    i+= 1
