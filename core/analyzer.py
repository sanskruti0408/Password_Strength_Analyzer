
from core.common_passwords import is_common_password

def analyze_password(password):

    result = {}
    return result

def check_length(password):
    length = len(password)
    
    if length <6 :
        return "very weak"
    
    elif length <=7 :
        return "weak"

    elif length <=9 :
        return "Fair"

    elif length <=11 :
        return "Good"

    elif length <=15 :
        return "Strong"

    else :
        return "Very Strong"

def check_complexity(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_uppercase = True

        elif char.islower():
            has_lowercase = True

        elif char.isdigit():
            has_digit = True

        else:
            has_symbol = True


    return{
            "uppercase": has_uppercase,
            "lowercase": has_lowercase,
            "digit": has_digit,
            "symbol": has_symbol
            }

def check_common_password(password):
    return is_common_password(password)






