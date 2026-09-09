
from core.common_passwords import is_common_password

def analyze_password(password):

    result = {
        "length": check_length(password),
        "complexity": check_complexity(password),
        "common_password": check_common_password(password),
        "repetition": check_repetition(password),
        "sequence": check_sequence(password)
    }
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

def check_repetition(password):
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True
    return False

def check_sequence(password):
    password = password.lower()

    for i in range(len(password)-2):
        first = ord(password[i])
        second = ord(password[i+1])
        third = ord(password[i+2])

        if second == first +1 and third == second +1:
            return True

        if second == first -1 and third == second -1:
            return True
    return False




