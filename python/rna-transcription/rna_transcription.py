trantab = str.maketrans("GCTA", "CGAU")

def to_rna(string):
    if any(char not in "GCTA" for char in string):
        raise ValueError("Input DNA strand contains invalid bases")
    return string.translate(trantab)
