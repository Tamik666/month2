import random
from colorama import init, Fore, Style
from art import tprint

init(autoreset=True)

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'algorithm']
    return random.choice(words)


def display_hangman(tries):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    stages = [
        """
           ------
           |    |
           |    
           |    
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        -----
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        -----
        """
    ]
    color = colors[6 - tries]
    return color + stages[tries]


def play_game():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    tprint("давайте играть в виселицу", font="random")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Введите букву или слово целиком: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(Fore.BLUE + f"Вы уже угадывали букву {guess}.")
            elif guess not in word:
                print(Fore.RED + f"Буквы {guess} нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(Fore.GREEN + f"Отлично! Буква {guess} есть в слове!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(Fore.BLUE + f"Вы уже угадывали слово {guess}.")
            elif guess != word:
                print(Fore.RED + f"Слово {guess} не верно.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Некорректный ввод.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        tprint("You Win!", font="random")
    else:
        tprint("Game Over", font="random")
        print(f"Вы не угадали слово. Загаданное слово было {word}. Возможно, повезет в следующий раз!")


if __name__ == "__main__":
    play_game()
