n = int(input())

def ladder_digits(n):
    """making a ladder of digits"""
    for i in range(1,n+1):
        for y in range(1,i+1):
            print(y, end = "")
        print()

def main():
    ladder_digits(n)

if __name__ == "__main__":
    main()








