from afinn import Afinn
def calc(x, y, o):
    if (o == 'a'):
        return x + y
    elif (o == 's'):
        return x - y
    elif (o == 'd'):
        return x / y
    elif (o == 'm'):
        return x * y


def strrev(st):
    return st[::-1]


def str_add(stg):
    s = 0
    for i in stg:
        if (i.isnumeric()):
            s = s + int(i)
    return s


def strAdd(stg):
    stg = stg.split(' ')
    w = 0
    for i in stg:
        if (i.isnumeric()):
            w = w + int(i)
    return w


def summ(l):
    s = 0
    for i in l:
        if (isinstance(i, int) or isinstance(i, float)):
            s = s + i
    return round(s)


def factor(num):
    l = []
    for i in range(1, num):
        if (num % i == 0):
            l.append(i)
    return l


def perfact(x):
    l = factor(x)
    s = sum(l)
    if x == s:
        return True
    else:
        False


def evenodd(v):
    if 2 != 0:
        return 'odd'
    else:
        return 'even'
def qc(v):
    if(v==1):
        return 4
    elif(v==2):
        return 1
    elif(v==3):
        return 2
    elif(v==4):
        return 3
def sa(r):
    score = Afinn().score(r)
    if(score>0):
        return 'Positive'
    elif(score<0):
        return 'Negative'
    else:
        return 'Neutral'

