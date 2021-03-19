s  = "   1   2   3"
a = s.split()
print(a)
        # return len(s.strip().split(' ')[-1])
digits =  [9,9,9,9]
number = []
for i in digits:
    number.append(str(i))

print(number)
number = "".join(number)
print(number)
number = int(number) + 1
print(type(number))
new_2 = str(number)
print(new_2)
print(list(new_2))
print(new_2.split())

new_num = 10
print(bin(new_num))

a = x = 5
a =a - (a * a - x) / (2 * a)
print(int(a))

s = "A man, a plan, a canal: Panama"
for element in s:
    if element.isalnum():
        b= "".join([element])
a = b.lower()
print("this is giving me wrong output", a)
s = "".join([c.lower() for c in s if c.isalnum()])
print("this is giving me right output",s)