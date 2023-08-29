import os
import sys

def key_schedule(key):
    keylength = len(key)

    #print("key is " + ord(str(key)))
    #print("key is " + key)

    S = list(range(256))
    j = 0
    for i in range (256):
        #k = ord(key[i % keylength])
        k = (key[i % keylength])
        j = (j + S[i] + k) % 256
        S[i], S[j] = S[j], S[i] #swap
    return S

with open(sys.argv[1], 'rb') as key_file, open(sys.argv[2], 'rb') as encrypted, open("decrypted_shellcode.bin", 'wb') as out:
    key_size = os.path.getsize(sys.argv[1]) #0x20
    key = key_file.read(key_size)
    S = key_schedule(key)

    j = 0
    i = 0

    shellcode_size = os.path.getsize(sys.argv[2]) #0x65E4

    while (shellcode_size > 0):
        char = encrypted.read(1)
        #print ("char is ", char)

        i = (i + 1) % 256
        j = (j + S[i]) % 256

        #swap
        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        #k = (S[(S[i] + S[j]) % 256]).to_bytes(2, 'big')
        shellcode_size -= 1

        #print("k bytes gives ", k)

        print("byte to write ", (ord(char) ^ k))

        #out.write(bytes(ord(char) ^ k))
        outbyte = ord(char) ^ k
        out.write(bytes([outbyte]))



    out.close()
    key_file.close()
    encrypted.close()
