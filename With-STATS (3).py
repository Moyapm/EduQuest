import random
import os
import re
import time
import sys

# Clear screen function
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def loading_animation(duration=3):
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration

    while time.time() < end_time:
        for frame in spinner:
            sys.stdout.write(f"\rLoading... {frame}")
            sys.stdout.flush()
            time.sleep(0.2)
    clear_screen()

def terms_and_agreement():
    print(f"{Colors.CYAN}\nEduQuest Terms and Agreement{Colors.RESET}")
    print(f"""{Colors.YELLOW}
1. User Responsibility:
   - The accuracy of input text (e.g., spelling, grammar) is the sole responsibility of the user.
   - The application does not verify or correct user-provided input. Ensure your entries are accurate.

2. Disclaimer on Bugs and Errors:
   - This application is provided as is. Bugs or errors may occasionally occur.
   - If you encounter any issues, please report them to Group 5, COET 1-A.

3. Output Accuracy:
   - The output generated by EduQuest depends entirely on the input provided. Unexpected results caused by incorrect input are not the application's fault.

4. Privacy Notice:
   - EduQuest does not store or transmit user input data. Please do not enter sensitive or personal information.

5. Usage Agreement:
   - By continuing to use EduQuest, you acknowledge that you understand and accept these terms.

Thank you for choosing EduQuest! We hope you enjoy your experience.
{Colors.RESET}""")

    input(f"{Colors.GREEN}\nPress Enter to return to the main menu.{Colors.RESET}")

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

# Introduction
Colors.WHITE
print(f"\n{Colors.GREEN}Welcome to EduQuest! Where learning is fun and interactive!{Colors.RESET} (Click 'Enter' to Continue)")
time.sleep(2)
print(f'''
{Colors.YELLOW}In this game:{Colors.RESET}
    - You'll input a question, simple sentence or a whole entire Paragraph! and decide how many words to hide     
''')

input()
print(f'''
    - {Colors.GREEN}Much better! Copy and Paste your entire reviewer or your preferred text{Colors.RESET} and the code will do the work for you!
      {Colors.RED}HOWEVER{Colors.RESET} make sure you have read our terms before continuing the game''')
input()
print('''Isn't this game handy?''')
input()
clear_screen()

print(f'''
    - Your goal is to {Colors.YELLOW}guess the missing words before you run out of health points!
{Colors.RESET}''')
input()

print(f'''
    - The {Colors.YELLOW}purpose of our code{Colors.RESET} is to make a reviewer out of your inputed text
      Consider it a fill in the blank question BUT you make the statement
      
      This will {Colors.YELLOW}challenge your memorization {Colors.RESET}upon your given topic text  ''')
input()
print(f'''
    - At any point during guessing, you can type {Colors.RED}'/exit'{Colors.RESET} to return to the main menu.
                                        Let's begin!''')
input()

banned_words = {
    "the", "is", "are", "on", "in", "at", "she", "he", "a", "an", "or", "for",
    "that", "this", "by", "was", "were", "they", "their", "there", "be", "with",
    "to", "from", "and", "but", "so", "yet", "I", "you", "it", "we", "have", 
    "has", "do", "can", "will", "said"
}

global No_no_words

def add_banned_words():
    global banned_words
    global No_no_words
    print(f''' {Colors.RED}*{Colors.RESET} Do you have certain words in your text that you want to {Colors.RED}exclude{Colors.RESET} from being blanked out?''')
    
    while True:
        user_input = input('''
    - If yes, type the words here separated by spaces (or press Enter to skip): ''').strip()

        if not user_input:
            print(f"\n{Colors.GREEN}No new words were added.{Colors.RESET}")
            time.sleep(2)
            loading_animation(2)
            clear_screen()
            break

        new_words = {word.strip().lower() for word in user_input.split() if word.strip()}
        
        if not new_words:
            clear_screen()
            print("No valid words were added. Please try again.")
            time.sleep(1)
            continue

        banned_words.update(new_words)
        No_no_words = [word for word in words if word not in banned_words]

        print("\nCurrent banned words:", ', '.join(sorted(banned_words)))
        loop = input('Do you approve of these banned words? Type "no" to modify or press Enter to approve: ').strip().lower()
        if loop == 'no':
            print("Please enter the words you want to add again.")
            continue
        elif loop == '':
            time.sleep(1)
            print("Approved! Proceeding...")
            break
        else:
            print("Invalid input. Please type 'no' to modify or press Enter to approve.")
            time.sleep(1)
            clear_screen()

