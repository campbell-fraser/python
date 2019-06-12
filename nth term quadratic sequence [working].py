a = int(input("#1: "))
b = int(input("#2: "))
c = int(input("#3: "))
nsquared = ((c-b)-(b-a))/2
n = ((b-(4*nsquared))-(a-nsquared))
c = ((a-nsquared)-n)
nsquared = str(nsquared)+"n²"
if n == 0 and c == 0:
    nth_term = str(nsquared)
    print(nth_term)
if c == 0:
    if n > 0 or n == 0:
        n = "+"+str(n)+"n"
    nth_term = str(nsquared)+str(n)
    print(nth_term)
if n == 0:
    if c > 0 or c == 0:
        c = "+"+str(c)
    nth_term = str(nsquared)+str(c)
    print(nth_term)
else:
    if c > 0 or c == 0:
        c = "+"+str(c)
    if n > 0 or n == 0:
        n = "+"+str(n)+"n"
    nth_term = str(nsquared)+str(n)+str(c)
    print(nth_term)
