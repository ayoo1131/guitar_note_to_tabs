#validate_signup.py

def is_valid_username(username):
    if len(username) == 0:
        return "Please enter a valid username"

    if len(username) > 20:
        return "Username must be less than 20 characters"

    else:
        return None

def is_valid_password(password):
    #Password must have at least 8 characters. 
    #An upper-case letter, number, and a special character
    
    errorList=[]

    if len(password) < 8:
        errorList.append("Password must contain 8 or more characters")

    if not any(char.isdigit() for char in password):
        errorList.append("Password must contain 1 number")

    if not any(char.isupper() for char in password):
        errorList.append("Password must contain 1 upper case letter")

    if (password.isalnum() or len(password)==0):
        errorList.append("Password must contain 1 special character")

    return errorList
