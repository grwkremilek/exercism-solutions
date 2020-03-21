def slices(series, length):
    if 1 <= length <= len(series):
        substrings = []
        for i in range(len(series) - length + 1):
            substring = ""
            for n in range(length):
                substring += str(series[i+n])
            substrings.append(substring)
        return(substrings)
    raise ValueError("Series too short")

