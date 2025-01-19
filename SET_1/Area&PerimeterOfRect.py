choice = 0
while(choice != 3):
    print("1. Area\n2. Perimeter\n3. Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        length = float(input("Enter length of rectangle : "))
        breadth = float(input("Enter breadth of rectangle : "))
        area = length * breadth
        print("Area = ",area)

    elif choice == 2:
        length = float(input("Enter length of rectangle : "))
        breadth = float(input("Enter breadth of rectangle : "))
        perimeter = 2*(length+breadth)
        print("Perimeter = ",perimeter)

    else:
        print("EXITING...")