# C = (F-32) x 5/9
# F = (C x 9/5) + 32

choice=0
while(choice != 3):
    print("\n1. Fahrenheit to Celcius\n2. Celcius to Fahrenheit\n3. Exit")
    choice = int(input("Enter your choice : "))
    print()

    if choice == 1:
        fahrenheit = float(input("Enter temperature in fahrenheit : "))
        celcius = (fahrenheit - 32) * 5/9
        print("Temperature in Celcius : ",celcius)
    
    elif choice == 2:
        celcius = float(input("Enter temperature in celcius : "))
        fahrenheit = (celcius * 9/5) + 32
        print("Temperature in Fahrenheit :",fahrenheit)
    
    else:
        print("EXITING...")
