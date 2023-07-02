from acts import *
import sys
def decrypt(esentence,s):
    encoded = blockConverter(esentence)
    # enlength = len(encoded)
    A = int(encoded[0],2)
    B = int(encoded[1],2)
    C = int(encoded[2],2)
    D = int(encoded[3],2)
    cipher = []
    cipher.append(A)
    cipher.append(B)
    cipher.append(C)
    cipher.append(D)
    C = (C - s[2*r+3])%modulo
    A = (A - s[2*r+2])%modulo
    for j in range(1,r+1):
        i = r+1-j
        (A, B, C, D) = (D, A, B, C)
        u_temp = F(D)%modulo
        u = ROL(u_temp,lgw)
        t_temp = F(B)%modulo 
        t = ROL(t_temp,lgw)
        tmod=t%w
        umod=u%w
        C = (ROR((C-s[2*i+1])%modulo,tmod)  ^u)  
        A = (ROR((A-s[2*i])%modulo,umod)   ^t) 
    D = (D - s[1])%modulo 
    B = (B - s[0])%modulo
    orgi = []
    orgi.append(A)
    orgi.append(B)
    orgi.append(C)
    orgi.append(D)
    return cipher,orgi



def main():
    print ("DECRYPTION: ")
    #key='A WORD IS A WORD'
    key = input("Enter Key(0-16 characters): ")
    if len(key) <b:
        key = key + " "*(b-len(key))
    key = key[:b]
                         
    print ("UserKey: "+key )
    s = generateKey(key)
    plain_text = ""
    with open("encrypted.txt","rb") as f:
        if not f:
            print ("Encrypted input not found in encrypted.txt")
            sys.exit(0)
        else:
            resentence = f.read().decode(encoding='utf-8')
            print(resentence, len(resentence))
            lsentence = [resentence[chunk: chunk+sz] for chunk in range(0,len(resentence),sz)]
            for esentence in lsentence:
                cipher,orgi = decrypt(esentence,s)
                sentence = deBlocker(orgi)
                print ("\nEncrypted String list: ",cipher)
                print ("Encrypted String: " + esentence)
                print ("Length of Encrypted String: ",len(esentence))

                print ("\nDecrypted String list: ",orgi)
                print ("Decrypted String: " + sentence )
                print ("Length of Decrypted String: ",len(sentence))
                plain_text += sentence
    with open('plained.txt', 'w', encoding='utf-8') as f:
        f.write(plain_text)
    print('Decrypted')
if __name__ == "__main__":
    main()
