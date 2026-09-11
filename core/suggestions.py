def generate_suggestions(result):
    suggestions = []

    if result["length"] in ("Very Weak", "Weak", "Fair"):
        suggestions.append("Increase password length.")

    complexity = result["complexity"]

    if not complexity["uppercase"]:
        suggestions.append(
            "Add uppercase letters."
        )

    if not complexity["lowercase"]:
        suggestions.append(
            "Add lowercase letters."
        )

    if not complexity["digit"]:
        suggestions.append(
            "Add numbers."
        )

    if not complexity["symbol"]:
        suggestions.append(
            "Add special characters."
        )

    if result["common_password"]:
        suggestions.append(
            "Avoid commonly used passwords."
        )

    if result["predictability"]:
        suggestions.append(
            "Avoid predictable words or common password patterns."
        )

    if result["keyboard_pattern"]:
        suggestions.append(
            "Avoid keyboard patterns such as qwerty or asdf."
        )

    if result["sequence"]:
        suggestions.append(
            "Avoid ascending or descending sequences."
        )

    if result["repetition"]:
        suggestions.append(
            "Avoid repeated characters."
        )

    if not suggestions:
        suggestions.append(
            "Password has no major detected weaknesses."
        )

    return suggestions
