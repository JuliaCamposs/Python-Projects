''''
Functions needed: 

has_uppercase(password)     → checks for uppercase letters
has_lowercase(password)     → checks for lowercase letters
has_number(password)        → checks for numbers
has_special_char(password)  → checks for special characters (!@#$ etc)
is_long_enough(password)    → checks if length >= 8
check_strength(password)    → calls ALL the above and gives a score

'''


# step 1

def has_uppercase(password):
    for char in password:     # checking each character in password
        if char.isupper():
            return True
    return False

# step 2 

def has_lowercase(password):
    for char in password:
        if char.islower():
            return True 
    return False 

# step 3 

def has_number(password):
    for num in password:
        if num.isdigit():   # check for digits from (0-9)
            return True 
    return False 

# step 4

def has_special_char(password):
    special_char = "!@#$%"
    for char in password:
        if char in special_char:
            return True 
    return False 
    
# step 5

def is_long_enough(password):
    if len(password) >= 8:
        return True 
        
# step 6

def check_strenght(password):
    score = 0 

    if has_uppercase(password) == True:
        score += 1

    if has_lowercase(password) == True:
        score += 1 
    
    if has_number(password) == True:
        score += 1

    if has_special_char(password) == True:
        score += 1

    if is_long_enough(password) == True:
        score += 1 

    if score <= 2:
        return "Weak password"
    if score == 3 or score == 4:
        return "Medium password"
    if score == 5:
        return "Strong password"
    
def main():
    password = input("Enter your password: ")
    result = check_strenght(password)
    print("Your password is: ", result)



    






