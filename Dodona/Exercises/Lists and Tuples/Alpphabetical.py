def alphabetical(string):
    """function to sort the string in alphabetical order"""
    unorderd = string.split()
    orderd = str(" ".join(unorderd.sort()))
    return orderd

