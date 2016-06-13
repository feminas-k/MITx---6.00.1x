def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #base case
    if aStr == '':
        return False
    #base case
    if len(aStr) == 1:
        return aStr == char
    midind = len(aStr)/2
    midchar = aStr[midind]
    #base case
    if char == midchar:
        return True
    #recursive case
    elif char < midchar:
        return isIn(char,aStr[:midind])
    #recursive case
    else:
        return isIn(char,aStr[midind+1:])
        
