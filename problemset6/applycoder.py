def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    r = ''
    for char in text:
        if char in coder:
            r += coder[char]
        else:
            r += char
    return r        
