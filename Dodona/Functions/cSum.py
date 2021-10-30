digit = input()

def c_sum(digit):
    """calculating the c sum"""
    d = list(map(int,str(digit)))
    stop = True
    while stop:
        if len(d) == 1:
            res = ' '.join(map(str, d))
            print(res)
            stop = False
        sum(d)

def main():
    c_sum(digit)

if __name__ == "__main__":
  main()

