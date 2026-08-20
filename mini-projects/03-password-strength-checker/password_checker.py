import string

# Check password criteria and determine overall strength
def check_password_strength(password):
    checks = {
        "At least 8 characters long": len(password) >= 8,
        "Contains uppercase letter": any(char.isupper() for char in password),
        "Contains lowercase letter": any(char.islower() for char in password),
        "Contains a digit": any(char.isdigit() for char in password),
        "Contains a special character": any(char in string.punctuation for char in password)
    }

    # Calculate total criteria met
    score = sum(checks.values())

    # Assign rating based on score
    if score == 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, checks, score

# Interactive loop for user input
def main():
    print("=== PASSWORD STRENGTH CHECKER ===")
    print("Note: Entered passwords are evaluated in memory and never saved.\n")

    while True:
        password = input("Enter a password to check (or type 'exit' to quit): ").strip()

        if password.lower() == "exit":
            print("Goodbye!")
            break

        if not password:
            print("Password cannot be empty. Please try again.\n")
            continue

        rating, checks, score = check_password_strength(password)

        print(f"\nPassword Strength: {rating} ({score}/5)")
        print("Checklist:")
        for rule, passed in checks.items():
            status = "✓" if passed else "✗"
            print(f"  [{status}] {rule}")
        print("-" * 40 + "\n")

if __name__ == "__main__":
    main()
