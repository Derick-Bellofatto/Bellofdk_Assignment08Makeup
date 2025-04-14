# File Name : functions.py
# Student Name: Derick Bellofatto
# email:  Bellofdk@mail.uc.edu
# Assignment Number: Assignmen 08 Makeup
# Due Date:   4/13/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Makeup assignment for Assignment 08 - Finds all permutations of a digit between 1 and 2 billion

# Brief Description of what this module does: Calls the function to list all permutations that are prime
# Citations: ChatGPT 4.0, https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python, https://stackoverflow.com/questions/64893074/function-to-check-if-number-is-a-prime-number

# Anything else that's relevant: Validated permutations up to 200,000, but 2 billion will take a while to run. The code is currently configured to run up to 2 billion

#SOURCE 1: https://stackoverflow.com/questions/64893074/function-to-check-if-number-is-a-prime-number
#SOURCE 2: https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python

import itertools
import numbers



#SOURCE 1
def is_prime(number):
    '''
    Checks if a number is prime or not
    @number: number being checked (whether it is prime or not)
    @return: Boolean, returns true if Prime, False otherwise
    '''
    if number >= 2:
        for i in range(2, number):
            if not (number % i):
                return False
        return True
    else:
        return False


#SOURCE 2
def get_permutations(number):
    '''
    Returns all different permutations of a number
    @number: number being inputted
    @return: list of all different permutations of the number
    '''
    digits = str(number)
    digit_sets = itertools.permutations(digits) #get all permutations of the digits

    numbers = []                                #list to store correct digits
    for digits in digit_sets:
        joined = ''.join(digits)  
        number_list = int(joined)               #convert the string to an integer
        numbers.append(number_list)             #add it to the list
    return set(numbers)                         #returns it as a set so there are no dupicates


def all_permutations_are_prime(number):
    '''
    Checks and lists all completely prime permutations
    @number: number being checked
    @return: Boolean, if true prints the number/permutations to the terminal via get_permutations function
    '''
    if not is_prime(number):                    #makes sure the initial number is prime    
        return False  
    for permutations in get_permutations(number): #checks all the permutations of the original prime nubmer
        if not is_prime(permutations):
            #print("checked, but not prime")
            return False                        #if any of the permutations are not prime, return false
    return True
