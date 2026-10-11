def check_password(password):
    score = 0
    missing = []

    if len(password) >= 8:
        score += 1
    else:
        missing.append("At least 8 characters long")

    if any(char.isupper() for char in password):
        score += 1
    else:
        missing.append("At least one uppercase letter")

    if any(char.islower() for char in password):
        score += 1
    else:
        missing.append("At least one lowercase letter")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        missing.append("At least one number")

    if any(not char.isalnum() for char in password):
        score += 1
    else:
        missing.append("At least one special character")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, missing

password = input("Enter your password: ")
strength, missing_reqs = check_password(password)

print(f"\nPassword Strength: {strength}")

if missing_reqs:
    print("Missing Requirements:")
    for req in missing_reqs:
        print(f"  - {req}")
else:
    print("Great job! All security requirements are met.")