def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    templist =  aDict.values()
    result = 0
    for elmnt in aDict.values():
        result += len(elmnt)
    return result
