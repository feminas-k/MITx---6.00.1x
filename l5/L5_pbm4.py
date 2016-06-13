def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        smaller = a
    else:
        smaller = b
    for i in range(1,smaller+1):
        if ((a%i == 0) and (b%i == 0)):
            gcd = i
    return gcd    
