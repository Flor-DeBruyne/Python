def csum(digit):
    """calculating the c sum"""
    d = digit
    while len(str(d)) is not 1:
        d = list(map(int,str(d)))
        d = sum(d)
    return d
    


# def main():
#     csum(digit)

# if __name__ == "__main__":
#   main()

