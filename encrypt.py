from acts import *
def encrypt(sentence,s):
    # print("in encrypt: {")
    encoded = blockConverter(sentence)
    # print(encoded)
    # enlength = len(encoded)
    A = int(encoded[0],2)
    B = int(encoded[1],2)
    C = int(encoded[2],2)
    D = int(encoded[3],2)
    orgi = []
    orgi.append(A)
    orgi.append(B)
    orgi.append(C)
    orgi.append(D)

  
    B = (B + s[0])%modulo
    D = (D + s[1])%modulo 
    for i in range(1,r+1):
        t_temp = F(B)%modulo 
        t = ROL(t_temp,lgw)
        u_temp = F(D)%modulo
        u = ROL(u_temp,lgw)
        tmod=t%w
        umod=u%w
        A = (ROL(A^t,umod) + s[2*i])%modulo 
        C = (ROL(C^u,tmod) + s[2*i+ 1])%modulo
        (A, B, C, D)  =  (B, C, D, A)
    A = (A + s[2*r + 2])%modulo 
    C = (C + s[2*r + 3])%modulo
    cipher = []
    cipher.append(A)
    cipher.append(B)
    cipher.append(C)
    cipher.append(D)
    # print(orgi, cipher)
    # print("}")
    return orgi,cipher


def main():
    print ("ENCRYPTION: ")
    #key='A WORD IS A WORD'
    key = input("Enter Key(0-16 characters): ")
    if len(key) <b:
        key = key + " "*(b-len(key))
    key = key[:b]
                         
    print( "UserKey: "+key )
    s = generateKey(key)
    # print(s)
    #sentence = 'I WORD IS A WORD'
    rsentence = input("Enter a text: ")
    with open("encrypted.txt", mode = 'wb') as f:
            pass
    
    cipher_text = ""
    ftt = len(rsentence)//sz
    rmr = len(rsentence)%sz
    if rmr:
        rsentence = rsentence + " "*(sz-rmr)
    # print(sz, len(rsentence), ftt, rmr)
    lsentence = [rsentence[chunk: chunk+sz] for chunk in range(0,len(rsentence),sz)]
    # print(lsentence)
    for sentence in lsentence:
        orgi,cipher = encrypt(sentence,s)
        esentence = deBlocker(cipher)
        print ("\nInput String: "+sentence )
        print ("Original String list: ",orgi)
        print ("Length of Input String: ",len(sentence))
        print ("\nEncrypted String list: ",cipher)
        print ("Encrypted String: " + esentence)
        print ("Length of Encrypted String: ",len(esentence))
        with open("encrypted.txt", mode = 'ab') as f:
            f.write(str.encode(esentence, encoding='utf-8'))
        cipher_text += esentence
    print(cipher_text)
    print('Encrypted')
if __name__ == "__main__":

    main()
