from cryptography.fernet import Fernet
file = "data.csv"

##############################################################################################
#Generates a key and save it into a file
##############################################################################################

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

##############################################################################################
#Loads the key from the current directory named `key.key`
##############################################################################################
def load_key():
    return open("key.key", "rb").read()

key = load_key()

#print(key)

##############################################################################################
#Given a filename (str) and key (bytes), it encrypts the file and write it
##############################################################################################

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)

    with open('encrypt'+filename, "wb") as file:
        file.write(encrypted_data)

encrypt(file, key)

##############################################################################################
#Given a filename (str) and key (bytes), it decrypts the file and write it
##############################################################################################

def decrypt(filename, key):
    f = Fernet(key)
    with open('encrypt'+filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    print(decrypted_data)
    # write the original file
    with open('decrypt'+filename, "wb") as file:
        file.write(decrypted_data)

decrypt(file, key)