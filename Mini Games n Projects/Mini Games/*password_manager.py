# a module allowing us to encrypt text to make it more obfuscated
from cryptography.fernet import Fernet


# wb stands for a write-in-byte mode (a special file format)
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        '''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
# connect with the master_pwd from user's input
# byte is kind of a different way of storing information
# in terms of computing we have bits and bytes, so our key here is byte -> so that is why we
# gotta change the master_pwd to bytes format by .encode() method -> *reference to fernet.py for more details
key = load_key() + master_pwd.encode()
# initialize Fetnet encryption module
fer = Fernet(key)


# take a string of text, using a key and turn it into a random string of text
# that we cannot give it back to the original text from without knowing the key

# key + password + text_to_encrypt = random_text
# random_text + key + password = text_to_encrypt


def view():
    with open('password.txt', 'r') as f:
        # noticed  that readline does not resemble readlines (print out to see the dissimilarity)
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            print(f"User: {user}\nPassword: {str(fer.decrypt(passw.encode()))}")


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    # a stands for the ability to append
    # r stands for the ability to read
    # w stands for the ability to write
    with open('password.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("It was an invalid mode.")
        continue
