import re

def analyze_password(password):
    score = 0
    suggestions = []

    try:
        with open("common_passwords.txt", "r") as file:
            common_passwords = [line.strip().lower() for line in file]
    except FileNotFoundError:
        common_passwords = []

    if password.lower() in common_passwords:
        return {
            "rating": "Weak",
            "score": 0,
            "suggestions": [
                "This is a very common password.",
                "Choose a unique password."
            ]
        }

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character.")

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return {
        "rating": rating,
        "score": score,
        "suggestions": suggestions
    }