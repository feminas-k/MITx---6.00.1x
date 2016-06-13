def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    result = {}
    import string
    lower = string.ascii_lowercase
    lower_shifted = lower[shift:]+lower[:shift]
    upper = string.ascii_uppercase
    upper_shifted = upper[shift:]+upper[:shift]
    for i in range(26):
        result[lower[i]] = lower_shifted[i]
    for i in range(26):
        result[upper[i]] = upper_shifted[i]
    return result    
