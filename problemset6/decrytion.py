def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    import string
    decoded = ''
    r = 0
    max_count = 0
    for i in range(26):
        count = 0
        decoded = applyShift(text,i)
        for word in decoded.split():
            if word.strip(string.punctuation+string.digits).lower() in wordList:
                count += 1
        if count > max_count:
            max_count = count
            r = i
    return r        
    
