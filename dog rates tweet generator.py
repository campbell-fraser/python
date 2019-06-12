import random
import time

print("GENERATING @DOG_RATES TWEET...\n")
time.sleep(3)

name = random.randint(1,3)
pronoun = random.randint(1,2)
activity = random.randint(1,3)
extra = random.randint(1,3)
rate = random.randint(1,3)
end = random.randint(1,3)

if name == 1:
    name = "Zoey. "
elif name == 2:
    name = "Dewey. "
elif name == 3:
    name = "Rumble. "

if pronoun == 1:
    pronoun = "He "
elif pronoun == 2:
    pronoun = "She "

if activity == 1:
    activity = "likes road trips. "
elif activity == 2:
    activity = "just watched you drop a skittle on the ground. "
elif activity == 3:
    activity = "passed the h*ck out. "

if extra == 1:
    extra = "Savage af. "
elif extra == 2:
    extra = "Hopes you had a good day. "
elif extra == 3:
    extra = "Could not be less impressed. "

if rate == 1:
    rate = "13/10 "
elif rate == 2:
    rate = "11/10 "
elif rate == 3:
    rate = "10/10 "

if end == 1:
    end = "superior pupper"
elif end == 2:
    end = "would pet so well"
elif end == 3:
    end = "intellectual doggo"

tweet = "This is "+name+pronoun+activity+extra+rate+end+"."

print(tweet)
