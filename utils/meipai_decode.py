def getHex(a):
    hex = a[:4][::-1]
    str1= a[4:]
    return str1, hex

def getDec(a):
    b = str(int(a, 16))
    c = list(b[:2])
    d = list(b[2:])
    return c, d

def substr(a,b):
    k = int(b[0])
    c = a[:k]
    d = a[k:k+int(b[1])]
    temp = a[int(b[0]):].replace(d, "")
    res = c+ temp
    return res

def getPos(a,b):
        b[0] = len(a) -int(b[0]) - int(b[1])
        return b