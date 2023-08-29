def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]
        new_char = ord(char)+s
        result += chr(new_char)

    return result

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        new_char = (ord(char) -s)
        result += chr(new_char)
    return result

text = "Hello"
s = 27

encrypted_str = encrypt(text, s)
print("encrypted string is ", encrypted_str)
print("decrypted string is ", decrypt(encrypted_str, s))

