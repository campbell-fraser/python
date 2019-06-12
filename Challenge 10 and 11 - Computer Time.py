comptime = input("On average, how many hours do you spend on a computer a day? ")
if int(comptime) < 2:
    print("That seems reasonable.")
elif int(comptime) < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get some fresh air. And a life.")
