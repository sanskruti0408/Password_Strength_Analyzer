def calculate_correlation_score(result):
    correlation_score = 0

    if result["predictability"] and any(result["complexity"].values()):
        correlation_score -= 10

    if result["predictability"] and result["sequence"]:
        correlation_score -= 10

    if result["keyboard_pattern"] and result["sequence"]:
        correlation_score -= 8

    if result["repetition"] and result["length"] in (
        "Strong",
        "Very Strong"
    ):
        correlation_score -= 10

    if result["common_password"] and any(result["complexity"].values()):
        correlation_score -= 10

    weakness_count = sum([
        result["predictability"],
        result["keyboard_pattern"],
        result["sequence"],
        result["repetition"],
        result["common_password"]
    ])

    if weakness_count >= 3:
        correlation_score -= 10

    if (
        result["length"] in ("Strong", "Very Strong")
        and sum(result["complexity"].values()) >= 3
        and not result["predictability"]
        and not result["keyboard_pattern"]
        and not result["sequence"]
        and not result["repetition"]
        and not result["common_password"]
    ):
        correlation_score += 10

    return correlation_score
