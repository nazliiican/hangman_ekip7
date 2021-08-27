import colorama
from network import x
from images import images
from colorama import Fore, Style, Back
colorama.init(autoreset=True)


#intro
print(f"{Fore.RED}Welcome the to Hangman!".center(80))
print()

print(f"""{Fore.GREEN}Game Modes:
1- Player vs Player
2- Player vs AI
""")


#choosing word
while True:
    opt = int(input("Please select a game mode: "))
    if opt in [1, 2]:
        if opt == 1:

            while True:
                word = str(input(f"{Style.DIM}Please enter a word: ")).lower()
                if word.isalpha():
                    print()
                    print("Word has been confirmed. Let' s begin!")
                    print()
                    break
                else:
                    print()
                    print(f"{Style.BRIGHT}Please enter a valid word.(no numbers or special characters.)")
            break
        else:
            word = x
            break
    else:
        print()
        print(f"{Fore.RED}Option must be 1 or 2!")

        
#engine
count = 0
hidden_word = ("_"  + " ")* len(word)

print("Word:" + " ", hidden_word)


correct_letters = []
wrong_letters = []

while count <= 7:
    unlocked_word = ""
    guess = str(input(f"{Fore.GREEN}Make a guess!: ")).lower()
    #if guess == "word":
        #print(word)
        #quit()
    if not guess.isalpha() or len(guess) > 1:
        print()
        print(f"{Fore.CYAN}Your guess should not contain any number and must be a letter !")
    else:

        #main_logic
        if guess in word:
            correct_letters.append(guess)
            for char in word:
                if char not in correct_letters:
                    unlocked_word += "_"
                else:
                    unlocked_word += char

        elif guess in wrong_letters:
                print(f"{Fore.RED}You have already guessed that letter!")
                
        else:
            print(f"{Fore.BLUE}Your left attempts: ", 8 - count - 1)
            wrong_letters.append(guess)
            print(f"{Fore.MAGENTA}{Style.BRIGHT}{images[8 - count]}")
            count += 1

        print()
        print(f"{Fore.BLACK}{Back.WHITE}{unlocked_word}")
        
    #conclusion
    if unlocked_word == word:
        print(f"{Fore.YELLOW}Congrulations! You won the game!")
        break


else:
    #print(f"{Fore.MAGENTA}{Style.BRIGHT}{images[1]}")
    print()
    print(f"{Fore.BLUE}LOST! :(")
    print("Word was {}".format(word))