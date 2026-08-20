import json
import os

# Load questions from the JSON dataset
def load_questions(filepath="questions.json"):
    if not os.path.exists(filepath):
        print(f"Error: Could not find '{filepath}'.")
        return []
    
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

# Run a single quiz round
def run_quiz(questions):
    score = 0
    total = len(questions)

    for index, item in enumerate(questions, start=1):
        print(f"Question {index}: {item['question']}")
        for key, value in item["options"].items():
            print(f"  {key}) {value}")

        # Input validation loop
        valid_options = list(item["options"].keys())
        while True:
            choice = input("Your answer: ").strip().upper()
            if choice in valid_options:
                break
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

        # Check answer
        if choice == item["answer"].upper():
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Incorrect! Correct answer was {item['answer']}.\n")

    # Score and percentage calculation
    percentage = (score / total) * 100
    print("=" * 30)
    print("Quiz Finished!")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.1f}%")
    print("=" * 30 + "\n")

# Main program flow with replay loop
def main():
    questions = load_questions()
    if not questions:
        return

    print("=== QUIZ APPLICATION ===\n")

    while True:
        run_quiz(questions)

        # Replay prompt with validation
        while True:
            replay = input("Do you want to play again? (y/n): ").strip().lower()
            if replay in ["y", "yes", "n", "no"]:
                break
            print("Invalid input. Enter 'y' for yes or 'n' for no.")

        if replay in ["n", "no"]:
            print("Thanks for playing! Goodbye.")
            break
        print("\nStarting new game...\n")

if __name__ == "__main__":
    main()
