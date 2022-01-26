def blackJack():
    """manual BlackJack with infinite cards"""
    stoppen = True
    totaal = 0
    while stoppen:
        kaart = int(input())
        if kaart == 0:
            print(f"Voorzichtig gespeeld ({totaal})")
            stoppen = False
        totaal += kaart
        if totaal >21:
            print(f"Verbrand ({totaal})")
            stoppen = False
        elif totaal == 21:
            print("Gewonnen!")
            stoppen = False
        


def main():
    blackJack()

if __name__ == "__main__":
    main()