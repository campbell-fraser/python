word = "sugar"
new_word = "-----"
playagain = True
counter = 0
l1 = word[0:1]
l2 = word[1:2]
l3 = word[2:3]
l4 = word[3:4]
l5 = word[4:5]
l6 = word[5:6]
print("Welcome to Hangman.\nI'm thinking of a word with "+str(len(word))+" letters.\nCan you guess it?")
while playagain == True:
    guess = input("Take a guess: ")
    new_word_II = new_word_II
    if guess in word and counter == 1:
        new_word = new_word_II
        location = word.find(guess)
        new_word_II = guess + new_word_II[location:]
        print(new_word_II)
    if guess in word:
        counter = 1
        location = word.find(guess)
        new_word_II = guess + new_word[location:]
        print(new_word_II)
