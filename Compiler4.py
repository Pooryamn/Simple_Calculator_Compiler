import re

def GetNumber(s):
    
    a = re.match('[0-9]+(\.[0-9]+)?',s)

    if a is None: 
        raise
    
    x = float(a.group())

    s = s[a.end():].strip()

    return s,x

def E(s):
    s,x = T(s)

    while len(s)>0 and (s[0] == '+' or s[0] == '-'):
        op = s[0]

        s,x2 = T(s[1:])

        if op == '+':
            x += x2
        else :
            x -= x2

    return s,x

def T(s):
    s,x = F(s)

    while len(s)>0 and (s[0]=='*' or s[0] =='/'):
        op = s[0]

        s,x2 = F(s[1:])

        if op =='*':
            x *= x2
        else:
            x /= x2

    return s,x

def F(s):

    if s[0] == '(':
        s,x = E(s[1:])

        if s[0] !=')':
            print('Unmatched parenthesis: ',x)
            raise 'Unmatched parenthesis'
        s = s[1:]
    else:
        s,x = GetNumber(s)

    return s,x       

s = input('Enter Experetion : ')

try:
    s,x = E(s.strip())
    
    if len(s) > 0:
        print('Error ',s)
    
    else:
        print('success : ',x)

except:
    print('Error')


'''

E -> TE'
E' -> +TE' | -TE' | lambda
T -> FT'
T' -> *FT' | /FT' | lambda
F -> a | (E)

'''