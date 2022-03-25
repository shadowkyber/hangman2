import random


def stats():
    print(f"You won: {win} times.")
    print(f"You lost: {lose} times.")


def game():
    lives = 8
    word = list(random.choice(words))  # randomly selects a word to be guesses (java)
    guessed = list("-" * len(word))  # guessed letters (----)
    wrong = set()  # wrong guesses made
    w = set(word)  # letters in word (ajv)

    print()
    print("".join(guessed))
    letter = input("Input a letter: ")  # gets the users guess

    while lives:  # game
        if len(letter) != 1:  # if letter is longer than 1 letter
            print("Please, input a single letter.")
        elif letter not in alph:  # if letter isn't a lowercase English letter
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in w or letter in wrong:  # if letter guessed was/is in word or has already been guessed
            if letter not in word:  # if letter has already been guessed
                print("You've already guessed this letter.")
                wrong.add(letter)  # adds letter to the wrong/already guessed set
            while letter in word:
                n = word.index(letter)  # gets the first index of letter
                guessed.pop(n)  # removes - from guessed
                guessed.insert(n, letter)  # replaces the - with the letter guessed
                word.insert(n, "-")  # inserts - into word
                word.remove(letter)  # removes the letter that was guessed
        else:
            print("That letter doesn't appear in the word.")  # if the guess is wrong
            lives -= 1
            wrong.add(letter)  # adds letter to wrong list

        if word.count("-") == len(word):  # if word is fully guessed
            print(f"You guessed the word {''.join(guessed)}!")
            print("You survived!")
            return "win"
        elif lives != 0:  # if the player hasn't run out of lives
            print()
            print("".join(guessed))
            letter = input("Input a letter: ")

    else:
        print()
        print("You lost!")
        return "lose"


def menu():
    return input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')


print("H A N G M A N")

words = ['python', 'java', 'swift', 'javascript']  # potential words
alph = set("qwertyuiopasdfghjklzxcvbnm")  # lowercase English alphabet
win = 0  # number of times user has won
lose = 0  # number of times user has won

select = menu()
while select != "exit":
    if select == "play":
        if game() == "win":
            win += 1
        else:
            lose += 1
    elif select == "results":
        stats()
    select = menu()
