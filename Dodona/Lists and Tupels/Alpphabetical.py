def alphabetical(string):
    """function to sort the string in alphabetical order"""
    unorderd = string.split()
    unorderd.sort()
    orderd = str(" ".join(unorderd))
    return orderd

