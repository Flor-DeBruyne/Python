eerste = int(input())
tweede = int(input())

def bevriende_getallen(eerste, tweede):
    """checks if two int's are friendly"""
    delersEerste = 0
    delersTweede = 0
    for x in range(eerste):
        if x != 0:
            if eerste % x == 0:
                delersEerste += x
    for y in range(tweede):
        if y != 0:
           if tweede % y == 0:
                delersTweede += y
    if delersEerste == tweede and delersTweede == eerste:
        print(f"{eerste} en {tweede} zijn bevriende getallen")
    else:
        print(f"{eerste} en {tweede} zijn geen bevriende getallen")


def main():
  bevriende_getallen(eerste, tweede)

if __name__ == "__main__":
  main()