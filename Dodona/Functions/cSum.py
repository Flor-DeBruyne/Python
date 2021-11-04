def csum(digit):
    """calculating the c sum"""
    d = list(map(int,str(digit)))
    stop = True
    while stop:
        if len(d) == 1:
            res = ' '.join(map(str, d))
            print(res)
            stop = False
        else:
            sum(d)


# def main():
#     csum(digit)

# if __name__ == "__main__":
#   main()

