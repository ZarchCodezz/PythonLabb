import random
import string

length = int(input("Enter length of password : "))
allchar = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(allchar) for i in range(length))
print(password)