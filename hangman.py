import random
EASY_WORDS=["apple","house","water","music","chair","school","green","happy","river","light"]
MEDIUM_WORDS=["python","computer","database","developer","internet","software","keyboard","science","network","program"]
HARD_WORDS = ["algorithm","programming","cybersecurity","architecture","cryptography","artificial","intelligence","technology","development","debugging"]
HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]
def choose_difficulty():
    print("\nChoose your difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice=input("Enter 1, 2, or 3: ").strip()
        if choice=="1":
            return EASY_WORDS,1,"Easy"
        elif choice=="2":
            return MEDIUM_WORDS,1.5,"Medium"
        elif choice=="3":
            return HARD_WORDS,2,"Hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3")
def display_status(display_word,incorrect_guesses,guessed_letters,score,hints_remaining,difficulty_name):
    print("\n"+"="*45)
    print("HANGMAN")
    print("="*45)
    print(HANGMAN_STAGES[incorrect_guesses])
    print("Difficulty:",difficulty_name)
    print("Word:"," ".join(display_word))
    print("Incorrect guesses:",incorrect_guesses,"/ 6")
    print("Score:",score)
    if guessed_letters:
        print("Guessed letters:"," ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")
    print("Hints remaining:",hints_remaining)
    print("="*45)
def get_guess():
    while True:
        guess=input("Enter a letter or type 'hint': ").strip().lower()
        if guess=="hint":
            return guess
        if len(guess)!=1:
            print("Please enter exactly one letter")
            continue
        if not guess.isalpha():
            print("Please enter a letter, not a number or symbol")
            continue
        return guess
def use_hint(secret_word,display_word):
    hidden_positions=[]
    for position,letter in enumerate(display_word):
        if letter=="_":
            hidden_positions.append(position)
    if not hidden_positions:
        return None
    hint_position=random.choice(hidden_positions)
    hint_letter=secret_word[hint_position]
    display_word[hint_position]=hint_letter
    return hint_letter
def play_game():
    words,multiplier,difficulty_name=choose_difficulty()
    secret_word=random.choice(words)
    display_word=["_"]*len(secret_word)
    guessed_letters=[]
    incorrect_guesses=0
    score=0
    max_hints=2
    hints_used=0
    print("\nStarting a new game...")
    print("Difficulty:",difficulty_name)
    print("You have 6 incorrect guesses")
    print("You have 2 hints")
    print("Good luck!")
    while "_" in display_word and incorrect_guesses<6:
        display_status(display_word,incorrect_guesses,guessed_letters,score,max_hints-hints_used,difficulty_name)
        guess=get_guess()
        if guess=="hint":
            if hints_used>=max_hints:
                print("You have already used all your hints")
                continue
            hint_letter=use_hint(secret_word,display_word)
            if hint_letter:
                hints_used+=1
                score=max(0,score-10)
                print("Hint revealed the letter:",hint_letter)
                print("10 points deducted")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("Correct guess!")
            occurrences = 0
            for position,letter in enumerate(secret_word):
                if letter==guess:
                    display_word[position]=guess
                    occurrences+=1
            points=int(10*multiplier*occurrences)
            score+=points
            print("+"+str(points)+"points!")
        else:
            incorrect_guesses+=1
            score=max(0,score-5)
            print("Wrong guess!")
            print("5 points deducted")
    if "_" not in display_word:
        completion_bonus=int(20*multiplier)
        score+=completion_bonus
        print("\n"+"="*45)
        print("YOU WON!")
        print("="*45)
        print("The word was:",secret_word.upper())
        print("Completion bonus:",completion_bonus)
        print("Final score:",score)
        return True,score
    else:
        print("\n"+"="*45)
        print("GAME OVER")
        print("="*45)
        print(HANGMAN_STAGES[6])
        print("The word was:",secret_word.upper())
        print("Final score:",score)
        return False,score
def main():
    games_played=0
    games_won=0
    total_score=0
    best_score=0
    print("\n"+"="*50)
    print("WELCOME TO HANGMAN CHALLENGE")
    print("="*50)
    print("""Guess the hidden word one letter at a time.
Rules:
• You can make up to 6 incorrect guesses.
• Correct letters earn points.
• Wrong guesses cost 5 points.
• You get 2 hints per game.
• A hint costs 10 points.
• Completing the word gives a bonus.
• Harder difficulty gives higher scores.""")
    while True:
        won,score=play_game()
        games_played+=1
        total_score+=score
        if won:
            games_won+=1
        if score>best_score:
            best_score=score
        print("\n"+"="*45)
        print("YOUR STATISTICS")
        print("="*45)
        print("Games played:",games_played)
        print("Games won:",games_won)
        print("Games lost:",games_played-games_won)
        print("Total score:",total_score)
        print("Best score:",best_score)

        if games_played>0:
            win_rate=(games_won/games_played)*100
            print("Win rate:",round(win_rate,1),"%")
        print("="*45)
        while True:
            again=input("\nPlay again?(y/n):").strip().lower()
            if again=="y":
                break
            elif again=="n":
                print("\nThanks for playing Hangman!")
                print("Your best score:",best_score)
                print("See you next time!")
                return
            else:
                print("Please enter y or n.")
if __name__=="__main__":
    main()