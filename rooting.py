import sys

from math import sqrt   #imports the module for square rooting
from math import sin    #imports the module for sine calculations
from math import cos    #imports the module for cosine calculations
from math import tan    #imports the module for tangent calculations
from math import asin   #imports the module for inverse sine calculations
from math import acos   #imports the module for inverse cosine calculations
from math import atan   #imports the module for inverse tangent calculations

pyth_trig = input("PYTHAGORAS OR TRIGONOMETRY?  ")
if pyth_trig == "pythagoras":
    abc = input("Which side are you working out? A, B or C? ")
    if abc == "c" or abc == "c":
        a = int(input("A: "))
        b = int(input("B: "))
        c = (a*a)+(b*b)
        c = sqrt(c)
        print("C = "+str(c))
    if abc == "a" or abc == "A":
        b = int(input("B: "))
        c = int(input("C: "))
        a = (c*c)-(b*b)
        a = sqrt(a)
        print("A = "+str(a))
    if abc == "b" or abc == "B":
        a = int(input("A: "))
        c = int(input("C: "))
        b = (c*c)-(a*a)
        b = sqrt(b)
        print("B = "+str(b))
