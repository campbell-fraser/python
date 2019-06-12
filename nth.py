counter = 0
repeat1 = True
nth_term = input("nth term: ")
if repeat1 == True:
    for i in nth_term:
        if i != "n":
            counter = counter + 1
        if i == "n" and counter > 0:
            a = nth_term[0:counter]
            print(a)
            new = len(nth_term) - counter
            print(new)
            repeat1 = False
            counter = -100
