#Check if number is composite
def isComposite(n): 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return False

    if (n % 2 == 0 or n % 3 == 0): 
        return True
    i = 5
    while(i * i <= n): 
          
        if (n % i == 0 or n % (i + 2) == 0): 
            return True
        i = i + 6
          
    return False

# Returns factors of prime numbers 
def factorise(n):
    d = 2
    factors = [ ] 
    while n > 1:
      if n % d == 0:
        factors.append(d)
        n = n/d
      else:
        d = d + 1
    return factors


#Find composite elements
def findComposite():
 for i in range(1,10000):
        if isComposite(i):
            compositeElements.append(i)

#Find the prime factors
def findCompositesWith2PrimeMultiples():
    for i in compositeElements:
        if len(factorise(i))==2:
            storeCompositesofTwoMultiples.append(i)

#Main Program

compositeElements=[]
storeCompositesofTwoMultiples=[]

findComposite()

findCompositesWith2PrimeMultiples()

sortedList=sorted(storeCompositesofTwoMultiples)

print(sortedList[60])

#Phone number is 6598730187