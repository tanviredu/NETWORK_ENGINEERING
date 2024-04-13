import crypt
import argparse
password_ok = False
parser = argparse.ArgumentParser()
parser.add_argument("--name",type=str,required=True)
args = parser.parse_args()
while password_ok!=True:

    #new_password = input("Enter a new password\n=>")
    new_password = args.name
    password_length = len(new_password)
    salt = "thisisaverysecretsalt"
    hashed_password = crypt.crypt(new_password,salt)

    if password_length > 6:
        password_ok = True
        print(hashed_password)
