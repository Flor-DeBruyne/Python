import math

def BaselProblem():
    """Outputting the Basel problem for 100"""
    result = 0
    #n = 0
    for i in range(1,101):        
        result += (1/i**2)
        #n = result - ((math.pi**2)/6)
    print(result)
    print(100) # don't know how to find the second solution

def main():
    BaselProblem()

if __name__ == "__main__":
    main()