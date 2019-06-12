a = int(input("#1: "))
b = int(input("#2: "))
c = int(input("#3: "))
nsquared = ((c-b)-(b-a))/2
n = ((b-(4*nsquared))-(a-nsquared))
c = ((a-nsquared)-n)
nsquared = str(nsquared)+"n²"
if n > 0:
    n = "+"+str(n)+"n"
if c > 0:
    c = "+"+str(c)
nth_term = str(nsquared)+str(n)+str(c)
print(nth_term)
