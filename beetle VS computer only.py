import random

#general variables
player = "player 1"
play = True

#player 1 specific variables
No_6 = True
No_5 = True
beetle_count = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0

#computer specific variables
No_6_computer = True
No_5_computer = True
beetle_count_computer = 0
counter_1_computer = 0
counter_2_computer = 0
counter_3_computer = 0
counter_4_computer = 0

#print rules (will do later, is boring)

#initiate loop
while play == True:
    if player == "player 1":
        if beetle_count_computer == 6:
            print("\nThe computer won!")
            print("\n\         /")
            print(" `-.`-'.-'")
            print(" ,:--.--:.")
            print("/ |  |  | \ ")
            print(" /\  |  /\ ")
            print(" | `.:.' |")
            play = False
        if beetle_count == 6:
            print("\nYou win!")
            print("\n\         /")
            print(" `-.`-'.-'")
            print(" ,:--.--:.")
            print("/ |  |  | \ ")
            print(" /\  |  /\ ")
            print(" | `.:.' |")
            play = False
        if play == True:
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
        player = "computer"
    if player == "computer":
        if play == True:
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
