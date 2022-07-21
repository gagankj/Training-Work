list1 = ['m', 'n']
list2 = []
n = 3

for i in range(n):
    a = list1[0]+str(i+1)
    list2.append(a)

for i in range(n):
    a = list1[1]+str(i+1)
    list2.append(a)

print(list2)
