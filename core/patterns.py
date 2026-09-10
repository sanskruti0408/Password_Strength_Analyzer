def check_repetition(password):
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True
    return False

def check_sequence(password):
    password = password.lower()

    for i in range(len(password)-2):
        first = password[i]
        second = password[i+1]
        third = password[i+2]

        if first.isalpha() and second.isalpha() and third.isalpha():
            
            if ord(second) == ord(first) +1 and ord(third) == ord(second) +1:
                return True

            if ord(second) == ord(first) -1 and ord(third) == ord(second) -1:
                return True

        elif first.isdigit() and second.isdigit() and third.isdigit():

            if int(second) == int(first) +1 and int(third) == int(second) +1:
                return True

            if int(second) == int(first) -1 and int(third) == int(second) -1:
                return True
    return False

def check_predictability(password):
    weak_words = [
        "password",
        "welcome",
        "admin",
        "login",
        "hello",
        "qwerty",
        "letmein"
    ]

    password_lower = password.lower()

    for word in weak_words:
        if word in password_lower:
            return True

    return False

def check_keyboard_pattern(password):
    keyboard_patterns = [
        "qwerty",
        "asdfgh",
        "zxcvbn",
        "qwertyui",
        "asdfghjk",
        "zxcvbnm",
        "!@#$%^&*",
        "0987654321"
        ]

    password_lower = password.lower()

    for pattern in keyboard_patterns:
        if pattern in password_lower:
            return True
    return False

print(check_repetition("11111111"))
print(check_sequence("12345678"))
print(check_predictability("Password123!"))
print(check_keyboard_pattern("qwerty123"))
print(check_keyboard_pattern("K7@mQ2!vR9"))
