# File Name : main.py
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


from functionPackage.function import *

if __name__ == "__main__":

    for i in range(10, 2000000000):           #technically all prime numbers 1-10 meet requirements but 
        if all_permutations_are_prime(i):
            print(i)