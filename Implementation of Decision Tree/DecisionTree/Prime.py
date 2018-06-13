#Function to find PrimeNumber less than Sqaure root of number.
def findPrimeSet(num):
    primelist =[2]
    if num == 2 :
        return primelist
    i=3
    while i <= num:

        primeflag = True
        #all the number in prime list
        for prime in primelist:
            # if the number is divisible in previous prime list then not a prime
            if i%prime ==0:
                primeflag=False
                break
        # Primeflag is set to true, if it was not divisible by any prime factor before.
        # add to the primelist
        if(primeflag==True):
            primelist.append(i)
        #increment the i.
        i+=1
    return primelist
#method to display the list of prime factors.
def displayfactorList(factors):

    length = len(factors)
    # if length is one then just print one element.
    if  length == 1:
        print(factors[0])
    # else this.
    else:
        # print all the prime factors other than the last element
        for i in range(length-1):
            print(factors[i],end=",")
         # print the last element without comma and new line.
        print(factors[length-1])



#Find Prime factors.
def primefactor(number):
    #make a copy of number
    dupNumber = number
    #if number less than 2 return empty.(no Prime factors)
    if(number <2):
        print("The number is less than 2 and no prime factors")
        return

    # List of primes less than sqaure root of a number.
    #example num is 100 then, [2,3,5,7]
    nums = findPrimeSet(number)

    #prime factors.
    Primefactorlist=[]

    for i in nums:
        #if the number is divisible by the prime factor,
        #add the prime factor to the list and divide the number
        #with the same factor again till it finishes.
        while(dupNumber%i==0):
            Primefactorlist.append(i)
            dupNumber=dupNumber/i

    #send the list to the method be printed.
    displayfactorList(Primefactorlist)

#Debug to check prime factors.
#primelist = findPrimeSet(3)
#print(primelist)
print("Input the Number:")
num = int(input())
print("The prime factors are below")
primefactor(num)



