import re

def GetNumber(s):
    
    a = re.match('[0-9]+(\.[0-9]+)?',s)

    if a is None: 
        raise
    
    x = float(a.group())

    s = s[a.end():].strip()

    return s,x

def E(s): 

    s,x = GetNumber(s) # a

    while len(s) > 0 and (s[0] == '-' or s[0] == '+'): # if it is not λ and s[0] is + or -

        if s[0] == '-': # -
            s,x2 = GetNumber(s[1:].strip()) # a
            x -= x2
        elif s[0] == '+': # +
            s,x2 = GetNumber(s[1:].strip()) # a
            x += x2      
        else :
            raise 'Error'

    return s,x 
 

s = input('Enter Experetion : \n\t')

try:
    s,x = E(s.strip())
    
    if len(s) > 0:
        print('Error ',s)
    else :
        print('success : ',x)
except:
    print('Error')
