import math
b = 16
r = 20
w = 32
lgw = int(math.log(w, 2))
modulo = 2**w
sz = (lgw-1)*4
def F(x):
    return x**2+x
#rotate right input x, by n bits
def ROR(x, n, bits = w):
    mask = (2**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))

#rotate left input x, by n bits
def ROL(x, n, bits = w):
    return ROR(x, bits - n,bits)

#convert input sentence into blocks of binary
#creates 4 blocks of binary each of 32 bits.
def blockConverter(sentence):
    # print("in blockconverter:{")
    encoded = []
    # print('sentence: ',sentence, len(sentence))
    res = ""
    for i in range(0,len(sentence)):
        temp = bin(ord(sentence[i]))[2:]
        if len(temp) <8:
            temp = "0"*(8-len(temp)) + temp
        res = res + temp
        if (i+1)%4==0:
            encoded.append(res)
            res = ""
    # encoded.append(res)
    # print('encoded: ',encoded, len(encoded))
    # print("}")
    return encoded

#converts 4 blocks array of long int into string
def deBlocker(blocks):
    # print("in deBlocker:{")
    # print('blocks: ',blocks, len(blocks))
    s = ""
    for ele in blocks:
        temp =bin(ele)[2:]
        if len(temp) <w:
            temp = "0"*(w-len(temp)) + temp
        for i in range(0,4):
            s=s+chr(int(temp[i*8:(i+1)*8],2))
    # print('s:', s, len(s))
    # print("}")
    return s

#generate key s[0... 2r+3] from given input string userkey
def generateKey(userkey):
    # print("in generatekey: {")
    # b=len(userkey)
    modulo = 2**w
    s=(2*r+4)*[0]
    s[0]=0xB7E15163
    for i in range(1,2*r+4):
        s[i]=(s[i-1]+0x9E3779B9)%(2**w)
    encoded = blockConverter(userkey)
    #print encoded
    enlength = len(encoded)
    l = enlength*[0]
    for i in range(1,enlength+1):
        l[enlength-i]=int(encoded[i-1],2)
    
    v = 3*max(enlength,2*r+4)
    A=B=i=j=0
    
    for index in range(0,v):
        A = s[i] = ROL((s[i] + A + B)%modulo,3)
        B = l[j] = ROL((l[j] + A + B)%modulo,(A+B)%w) 
        i = (i + 1) % (2*r + 4)
        j = (j + 1) % enlength
    # print('}')
    return s

# blockConverter('12345678901234567890')
    
