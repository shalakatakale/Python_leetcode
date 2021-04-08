# continue example
for i in range(1, 31):
    if i%3 == 0 or i%5 == 0:
        continue # it will skip the lines below (skip the remaining statements)
    print(i)