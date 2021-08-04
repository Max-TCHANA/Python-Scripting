"""module multipli contains the function table""" #This is the module docstring

def table(nb, max=10):
    """This function displays the multiplication table by nb from
    1 * nb to max * nb""" #This is the function docstring
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1