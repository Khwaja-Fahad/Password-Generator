import string
import random

lower_alphabet = string.ascii_lowercase
# print(lower_alphabet)

upper_alphabet = string.ascii_uppercase
# print(upper_alphabet)

digits = string.digits
# print(digits)

punctuation = string.punctuation
# print(punctuation)

generated_pass = []

while True:
    pass_length = input("Please enter password length: ")

    if pass_length.isdigit() and int(pass_length) >= 0:
        pass_length = int(pass_length)
        generated_pass.extend(list(lower_alphabet))
        generated_pass.extend(list(upper_alphabet))
        generated_pass.extend(list(digits))
        generated_pass.extend(list(punctuation))

        if pass_length > len(generated_pass):
            print("Password length exceeds the available characters.")
        else:
            random.shuffle(generated_pass)
            password = "".join(random.sample(generated_pass, pass_length))
            print("Generated password:", password)
        break
    elif not pass_length.isdigit():
        generated_pass.extend(list(lower_alphabet))
        generated_pass.extend(list(upper_alphabet))
        
        if len(generated_pass) == 0:
            print("No alphabets available for password generation.")
        else:
            random.shuffle(generated_pass)
            password = "".join(random.sample(generated_pass, len(generated_pass)))
            print("Generated password:", password)
        break
    else:
        print("Please enter a non-negative integer!")
