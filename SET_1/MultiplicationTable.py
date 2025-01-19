num = int(input("Enter a number : "))

for i in range(10,0,-1):
    j = 11-i
    print("%d * %d = %d"%(num,j,num*j),end='   ')
    print("%d * %d = %d"%(num,i,num*i))