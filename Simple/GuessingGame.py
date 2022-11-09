import random

secret_words = ['tree', 'sun', 'ball', 'moon', 'earth', 'grass', 'world']
secret_word = random.choice(secret_words)
guessed_words = ""
turns = 20
while turns > 0:
    failed = 0
    for char in secret_word:
        if char in guessed_words:
            print(char, end=" ")
        else:
            print("_")
            print(char, end=" ")
            failed += 1

    if failed == 0:
        print("You win!")
        print("You guessed it! The word was:", secret_word)
        break

    print()
    guess = input("Please enter a letter to guess: ")

    guessed_words = guess
    if guess not in secret_word:
        turns -= 1
        print("Wrong")
        print("1 less turns to guess", +turns)

        if turns == 0:
            print("You lost!")
