import re

def GetNumber(s):
    
    a = re.match('[0-9]+(\.[0-9]+)?',s)

    if a is None: 
        raise
    
    x = float(a.group())

    s = s[a.end():].strip()

    return s,x

def E(s):  # E -> aE'
    s,x = GetNumber(s) # a

    s = E_prim(s) # E'

    return s

def E_prim(s): # E' -> +aE' | -aE' | λ

    if len(s) > 0:

        if s[0] == '-': # -
            s,x = GetNumber(s[1:].strip()) # a
            s -= E_prim(s) # E'
        elif s[0] == '+': # +
            s,x = GetNumber(s[1:].strip()) # a
            s += E_prim(s) # E'
        else :
            raise 'Error'

    return s
 

s = input('Enter Experetion : \n\t')

try:
    s = E(s.strip())
    
    if len(s) > 0:
        print('Error')
    else :
        print('success')
except:
    print('Error')


'''
    E -> E + a | E - a | a 
    E -> aE'
    E' -> +aE' | -aE' | λ 

 '''