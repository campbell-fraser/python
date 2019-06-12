import random
import time
print("\tWelcome to The Obscure Number Game")

playagain = True

while playagain == True:
    gamemode = input("\nPick a gamemode (Easy, Medium, Hard, Impossible): ")
    if gamemode == ("Easy"):
        guess = True
        tries = 0
        the_number = random.randint(1, 100)
        print("\nI'm thinking of a number between 1 and 100.")
        print("Try and guess it in as few goes as possible!")
        while guess != the_number:
            guess = (input("Take a guess: "))

            try:
                guess = int(guess)
            except ValueError:
                print("Sorry, that wasn't an integer!")
            else:
              if guess < 1:
                  print("Sorry, too low!")
              if guess > 100:
                  print("Sorry, too high!")
              elif guess > the_number:
                  print("Lower...")
              elif guess < the_number:
                  print("Higher...")
            tries += 1

        if tries == 1:
            print("\nWHat??? Witchcraft! 1 attempt!?")
        else:
            print("\nYou guessed it! The number was "+ str(the_number)+".")
            if tries <= 10:
                print("And it only took you "+ str(tries)+" tries!")
            if tries > 10:
                print(str(tries)+" tries? Really? You can do better!")

        answer = input("\nWould you like to play again? (y/n) ")
        if answer == ("y"):
            playagain = True
        elif answer == ("n"):
            playagain = False
            print("Ok, thanks for playing!")
            print("\nCoded by Fraser Campbell")
            print("\"Obscure Number Game\" idea by Fraser Campbell, Joe Clitherow and Henry Blundell")
            time.sleep(3)
            print("By the way, feel free to modify this code!")
            time.sleep(100)
    if gamemode == ("Medium"):
        guess = True
        tries = 0
        the_number = random.randint(1, 1000)
        print("\nI'm thinking of a number between 1 and 1000.")
        print("Try and guess it in as few goes as possible!")
        while guess != the_number:
            guess = (input("Take a guess: "))

            try:
                guess = int(guess)
            except ValueError:
                print("Sorry, that wasn't an integer!")
            else:
              if guess < 1:
                  print("Sorry, too low!")
              if guess > 1000:
                  print("Sorry, too high!")
              elif guess > the_number:
                  print("Lower...")
              elif guess < the_number:
                  print("Higher...")
            tries += 1

        if tries == 1:
            print("\nWHat??? Witchcraft! 1 attempt!?")
        else:
            print("\nYou guessed it! The number was "+ str(the_number)+".")
            if tries <= 15:
                print("And it only took you "+ str(tries)+" tries!")
            if tries > 15:
                print(str(tries)+" tries? Really? You can do better!")

        answer = input("\nWould you like to play again? (y/n) ")
        if answer == ("y"):
            playagain = True
        elif answer == ("n"):
            playagain = False
            print("Ok, thanks for playing!")
            print("\n Coded by Fraser Campbell")
            print("\"Obscure Number Game\" idea by Fraser Campbell, Joe Clitherow and Henry Blundell")
            time.sleep(3)
            print("By the way, feel free to modify this code!")
            time.sleep(100)
    if gamemode == ("Hard"):
        guess = True
        tries = 0
        the_number = random.randint(-10000, 10000)
        print("\nI'm thinking of a number between -10000 and 10000.")
        print("Try and guess it in as few goes as possible!")
        print("You picked 'Hard', so the number could be negative this time!")
        while guess != the_number:
            guess = (input("Take a guess: "))

            try:
                guess = int(guess)
            except ValueError:
                print("Sorry, that wasn't an integer!")
            else:
              if guess < -10000:
                  print("Sorry, too low!")
              if guess > 10000:
                  print("Sorry, too high!")
              elif guess > the_number:
                  print("Lower...")
              elif guess < the_number:
                  print("Higher...")
            tries += 1

        if tries == 1:
            print("\nWHat??? Witchcraft! 1 attempt!?")
        else:
            print("You guessed it! The number was "+ str(the_number)+".")
            if tries <= 40:
                print("And it only took you "+ str(tries)+ " tries!")
            if tries > 40:
                print(str(tries)+" tries? Really? You can do better!")

        answer = input("\nWould you like to play again? (y/n) ")
        if answer == ("y"):
            playagain = True
        elif answer == ("n"):
            playagain = False
            print("Ok, thanks for playing!")
            print("\n Coded by Fraser Campbell")
            print("\"Obscure Number Game\" idea by Fraser Campbell, Joe Clitherow and Henry Blundell")
            time.sleep(3)
            print("\nBy the way, feel free to modify this code!")
            time.sleep(100)
    if gamemode == ("Impossible"):
        guess = True
        tries = 0
        the_number = random.randint(-10000000000000000000000000000000000000000, 10000000000000000000000000000000000000000)
        print("\nImpossible? Are you serious? Yikes. Well, good luck!")
        print("\nI'm thinking of a number between negative ten duodecillion and ten duodecillion.")
        print("Try and guess it in as few goes as possible!")
        while guess != the_number:
            guess = (input("Take a guess: "))

            try:
                guess = int(guess)
            except ValueError:
                print("Sorry, that wasn't an integer!")
            else:
              if guess < -10000000000000000000000000000000000000000:
                  print("Sorry, too low!")
              if guess > 10000000000000000000000000000000000000000:
                  print("Sorry, too high!")
              elif guess > the_number:
                  print("Lower...")
              elif guess < the_number:
                  print("Higher...")
            tries += 1

        if tries == 1:
            print("\nNO WAY! That can't be possible! 1 attempt!?")
        else:
            print("You guessed it! The number was "+ str(the_number)+".")
            if tries <= 1000:
                print("Whoa! "+ str(tries)+" tries! That's impressive!")
            if tries > 1000:
                print("Wow, good job! Not many people even finish this! You did it in "+ str(tries)+" tries!")

        answer = input("Would you like to play again? (y/n) ")
        if answer == ("y"):
            playagain = True
        elif answer == ("n"):
            playagain = False
            print("Ok, thanks for playing!")
            print("\nCoded by Fraser Campbell")
            print("\"Obscure Number Game\" idea by Fraser Campbell, Joe Clitherow and Henry Blundell")
            time.sleep(3)
            print("\nBy the way, feel free to modify this code!")
            time.sleep(100)
    if gamemode == ("Rick Astley"):
        encore = True
        while encore == True:
            print("\nNever gonna give you up")
            time.sleep(1)
            print("Never gonna let you down")
            time.sleep(1)
            print("Never gonna run around and desert you")
            time.sleep(1)
            print("Never gonna make you cry")
            time.sleep(1)
            print("Never gonna say goodbye")
            time.sleep(1)
            print("Never gonna tell a lie")
            time.sleep(1)
            print("And hurt you")
            answer = input("\nEncore? (y/n) ")
            if answer == ("y"):
                encore = True
            elif answer == ("n"):
                answer = input("\nOk then. How about playing the Obscure Number Game? (y/n) ")
                if answer == ("y"):
                    playagain = True
                    encore = False
                elif answer == ("n"):
                    playagain = False
                    print("Ok, thanks for playing!")
                    print("\nCoded by Fraser Campbell")
                    print("\"Obscure Number Game\" idea by Fraser Campbell, Joe Clitherow and Henry Blundell")
                    time.sleep(3)
                    print("\nBy the way, feel free to modify this code!")
                    time.sleep(100)
