import hashlib
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

#cube root of the first 64 primes


k = ['0x428a2f98', '0x71374491', '0xb5c0fbcf', '0xe9b5dba5', '0x3956c25b', '0x59f111f1', '0x923f82a4','0xab1c5ed5', '0xd807aa98', '0x12835b01', '0x243185be', '0x550c7dc3', '0x72be5d74', '0x80deb1fe','0x9bdc06a7', '0xc19bf174', '0xe49b69c1', '0xefbe4786', '0x0fc19dc6', '0x240ca1cc', '0x2de92c6f','0x4a7484aa', '0x5cb0a9dc', '0x76f988da', '0x983e5152', '0xa831c66d', '0xb00327c8', '0xbf597fc7','0xc6e00bf3', '0xd5a79147', '0x06ca6351', '0x14292967', '0x27b70a85', '0x2e1b2138', '0x4d2c6dfc','0x53380d13', '0x650a7354', '0x766a0abb', '0x81c2c92e', '0x92722c85', '0xa2bfe8a1', '0xa81a664b','0xc24b8b70', '0xc76c51a3', '0xd192e819', '0xd6990624', '0xf40e3585', '0x106aa070', '0x19a4c116','0x1e376c08', '0x2748774c', '0x34b0bcb5', '0x391c0cb3', '0x4ed8aa4a', '0x5b9cca4f', '0x682e6ff3','0x748f82ee', '0x78a5636f', '0x84c87814', '0x8cc70208', '0x90befffa', '0xa4506ceb', '0xbef9a3f7','0xc67178f2']



def sigma0(b):
    v=0
    #Xor rotate 7, rotate18,sr 3

def sigma1(b):
    v=1
    #Xor rotate 17, 19 shr 10


def Sigma0(i):
    v=4
    #rotate 2, rotate 13, roatate 22

def Sigma1(i):
    v=1
    #..6 11 25


def choice(i):
    v=1 
    #three inputs, the choosing between y and z depending of x







#Start the program
text = input("enter a string to convert into ascii values:")
ascii_values = []
for character in text:
    ascii_values.append(ord(character))


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

    print("new")


    print(bin(tmp1))

    print(bin(tmp2))
    print(bin(tmp3))
    print(bin(tmp4))



    print(bin(WB))



    
#Expand the message schedules    







print(ascii_values)
print(len(ascii_values))
print("-----")
print(WS)
print(len(WS),"WS length")
