def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

while(1):
    num = int(input("Enter a positive integer (enter -1 to exit) : "))
    if num==-1:
        print("EXITING...")
        break
    print("%d! = %d"%(num,factorial(num)))
