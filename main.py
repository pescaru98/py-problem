

import random

def generate_initial_number():
    return str(random.randint(1000,9999))

def generate_new_digit():
    return str(random.randint(0,9))

def is_digit_repeated(digit, number):
    return number.count(digit) > 1

#This method should return a digit that is unique in parameter number
#Example: 4442
def get_unique_digit(i, number):
    print(type(i))
    if not is_digit_repeated(number[i], number):
        return number[i]
    
    new_digit = number[i]

    while(is_digit_repeated(new_digit, number)):
        new_digit = generate_new_digit();
    
    return new_digit
    

#This method will return the final number, with each digit unique. 
#initial_generated_number ex: 4421
#final_generated_number ex: 9821
def get_final_generated_number(initial_generated_number):
    final_generated_number = initial_generated_number
    for i in range(len(final_generated_number)):
        final_generated_number[i] = get_unique_digit(i, final_generated_number)
        
    return final_generated_number
    

def generate_different_digit_number():
    initial_generated_number = generate_initial_number()
    
    return get_final_generated_number(initial_generated_number)
    
    
print(generate_different_digit_number())
