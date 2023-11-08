import random

#This method replace the @new_character, in @original_string, at position @pos
#string[i] = "a" does not work in python
def get_replace_string_character_at(pos, new_character, original_string):
    string_list = list(original_string)
    string_list[pos] = new_character
    
    return ''.join(string_list)

def generate_initial_number():
    return str(random.randint(1000,9999))

def generate_new_digit():
    return str(random.randint(0,9))

#Check if a digit is not found repeating in a number
#Example: is_digit_repeated(2, 2236) return True
#Example: is_digit_repeated(6, 2236) return False
def is_digit_repeated(digit, number):
    return number.count(digit) > 1

#Check if the first digit is not zero
def is_digit_valid(string_number):
    if int(string_number[0]) == 0:
        return False
    return True

#This method should return a digit that is unique in the parameter @number
def get_unique_digit(i, number):
    copy_of_number = number

    if not is_digit_repeated(copy_of_number[i], copy_of_number) and is_digit_valid(copy_of_number):
        return copy_of_number[i]
    
    new_digit = copy_of_number[i]

    while is_digit_repeated(new_digit, copy_of_number) or not is_digit_valid(copy_of_number):
        new_digit = generate_new_digit()

        copy_of_number = get_replace_string_character_at(i, new_digit, copy_of_number)
    
    return new_digit
    

#This method will return the final number, with each digit unique. 
def get_final_generated_number(initial_generated_number):
    final_generated_number = initial_generated_number
    
    for i in range(len(final_generated_number)):
        final_generated_number = get_replace_string_character_at(i, get_unique_digit(i, final_generated_number), final_generated_number)
         
    return final_generated_number
    

def generate_different_digit_number():
    initial_generated_number = generate_initial_number()

    return get_final_generated_number(initial_generated_number)
    