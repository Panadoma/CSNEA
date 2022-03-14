import hashlib
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

#cube root of the first 64 primes, used as random constants


k = ['0x428a2f98', '0x71374491', '0xb5c0fbcf', '0xe9b5dba5', '0x3956c25b', '0x59f111f1', '0x923f82a4','0xab1c5ed5', '0xd807aa98', '0x12835b01', '0x243185be', '0x550c7dc3', '0x72be5d74', '0x80deb1fe','0x9bdc06a7', '0xc19bf174', '0xe49b69c1', '0xefbe4786', '0x0fc19dc6', '0x240ca1cc', '0x2de92c6f','0x4a7484aa', '0x5cb0a9dc', '0x76f988da', '0x983e5152', '0xa831c66d', '0xb00327c8', '0xbf597fc7','0xc6e00bf3', '0xd5a79147', '0x06ca6351', '0x14292967', '0x27b70a85', '0x2e1b2138', '0x4d2c6dfc','0x53380d13', '0x650a7354', '0x766a0abb', '0x81c2c92e', '0x92722c85', '0xa2bfe8a1', '0xa81a664b','0xc24b8b70', '0xc76c51a3', '0xd192e819', '0xd6990624', '0xf40e3585', '0x106aa070', '0x19a4c116','0x1e376c08', '0x2748774c', '0x34b0bcb5', '0x391c0cb3', '0x4ed8aa4a', '0x5b9cca4f', '0x682e6ff3','0x748f82ee', '0x78a5636f', '0x84c87814', '0x8cc70208', '0x90befffa', '0xa4506ceb', '0xbef9a3f7','0xc67178f2']




#Bitwize Functinos

def rotateRight(value, rotations, width=8):
    #Circular shift right   
    
    if int(rotations) != abs(int(rotations)):
        rotations = width + int(rotations)
    return (int(value)<<(width-(rotations%width)) | (int(value)>>(rotations%width))) & ((1<<width)-1)





#Internal Functions
def sigma0(value):
    
    #Xor rotate 7, rotate18,sr 3
    v1= rotateRight(value,7,32)
    v2=rotateRight(value,18,32)
    v3=value>>3
    print("v1 rotate right 7,",bin(v1))
    print("v2, rotate 18," ,bin(v2))
    print("v3 the shift right 3,", bin(v3))
    returnValue= v1^v2^v3
    return returnValue



def sigma1(value):
    
    v1= rotateRight(value,17,32)
    v2=rotateRight(value,19,32)
    v3=value>>10
    print("v1 rotate right 17,",bin(v1))
    print("v2, rotate 19," ,bin(v2))
    print("v3 the shift right 10,", bin(v3))
    returnValue= v1^v2^v3
    return returnValue




def Sigma0(value):
    
    #Xor rotate 2, rotate 13, rotate 22
    v1= rotateRight(value,2,32)
    v2=rotateRight(value,13,32)
    v3=rotateRight(value,22,32)
    print("v1 rotate  2,",bin(v1))
    print("v2, rotate 13," ,bin(v2))
    print("v3 rotate 22", bin(v3))
    returnValue= v1^v2^v3
    return returnValue


def Sigma1(value):
    
    #Xor rotate 6, rotate 11, rotate 25
    v1= rotateRight(value,6,32)
    v2=rotateRight(value,11,32)
    v3=rotateRight(value,25,32)
    print("v1 rotate  6,",bin(v1))
    print("v2, rotate 11," ,bin(v2))
    print("v3 rotate 25", bin(v3))
    returnValue= v1^v2^v3
    return returnValue






def Choice(x,y,z):
    #Choose between two inputs(x and y) depending on the third(z)
    #ie (X or Y)XOR(NotX or Z)    in mathematical notation
    return((x&y)^(~x&z)) 







def Majority(x,y,z):
    #compare the three numbers x, y and z; for each bit output the majority 
    #ie (X and Y) Xor (X and Z) Xor (Y and X)
    return((x&y)^(x&z)^(y&z))
    




#Start the program
text = input("enter a string to convert into ascii values:")

ascii_values = []
for character in text:
    ascii_values.append(ord(character))
#turn the text into assci

orignalLen=len(ascii_values)

#apend a 1

ascii_values.append(0b10000000)


#pad
#Add 0's until multiple of 512 

varLength = len(ascii_values)
toAdd=63-varLength
for i in range(toAdd):
    ascii_values.append(0)


#apend the orignal length to the end(times by 8 since ascci is a byte)
ascii_values.append(orignalLen*8)






######creating message schedules
#the first 16 ws
WS=[]
for i in range(0,64,4):
    #convert into binary, concatinate each group of 4, append to WS
    #0-16 the for loop is
    
    tmp1=int(ascii_values[i])
    tmp2=int(ascii_values[i+1])
    tmp3=int(ascii_values[i+2])
    tmp4=int(ascii_values[i+3])



    tmp1=tmp1<<24
    tmp2=tmp2<<16
    tmp3=tmp3<<8
    
    WB=(((tmp1|tmp2)|tmp3)|tmp4) #concatinate each group of 4
    WS.append(WB)
    print(bin(WB))



    
#Expand the message schedules to 64 (the remaining 48)
#Wi= sigma1(Wi-2)+Wi-7+sigma0(Wi-15)+Wi-16


for i in range(16,64):
    temp=sigma1(WS[i-2])+WS[i-7]+sigma0(WS[i-15])+WS[i-16]
    WS.append(temp) 

    
    #if temp is larger than 32 bits, the MSB's should be ignored
    #TODO!











    
    




print(ascii_values)
print("assci values")
print(len(ascii_values))
print("asci values length")
print("-----")
print(WS)
print("ws")
print(len(WS),"WS length")

print(bin(WS[0]))
