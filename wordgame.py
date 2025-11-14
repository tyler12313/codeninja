from random import shuffle
def scramble_word(word):
    letter_list = list(word)
    shuffle(letter_list)
    scrambled = "".join(letter_list)
    return scrambled
    

def load_words_from_file(filename):
    word_list = []
    try:
        with open (filename, 'r') as file:
            for line in file:
                word = line.strip().lower()
                if word:
                    word_list.append(word)
        print(f"Loaded {len(word_list)} words from {filename}")
        return word_list
    except FileNotFoundError:
        print(f"Error: FIle '{filename}' not found.")
        return []
        
    
def play_game():
    score = 0
    
    shuffle(word_list)
    for word in word_list:
        mixed_word = scramble_word(word)
        print(f"\nUnscramble this word: {mixed_word}")
        
        guess = input("Your answer: ")
        
        if guess == word:
            print("Correct! +1 point!")
        else:
            print(f"Sorry, the word was {word}")
            
    print(f"\nGame Over! Final score: {score}")

difficulty = input("Normal mode or hard mode")
if difficulty == "normal":
    word_list = load_words_from_file("word_list")
if difficulty == "hard":
    word_list = load_words_from_file("hard_word_list")
    
play_game()
