'''#2 Add two numbers
but my mistake is I need to use Linkedlist and I have used array / list and used pop or indexing'''

l1 = [2,4,3]
l2 = [5,6,4]

sum_l1 = 0
sum_l2 = 0
#def find_num():
while l1:
    sum_l1 = sum_l1*10 + l1[-1] #use pop l1.pop() no need for next line
    l1 = l1[0:len(l1)-1]
print(sum_l1)
while l2:
    sum_l2 = sum_l2*10 +l2[-1]
    l2 = l2[0:len(l2) - 1]
print(sum_l2)
sum_l3 = sum_l1 + sum_l2
sum_l3 = int(sum_l3)
print(sum_l3)
l3 = []
while sum_l3 != 0:
    l3_list = int(sum_l3%10)
    sum_l3 = int(sum_l3/10)
    l3.append(l3_list)
print(l3)

