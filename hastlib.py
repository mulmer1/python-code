import hashlib
#Demonstrates the SHA1
password = input("Input the password to hash\n>")
print("\nSHA1:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    print(setpass)
    hash_object = hashlib.sha1(setpass)
    print(hash_object)
    guess_pw = hash_object.hexdigest()
    ##print(guess_pw)
    value=len(guess_pw)
    print(value)
