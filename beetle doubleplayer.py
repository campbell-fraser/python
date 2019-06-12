import random
import time

playagain = True

#print rules (will do later, is boring)

while playagain == True:
    play = True
    player = "player 1"
    player_1 = input("PLAYER 1: ")
    player_2 = input("PLAYER 2 (type \"computer\" if you want to play the computer): ")
    if player_2 == "computer" or player_2 == "Computer":
        doubleplayer = False
    elif player_2 != "computer" or player_2 != "Computer":
        doubleplayer = True

    #player 1 specific variables
    No_6 = True
    No_5 = True
    beetle_count = 0
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0

    #player 2 specific variables
    P2_No_6 = True
    P2_No_5 = True
    P2_beetle_count = 0
    P2_counter_1 = 0
    P2_counter_2 = 0
    P2_counter_3 = 0
    P2_counter_4 = 0

    #computer specific variables
    No_6_computer = True
    No_5_computer = True
    beetle_count_computer = 0
    counter_1_computer = 0
    counter_2_computer = 0
    counter_3_computer = 0
    counter_4_computer = 0

    #initiate loop
    while play == True:
        if player == "player 1":
            if beetle_count_computer == 6:
                print("\nTHE COMPUTER WON!")
                print("\n\         /")
                print(" `-.`-'.-'")
                print(" ,:--.--:.")
                print("/ |  |  | \ ")
                print(" /\  |  /\ ")
                print(" | `.:.' |")
                play = False
            if beetle_count == 6:
                print("\n"+player_1.upper()+" WON!")
                print("\n\         /")
                print(" `-.`-'.-'")
                print(" ,:--.--:.")
                print("/ |  |  | \ ")
                print(" /\  |  /\ ")
                print(" | `.:.' |")
                play = False
            if P2_beetle_count == 6:
                print("\n"+player_2.upper()+" WON!")
                print("\n\         /")
                print(" `-.`-'.-'")
                print(" ,:--.--:.")
                print("/ |  |  | \ ")
                print(" /\  |  /\ ")
                print(" | `.:.' |")
                play = False
            if play == True:
                time.sleep(0.5)
                print("")
                if player_1.endswith("s"):
                    print(player_1.upper()+"' TURN")
                else:
                    print(player_1.upper()+"'S TURN")
                roll_input = input("Press enter to roll: ")
                roll = random.randint(1, 6)
                print("You got "+str(roll)+".")
            if roll == 6 and No_6 == True:
                print("You got the body! Now you can start adding the rest of the features.")
                beetle_count = beetle_count + 1
                No_6 = False
            if roll == 5 and No_5 == True and No_6 == False:
                print("You got the head! Now you can begin to add the eyes (1) and antenna (2).")
                beetle_count = beetle_count + 1
                No_5 = False
            if roll == 4 and No_6 == False:
                counter_4 = counter_4 + 1
                if counter_4 == 2:
                    beetle_count = beetle_count + 1
            if roll == 3 and No_6 == False:
                counter_3 = counter_3 + 1
                if counter_3 == 6:
                    beetle_count = beetle_count + 1
            if roll == 2 and No_5 == False and No_6 == False:
                counter_2 = counter_2 + 1
                if counter_2 == 2:
                    beetle_count = beetle_count + 1
            if roll == 1 and No_5 == False and No_6 == False:
                counter_1 = counter_1 + 1
                if counter_1 == 2:
                    beetle_count = beetle_count + 1
            if doubleplayer == False:
                player = "computer"
            elif doubleplayer == True:
                player = "player 2"

        if player == "player 2" and doubleplayer == True:
            if beetle_count == 6:
                print("\n"+player_1.upper()+" WON!")
                print("\n\         /")
                print(" `-.`-'.-'")
                print(" ,:--.--:.")
                print("/ |  |  | \ ")
                print(" /\  |  /\ ")
                print(" | `.:.' |")
                play = False
            if play == True:
                time.sleep(0.5)
                print("")
                if player_2.endswith("s") or player_2.endswith("S"):
                    print(player_2.upper()+"' TURN")
                else:
                    print(player_2.upper()+"'S TURN")
                roll_input = input("Press enter to roll: ")
                roll = random.randint(1, 6)
                print("You got "+str(roll)+".")
            if roll == 6 and P2_No_6 == True:
                print("You got the body! Now you can start adding the rest of the features.")
                P2_beetle_count = P2_beetle_count + 1
                P2_No_6 = False
            if roll == 5 and P2_No_5 == True and P2_No_6 == False:
                print("You got the head! Now you can begin to add the eyes (1) and antenna (2).")
                P2_beetle_count = P2_beetle_count + 1
                P2_No_5 = False
            if roll == 4 and P2_No_6 == False:
                P2_counter_4 = P2_counter_4 + 1
                if P2_counter_4 == 2:
                    P2_beetle_count = P2_beetle_count + 1
            if roll == 3 and P2_No_6 == False:
                P2_counter_3 = P2_counter_3 + 1
                if P2_counter_3 == 6:
                    P2_beetle_count = P2_beetle_count + 1
            if roll == 2 and P2_No_5 == False and P2_No_6 == False:
                P2_counter_2 = P2_counter_2 + 1
                if P2_counter_2 == 2:
                    P2_beetle_count = P2_beetle_count + 1
            if roll == 1 and P2_No_5 == False and P2_No_6 == False:
                P2_counter_1 = P2_counter_1 + 1
                if P2_counter_1 == 2:
                    P2_beetle_count = P2_beetle_count + 1
            if doubleplayer == False:
                player = "computer"
            elif doubleplayer == True:
                player = "player 1"

        if player == "computer" and doubleplayer == False:
            if play == True:
                time.sleep(0.5)
                print("")
                print("COMPUTER'S TURN")
                roll = random.randint(1, 6)
                print("The computer got "+str(roll)+".")
            if roll == 6 and No_6_computer == True:
                print("The computer got the body! Now it can start adding the rest of the features.")
                beetle_count_computer = beetle_count_computer + 1
                No_6_computer = False
            if roll == 5 and No_5_computer == True and No_6_computer == False:
                print("The computer got the head! Now it can begin to add the eyes (1) and antenna (2).")
                beetle_count_computer = beetle_count_computer + 1
                No_5_computer = False
            if roll == 4 and No_6_computer == False:
                counter_4_computer = counter_4_computer + 1
                if counter_4_computer == 2:
                    beetle_count_computer = beetle_count_computer + 1
            if roll == 3 and No_6_computer == False:
                counter_3_computer = counter_3_computer + 1
                if counter_3_computer == 6:
                    beetle_count_computer = beetle_count_computer + 1
            if roll == 2 and No_5_computer == False and No_6_computer == False:
                counter_2_computer = counter_2_computer + 1
                if counter_2_computer == 2:
                    beetle_count_computer = beetle_count_computer + 1
            if roll == 1 and No_5_computer == False and No_6_computer == False:
                counter_1_computer = counter_1_computer + 1
                if counter_1_computer == 2:
                    beetle_count_computer = beetle_count_computer + 1
            player = "player 1"
        if play == False:        
            playagain = input("Do you want to play again? ")
            if playagain == "yes" or playagain == "Yes":
                playagain = True
                print("")
