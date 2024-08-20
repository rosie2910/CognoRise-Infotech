import random
import string

i = 0
password = ""
print("Welcome to Password Generator!")
print("Please enter your desired complexity from the following options")
complexity = input("Basic, Medium, Complex, Extremely Complex: ")
alphabet = list(string.ascii_lowercase)
if(complexity == "Basic"):
    length = 9
elif(complexity == "Medium"):
    length = 15
elif(complexity == "Complex"):
    length = 20
else:
    length = 25

while(i < length):
    dec = random.randint(1,3)
    if(dec == 1):
        decision = "Letter"
        num = random.randint(0,25)
        addedValue = alphabet[num]
        password = password + addedValue
    elif(dec == 2):
        decision = "Number"
        num = random.randint(0,9)
        password = password + str(num)
    else:
        decision = "Special"
        num = random.randint(1,3)
        if(num == 1):
            addedValue = "!"
        elif(num == 2):
            addedValue = "*"
        else:
            addedValue = "_"
        password = password + addedValue
    
    i = i + 1

print("Your password has been generated! Please make a note of your password")
print(password)


    

    


