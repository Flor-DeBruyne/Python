pirates =  int(input("How many pirates are on the island?"))
coconuts =  int(input("How many coconuts have the pirates collected?"))


def sharing_coconuts(pirates,coconuts):
    """Solving the monkey and coconuts math problem"""
    for i in range(1,pirates+1):
        part = int(coconuts//pirates)
        monkey = int(coconuts - (part * pirates))
        if monkey >1:
            print(f"{coconuts} nuts = {part} nuts for pirate#{i} and {monkey} nuts for the monkey")
        elif monkey == 1:
            print(f"{coconuts} nuts = {part} nuts for pirate#{i} and {monkey} nut for the monkey")
        else:
            print(f"{coconuts} nuts = {part} nuts for pirate#{i} and no nuts for the monkey")
        coconuts -= part+monkey
        if i == pirates:
            if int(coconuts - ((coconuts//pirates) * pirates)) >1:
                print(f"each pirate gets {int(coconuts//pirates)} nuts and {int(coconuts - ((coconuts//pirates) * pirates))} nuts for the monkey")
            elif int(coconuts - ((coconuts//pirates) * pirates)) == 1:
                print(f"each pirate gets {int(coconuts//pirates)} nuts and {int(coconuts - ((coconuts//pirates) * pirates))} nut for the monkey")
            else:
                print(f"each pirate gets {int(coconuts//pirates)} nuts and no nuts for the monkey")


def main():
    sharing_coconuts(pirates,coconuts)

if __name__ == "__main__":
    main()
