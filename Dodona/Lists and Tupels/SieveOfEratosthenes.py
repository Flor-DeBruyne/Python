def sieve(number):
    """Sieve of Eratosthenes"""
    prime = [True for i in range(number + 1)]
    p = 2
    printer = []
    while p * p <= number:
        if prime[p] == True:
            for i in range(p**2, number + 1, p):
                prime[i] = False
        p +=1
    prime[0] = False
    prime[1] = False
    for p in range(number + 1):
        printer.append(p)
    print(printer)
    
            



			


