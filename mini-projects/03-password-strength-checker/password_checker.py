import string

# Function to check password rules and calculate strength score
def check_password_strength(password):
    # Dictionary of rules and boolean results
    checks = {
        "At least 8 characters long": len(password) >= 8,
        "Contains uppercase letter": any(char.isupper() for char in password),
        "Contains lowercase letter": any(char.islower() for char in password),
        "Contains a digit": any(char.isdigit() for char in password),
        "Contains a special character": any(char in string.punctuation for char in password)
    }

    # Calculate score out of 5
    score = sum(checks.values())

    # Determine strength category
    if score == 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, checks, score

if __name__ == "__main__":
    rating, checks, score = check_password_strength("Pass123!")
    print(f"Overall Rating: {rating} ({score}/5)")
    for check, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f" [{status}] {check}")
