again = True
while again == True:
    a = int(input("#1: "))
    b = int(input("#2: "))
    c = int(input("#3: "))
    d = int(input("#4: "))
    if (c-b) == (b-a):
        r = b-a
        ar = (a-r)
        if ar > 0 or ar == 0:
            ar = "+"+str(ar)
        r = str(r)+"n"
        nth_term = str(r)+str(ar)
        print(nth_term)
    elif ((d-c)-(c-b)) == ((c-b)-(b-a)):
        nsquared = ((c-b)-(b-a))/2
        n = ((b-(4*nsquared))-(a-nsquared))
        c = ((a-nsquared)-n)
        if n > 0 or n == 0:
            n = "+"+str(n)
        if c > 0 or c == 0:
            c = "+"+str(c)
        nsquared = str(nsquared)+"n²"
        n = str(n)+"n"
        nth_term = (str(nsquared) + str(n) + str(c))
        print(nth_term)
    elif (c/b) == (b/a):
        r = (b/a)
        nth_term = str(a)+"*("+str(r)+"^n-1)"
        print(nth_term)
    again_ = input("Again (y/n): ")
    if again_ == "y" or again_ == "Y":
        again = True
    else:
        again = False
