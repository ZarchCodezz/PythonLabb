size = int(input("Enter size of list : "))
list = []
for _ in range(0,size):
    list.append(float(input("Enter value : ")))

sum = 0
for i in list:
    sum += i
avg = sum/len(list)
print("Average of values of list = ",avg)