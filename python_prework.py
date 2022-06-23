# --- QUESTION 1 ---
# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function.
def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")


# --- QUESTION 2 ---
# Write a python function, first_odds that prints
#   the odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(101):
        if num % 2 == 1:
            print(num)


# --- QUESTION 3 ---
# Please write a Python function, max_num_in_list 
#   to return the max number of a given list. 
def max_num_in_list(a_list):
    return max(a_list)


# --- QUESTION 4 ---
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
#   unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 100 == 0:
        if a_year % 400 == 0:
            return True
        else: 
            return False
    else:
        return False


# --- QUESTION 5 ---
# Write a function to check to see if all numbers in list 
#   are consecutive numbers. For example, [2,3,4,5,6,7] are 
#   consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    while len(a_list) > 2:
        current_num = a_list.pop()
        if current_num - 1 == a_list[-1]:
            continue
        else:
            return False
    return True if a_list[0] + 1 == a_list[1] else False
