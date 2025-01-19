while(1):
    my_str = input("Enter a string (enter 'exit' to exit): ")
    my_str = my_str.casefold()
    if my_str == 'exit':
        print("EXITING...")
        break
    
    rev_str = my_str[::-1]

    if my_str == rev_str:
        print("Palindrome!")
    else:
        print("Not a Palindrome!")