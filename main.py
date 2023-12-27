#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pw_length = nr_letters + nr_symbols + nr_numbers
pw_letters = []
pw_numbers = []
pw_symbols = []
password = ""
for i in range(0, nr_letters):
    pw_letters.append(letters[random.randint(0, 51)])
for i in range(0, nr_symbols):
    pw_symbols.append(symbols[random.randint(0, 8)])
for i in range(0, nr_numbers):
    pw_numbers.append(numbers[random.randint(0, 9)])
pw_list = [pw_letters, pw_symbols, pw_numbers]
x = 2
#for i in range(0, pw_length):
while (len(pw_list) != 0):
    #print(pw_list)
    cha_type = random.randint(0, x)
    if (len(pw_list[cha_type]) == 0):
        #cha_type=random.randint(0, x)
        x -= 1
        pw_list.remove(pw_list[cha_type])
    else:
        test = len(pw_list[cha_type]) - 1
        #print(test)
        cha = random.randint(0, test)
        pw_cha = pw_list[cha_type][cha]
        password += pw_cha
        pw_list[cha_type].remove(pw_cha)

print(password)