def store_sentence_in_dict(sentence):
    global words, No_no_words
    words = re.findall(r'\b\w+\b|[^\w\s]', sentence.lower())
    No_no_words = [word for word in words if word not in banned_words]
    word_dict = {f"word_{i+1}": word for i, word in enumerate(words)}
    return word_dict

def display_sentence(sentence):
    return ' '.join(sentence)

def play_game():
    global No_no_words

    health = 5
    correct_streak = 0
    wrong_answers = 0
    highest_streak = 0

    user_input = input('''\nEnter the text that the code will use here (copy or paste, or manually type it): ''')
    word_dict = store_sentence_in_dict(user_input)

    add_banned_words()

    if not No_no_words:
        print(f"{Colors.RED}No eligible words to guess. Please enter a different sentence.{Colors.RESET}")
        return "ui"

    num_words_to_blank = int(input(f"How many words do you wish to blank out from your text? (Max: {len(No_no_words)}): "))
    num_words_to_blank = min(num_words_to_blank, len(No_no_words))

    selected_words = random.sample(No_no_words, num_words_to_blank)
    modified_sentence = words.copy()
    blanks_map = {word: i for word in selected_words for i in range(len(modified_sentence)) if modified_sentence[i] == word}
    
    for word in selected_words:
        modified_sentence[blanks_map[word]] = "_____"

    guessed_words = set()
    blanks = {word: word for word in selected_words}

    while blanks and health > 0:
        clear_screen()
        print("\nUpdated sentence:")
        print(display_sentence(modified_sentence))
        print(f"Health remaining: {health}")

        guess = input("\nGuess a missing word (or type '/exit' to quit to the main menu): ").strip()

        if guess == "/exit":
            print("\nExiting game and returning to the main menu...\n")
            time.sleep(1)
            clear_screen()
            return "ui"

        if guess in guessed_words:
            print(f"{Colors.YELLOW}You already guessed that word. Try another one.{Colors.RESET}")
            time.sleep(1)
            clear_screen()
            continue

        guessed_words.add(guess)

        if guess.lower() in blanks:
            index = blanks_map[guess.lower()]
            modified_sentence[index] = guess
            print(f"{Colors.GREEN}Correct!{Colors.RESET}")
            del blanks[guess.lower()]
            correct_streak += 1
            time.sleep(1)

             # Update the highest streak
            if correct_streak > highest_streak:
                highest_streak = correct_streak


        else:
            health -= 1
            wrong_answers += 1
            correct_streak = 0
            print(f"{Colors.RED}Incorrect! You lose a health point. Health remaining: {health}{Colors.RESET}")
            time.sleep(2)

    if health == 0:
        print(f"\n{Colors.RED}You've run out of health! Game over.{Colors.RESET}")
    else:
        print(f"\n{Colors.GREEN}Congratulations! You've guessed all the missing words.{Colors.RESET}")
    Colors.GREEN
    print("\nGame Summary:")
    print(f"Health remaining: {health}")
    print(f"Wrong answers: {wrong_answers}")
    print(f"Correct streak: {correct_streak}")
    print(f"Highest streak: {highest_streak}")
    print("\nWe hope you enjoyed Group Five's code!")
    Colors.RESET

    replay = input("Do you want to play again? Type 'yes' to replay or press Enter to return to the main menu: ").strip().lower()
    if replay == 'yes':
        return "replay"
    return "ui"

while True:
    user_answer = input("\nChoose one of the following options: Play, Policy, Options, Exit: ").capitalize()
    clear_screen()

    if user_answer == "Play":
        print("Wonderful! \nGame Starting....")
        if play_game() == "replay":
            continue
    elif user_answer in ["Menu", "Options"]:
        print(f"You chose {user_answer}. This feature is coming soon!")
        time.sleep(1)
        clear_screen()
        continue
    elif user_answer == "Policy":
        terms_and_agreement()
        clear_screen()
    elif user_answer == "Exit":
        print(f"{Colors.GREEN}Thank you for trying EduQuest! Goodbye!{Colors.RESET}")
        exit()
    else:
        print("Invalid choice. Please try again.")
