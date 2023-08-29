import itertools
import string

password_db = ["abc", "123", "cat"]
# password = "abc"
pass_success = []

def guess_passwords():
    chars = string.ascii_lowercase + string.digits
    attempts = 0

    for password_length in range(1, 4):
        for p in itertools.product(chars, repeat = password_length):
            attempts +=1
            p = ''.join(p)
            # print(p, attempts)

            # if p == password:
            #     print ("password found: " + p) 
            
            if (p in password_db):
                # print("Password found! " + p)
                pass_success.append(p)

    return pass_success
            

print("ready, set, go!!!")
pass_list = guess_passwords()
if pass_list == []:
    print("No passwords found")
else:
    print(f"{len(pass_list)} Passwords found: {pass_list} ")



    
