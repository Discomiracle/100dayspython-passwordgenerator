import random
### MY PYTHON PASSWORD GENERATOR ###

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#add letters
password_str = ''
for count in range(0, nr_letters):
    password_str += random.choice(letters)
#add symbols
for count in range(0, nr_symbols):
    password_str += random.choice(symbols)
#add numbers
for count in range(0, nr_numbers):
    password_str += random.choice(numbers)

#randomise the password.

'''
LONG WAY:
pass_len = len(password_str)
randomised_password = [""] * pass_len
for char in range(0, pass_len):
    #keep selecting new positions in the list until finding an empty spot
    while True:
        pos = random.randint(0, pass_len-1)
        if randomised_password[pos] == "":
            randomised_password[pos] = password_str[char]
            break;
'''

#or SHORT WAY, because Python has a built-in shuffle method :)
randomised_password = list(password_str)
random.shuffle(randomised_password)

#convert list back to a string
randomised_password_str = ''.join(randomised_password)
print(f"Your new password is: {randomised_password_str}")
