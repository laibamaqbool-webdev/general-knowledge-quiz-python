"""
====================================================================
 DecodeLabs - Python Programming Industrial Training Kit
 Project 4 : The General Knowledge Quiz
====================================================================

Project Goal
------------
Develop a simple General Knowledge Quiz application using Python.

The program will:
1. Ask the user three General Knowledge questions.
2. Compare the user's answers with the correct answers.
3. Award one point for each correct answer.
4. Display the final score at the end.
5. Show the user's overall performance.

Python Concepts Used
--------------------
* Variables
* Lists
* Functions
* Loops
* If-Else Statements
* String Methods
* Input Validation
* Score Tracking
* f-Strings

Author : Laiba Maqbool
Batch  : DecodeLabs Industrial Training 2026
====================================================================
"""


# ============================================================
#                 WELCOME SCREEN
# ============================================================

def display_welcome():

    print("=" * 65)
    print("          WELCOME TO THE GENERAL KNOWLEDGE QUIZ")
    print("=" * 65)

    print("\nHello!")
    print("This quiz contains three General Knowledge questions.")
    print("Each correct answer gives you ONE point.")
    print("Your final score will be displayed at the end.")

    print("\nGood Luck!")
    print("=" * 65)


# ============================================================
#                   QUIZ RULES
# ============================================================

def display_rules():

    print("\nQUIZ RULES")
    print("-" * 65)

    print("1. There are only 3 questions.")
    print("2. Every correct answer gives 1 point.")
    print("3. Wrong answers give 0 points.")
    print("4. Uppercase and lowercase letters do not matter.")
    print("5. Extra spaces are automatically ignored.")
    print("6. Try to answer all questions correctly.")

    print("-" * 65)


# ============================================================
#               PLAYER INFORMATION
# ============================================================

def get_player_name():

    while True:

        name = input("\nEnter Your Name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        else:
            return name.title()


# ============================================================
#              QUIZ COUNTDOWN
# ============================================================

def countdown():

    print("\nGet Ready!")

    print("3...")
    print("2...")
    print("1...")

    print("\nQuiz Started!")
    print("=" * 65)


# ============================================================
#              ASK A SINGLE QUESTION
# ============================================================

def ask_question(question, correct_answers):

    """
    This function asks one question,
    accepts user input,
    checks the answer,
    and returns True or False.
    """

    user_answer = input(question + "\nYour Answer: ")

    cleaned_answer = user_answer.strip().lower()

    if cleaned_answer in correct_answers:

        print("Correct Answer! ")

        return True

    else:

        print("Wrong Answer! ")
        print(f"Correct Answer: {correct_answers[0].title()}")

        return False


# ============================================================
#                  MAIN QUIZ FUNCTION
# ============================================================

def run_quiz():

    score = 0

    correct_count = 0

    wrong_count = 0

    total_questions = 3

    display_welcome()

    player_name = get_player_name()

    print(f"\nWelcome, {player_name}!")

    display_rules()

    input("\nPress Enter to Start the Quiz...")

    countdown()

    questions = [

        (
            "Q1. What is the capital city of France?",
            ["paris"]
        ),

        (
            "Q2. Which planet is known as the Red Planet?",
            ["mars"]
        ),

        (
            "Q3. What is the largest ocean on Earth?",
            ["pacific", "pacific ocean"]
        )

    ]

    question_number = 1

    for question, answer in questions:

        print(f"\nQuestion {question_number} of {total_questions}")
        print("-" * 65)

        if ask_question(question, answer):

            score += 1
            correct_count += 1

        else:

            wrong_count += 1

        print(f"\nCurrent Score : {score}/{question_number}")

        question_number += 1

        # ============================================================
    #           CALCULATE QUIZ RESULT
    # ============================================================

    percentage = (score / total_questions) * 100

    if percentage == 100:
        grade = "A+"
        remark = "Outstanding! Excellent General Knowledge."

    elif percentage >= 80:
        grade = "A"
        remark = "Excellent Work! Keep it up."

    elif percentage >= 60:
        grade = "B"
        remark = "Very Good! You have good knowledge."

    elif percentage >= 40:
        grade = "C"
        remark = "Good Attempt! Practice a little more."

    else:
        grade = "D"
        remark = "Needs Improvement. Keep Learning."

    # ============================================================
    #                  DISPLAY RESULT
    # ============================================================

    print("\n")
    print("=" * 65)
    print("                    QUIZ COMPLETED")
    print("=" * 65)

    print(f"Player Name      : {player_name}")
    print(f"Total Questions  : {total_questions}")
    print(f"Correct Answers  : {correct_count}")
    print(f"Wrong Answers    : {wrong_count}")
    print(f"Final Score      : {score}/{total_questions}")
    print(f"Percentage       : {percentage:.2f}%")
    print(f"Grade            : {grade}")

    print("=" * 65)

    # ============================================================
    #            PERFORMANCE MESSAGE
    # ============================================================

    print("\nPerformance Report")
    print("-" * 65)

    print(remark)

    if score == total_questions:

        print("You answered every question correctly.")
        print("Fantastic Performance!")

    elif score == 2:

        print("Only one answer was incorrect.")
        print("Almost Perfect!")

    elif score == 1:

        print("You answered one question correctly.")
        print("Keep practicing to improve.")

    else:

        print("Don't worry.")
        print("Learning comes with practice.")

    print("-" * 65)

    # ============================================================
    #               QUIZ SUMMARY
    # ============================================================

    print("\nQuiz Summary")
    print("-" * 65)

    print(f"Player : {player_name}")
    print(f"Score  : {score}/{total_questions}")

    if score == total_questions:

        print("Status : PASS WITH EXCELLENT PERFORMANCE")

    elif score >= 2:

        print("Status : PASS")

    else:

        print("Status : KEEP PRACTICING")

    print("-" * 65)

    print("\nThank you for playing the General Knowledge Quiz.")
    print("We hope you enjoyed this small learning activity.")
    print("=" * 65)


# ============================================================
#              PLAY AGAIN FUNCTION
# ============================================================

def play_again():

    while True:

        choice = input("\nWould you like to play again? (Y/N): ")

        choice = choice.strip().lower()

        if choice == "y":

            return True

        elif choice == "n":

            return False

        else:

            print("Invalid Choice! Please enter Y or N.")


# ============================================================
#                    MAIN PROGRAM
# ============================================================

def main():

    while True:

        run_quiz()

        if play_again():

            print("\nStarting a New Quiz...\n")

        else:

            print("\nThank You for Using This Program.")

            print("Good Bye!")

            print("=" * 65)

            break


# ============================================================
#                  PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()