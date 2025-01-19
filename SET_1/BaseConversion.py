# choice = 0
# while(choice != 4):
#     print("\n1. Binary to Decimal")
#     print("\n2. Binary to Octal")
#     print("\n3. Binary to Hexadecimal")
#     print("\n4. Decimal to Binary")
#     print("\n5. Decimal to Octal")
#     print("\n6. Decimal to Hexadecimal")
#     print("\n7. Octal to Binary")
#     print("\n8. Octal to Decimal")
#     print("\n9. Octal to Hexadecimal")
#     print("\n1. Hexadecimal to Binary")
#     print("\n1. Hexadecimal to Decimal")
#     print("\n1. Hexadecimal to Octal")

def decimal_others(value, choice):
    if choice==1:
        return value
    elif choice==2:
        return '{0:b}'.format(value)
    elif choice==3:
        return '{0:o}'.format(value)
    elif choice==4:
        return '{0:x}'.format(value)
    else:
        return "Invalid Option"

def binary_others(value, choice):
    if choice==1:
        return value
    elif choice==2:
        return int(value,2)
    elif choice==3:
        return '{0:o}'.format(int(value,2))
    elif choice==4:
        return '{0:x}'.format(int(value,2))
    else:
        return "Invalid Option"
    
def octal_others(value, choice):
    if choice==1:
        return value
    elif choice==2:
        return int(value,8)
    elif choice==3:
        return '{0:b}'.format(int(value,8))
    elif choice==4:
        return '{0:x}'.format(int(value,8))
    else:
        return "Invalid Option"
    
def hex_others(value, choice):
    if choice==1:
        return value
    elif choice==2:
        return int(value,16)
    elif choice==3:
        return '{0:o}'.format(int(value,16))
    elif choice==4:
        return '{0:b}'.format(int(value,16))
    else:
        return "Invalid Option"
    
print("Convert from : \n1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal")
input_choice = int(input("Enter the choice : "))

if input_choice==1:
    decimal_num = int(input("Enter decimal number : "))
    print("Convert to : \n1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal")
    choice = int(input("Enter target conversion : "))
    print("Converted value: ",decimal_others(decimal_num,choice))

elif input_choice==2:
    binary_num = input("Enter binary number : ")
    print("Convert to : \n1. Binary\n2. Decimal\n3. Octal\n4. Hexadecimal")
    choice = int(input("Enter target conversion : "))
    print("Converted value: ",binary_others(binary_num,choice))

elif input_choice==3:
    octal_num = input("Enter octal number : ")
    print("Convert to : \n1. Octal\n2. Decimal\n3. Binary\n4. Hexadecimal")
    choice = int(input("Enter target conversion : "))
    print("Converted value: ",octal_others(octal_num,choice))

elif input_choice==4:
    hex_num = input("Enter hexadecimal number : ")
    print("Convert to : \n1. Hexadecimal\n2. Decimal\n3. Octal\n4. Binary")
    choice = int(input("Enter target conversion :"))
    print("Converted value: ",hex_others(hex_num,choice))

else:
    print("Invalid Input!!!")