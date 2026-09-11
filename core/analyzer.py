from core.common_passwords import is_common_password
from core.correlation import calculate_correlation_score
import math
from core.patterns import (
    check_repetition,
    check_sequence,
    check_predictability,
    check_keyboard_pattern
)

def analyze_password(password):
    result = {
        "length": check_length(password),
        "complexity": check_complexity(password),
        "common_password": check_common_password(password),
        "repetition": check_repetition(password),
        "sequence": check_sequence(password),
        "predictability": check_predictability(password),
        "keyboard_pattern": check_keyboard_pattern(password)
    }

    result["score"] = calculate_score(password)

    return result

def analyze_password(password):

    result = {
        "length": check_length(password),
        "complexity": check_complexity(password),
        "common_password": check_common_password(password),
        "repetition": check_repetition(password),
        "sequence": check_sequence(password),
        "predictability": check_predictability(password)
        }
    result["score"] = calculate_score(password)
    return result

def check_length(password):
    length = len(password)
    
    if length <6 :
        return "Very Weak"
    
    elif length <=7 :
        return "Weak"

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

def calculate_entropy(password):
    length = len(password)

    if length == 0:
        return 0

    pool_size = 0

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_symbol = False

    for char in password :
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True

    if has_uppercase:
        pool_size += 26
    if has_lowercase:
        pool_size += 26
    if has_digit:
        pool_size +=10
    if has_symbol :
        pool_size +=32
    if pool_size == 0:
        return 0

    entropy = length * math.log2(pool_size)

    return entropy


def check_common_password(password):
    return is_common_password(password)

            
def calculate_score(result):
    score = 0

    length_rating = result["length"]

    if length_rating == "Strong":
        score += 32
    elif length_rating == "Good":
        score += 22
    elif length_rating == "Fair":
        score += 15
    elif length_rating == "Weak":
        score += 8

    complexity = result["complexity"]

    for category in complexity.values():
        if category:
            score += 6

    if result["predictability"]:
        score -= 20

    if result["repetition"]:
        score -=10

    if result["sequence"]:
        score -=10

    score = max(0, min(score, 100))

    return score


def calculate_length_score(password):
    length = len(password)

    if length < 6:
        return 0
    elif length <= 7:
        return 5
    elif length <= 9:
        return 10
    elif length <= 11:
        return 15
    elif length <= 13:
        return 20
    elif length <= 15:
        return 23
    else:
        return 25

    
def calculate_unpredictability_score(password):
    score = 0

    if not check_predictability(password):
        score += 15

    if not check_keyboard_pattern(password):
        score += 8

    if not check_sequence(password):
        score += 6

    if not check_repetition(password):
        score += 6

    return score


def calculate_complexity_score(complexity):
    score = 0

    if complexity["uppercase"]:
        score += 5
    if complexity["lowercase"]:
        score += 5
    if complexity["digit"]:
        score += 5
    if complexity["symbol"]:
        score += 5

    return score

def calculate_score(password):
    length_score = calculate_length_score(password)

    complexity_score = calculate_complexity_score(
        check_complexity(password)
    )

    unpredictability_score = calculate_unpredictability_score(password)

    common_password_score = (
        0 if check_common_password(password) else 20
    )

    score = (
        length_score
        + complexity_score
        + unpredictability_score
        + common_password_score
    )

    if check_predictability(password):
        score -= 30

    if check_keyboard_pattern(password):
        score -= 15

    if check_sequence(password):
        score -= 10

    if check_repetition(password):
        score -= 15

    if check_common_password(password):
        score -= 20
        
    result = {
        "length": check_length(password),
        "complexity": check_complexity(password),
        "common_password": check_common_password(password),
        "repetition": check_repetition(password),
        "sequence": check_sequence(password),
        "predictability": check_predictability(password),
        "keyboard_pattern": check_keyboard_pattern(password)
    }

    score += calculate_correlation_score(result)
    

    return max(0, min(score, 100))
    
def calculate_entropy_score(entropy):
    if entropy < 20:
        return 0
    elif entropy < 30:
        return 5
    elif entropy < 40:
        return 8
    elif entropy < 50:
        return 11
    elif entropy < 60:
        return 14
    elif entropy < 70:
        return 17
    else:
        return 20
        






