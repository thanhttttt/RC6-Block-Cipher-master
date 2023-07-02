# temp = bin(ord('1'))[2:]
# temp = bin(ord('q'))
# print(temp)
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
blocks = (blockConverter('12345567890123456'))
print(blocks[0])
print(int(blocks[0],2))
print(int(0b00110001001100100011001100110100))