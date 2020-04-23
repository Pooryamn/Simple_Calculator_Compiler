import re

def GetNumber(s):
    
    a = re.match('[0-9]+(\.[0-9]+)?',s)

    if a is None: 
        raise
    
    x = float(a.group())

    s = s[a.end():].strip()

    return s,x

def E(s):
    s,x = GetNumber(s)

    if len(s) > 0:

        if s[0] == '-':
            x -= E(s[1:].strip())
        elif s[0] == '+':
            x += E(s[1:].strip())
        else :
            raise 'Error'

    return x

s = input('Enter Experetion : \n\t')

try:
    print(E(s.strip()))
except:
    print('Error')

'''

    E -> a + E | a
    E -> a - E | a

 '''