import random

ui_choices = ["Play", "Menu", "Options", "Exit"]

print("\nWelcome to EduQuest! Where it's fun learning")

while True:
    user_answer = str(input("Choose one of the following options: Play, Menu, Options: ")).capitalize()
    
    if user_answer == "Play":
        print("Wonderful! \nGame Starting....")
        break
    elif user_answer == "Menu" or user_answer == "Options":
        print(f"You chose {user_answer}.")
        break
    else:
        print('Invalid choice. Please try again.')

# Define the dictionary of banned words
banned_words = {
    "word_1": "fox",
    "word_2": "is",
    "word_3": "good"
}

# Function to split a sentence into words and store them in a dictionary
def store_sentence_in_dict(sentence):
    # Split the sentence into words and convert to lowercase
    words = sentence.lower().split()
    
    # Create a dictionary to store the words
    word_dict = {}
    
    # Iterate through the words and store them in the dictionary
    for i, word in enumerate(words):
        word_dict[f"word_{i+1}"] = word
    
    return word_dict

# Function to check if any words in the user's dictionary are in the banned words dictionary
def check_for_banned_words(user_input_dict, banned_words):
    found_banned_words = []  # Initialize list to store found banned words
    
    for key, word in user_input_dict.items():
        if word in banned_words.values():
            found_banned_words.append(word)  # Append banned word to the list
    
    if found_banned_words:
        print(f"{', '.join(found_banned_words)}")
        return True
    else:
        return False

# Function to select a random word from the user's input excluding banned words
def select_random_word(user_input_dict, banned_words):
    # Filter out banned words
    non_banned_words = [word for word in user_input_dict.values() if word not in banned_words.values()]
    
    if non_banned_words:
        # Select a random word from non-banned words
        random_word = random.choice(non_banned_words)
        return random_word
    else:
        return None

# User input
sentence = input("Enter a sentence: ")

# Store the user's input in a dictionary
user_input_dict = store_sentence_in_dict(sentence)

# Check if any banned words are present in the user's input
if check_for_banned_words(user_input_dict, banned_words):
    print("Your input contains banned words!")
else:
    print("Your input is clean!")

# Select a random non-banned word from the user's input
random_word = select_random_word(user_input_dict, banned_words)

user_final_answer = input("What is the missing word?: ")

if user_final_answer == random_word:
    print('You are absolutely correct!')
else:
    print('You are Wrong:( ')

