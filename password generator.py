import random

answers = ["yes","no"]
digits = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!',"@","#","$",'%','^','&','*','(',')',',','.']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  'I', 'J', 'K', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
combined_list = lower_letters + upper_letters

passlength = 0

include_digits = False
include_symbols = False

random_digit = random.choice(digits)
random_symbol = random.choice(symbols)
random_lowerletter = random.choice(lower_letters)
random_uppletter = random.choice(upper_letters)

temp_list = random_digit + random_symbol + random_lowerletter + random_uppletter

def specify():
    user_answer1 = input("would you like to include digits? (yes/no): ").lower()
    while user_answer1 not in answers:
        user_answer1 = input("invalid input. would you like to include digits? (yes/no): ").lower()
    include_digits = user_answer1 == 'yes'

    user_answer2 = input("would you like to include symbols? (yes/no): ").lower()
    while user_answer2 not in answers:
        user_answer2 = input("invalid input. would you like to include symbols? (yes/no): ").lower()
    include_symbols = user_answer2 == 'yes'

    passlength = int(input("how long do you want your password?: "))
    return passlength


def main():
    global include_digits, include_symbols, passlength, combined_list, temp_list

    passlength = specify()

    if include_digits:
        combined_list += digits
    if include_symbols:
        combined_list += symbols

    while len(temp_list) < passlength:
        temp_list += random.choice(combined_list)

    temp_list = random.sample(temp_list, len(temp_list))

    password = ''.join(temp_list)

    print(f"Your generated password is: {password}")

main()
