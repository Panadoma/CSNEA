def concat(a, b):
    tmpB = b
    bBits = 0
    while tmpB:
        tmpB >>= 1
        bBits += 1
        print(bBits)
        print('tmpB: '+str( bin(tmpB))+'  '+str(tmpB))
        

    return (a << bBits) | b



a= 0b100011
b= 0b001001
a=a<<6
b=a|b


print(bin(b))
