#!/usr/bin/python3.8
from cryptography.fernet import Fernet
import os


def banner():
    print("""
            .   .   .   .   .   .   .
           .                      .
          .      .    .    .    .
         .      .
         .      .
         .      . RYPTIC
         .      .
         .      .   .   .
         .                  .
            .                   .
                .   .   .   .   .   .""")

    print("\nCryptic -- File encryption and decryption software."
          "\n---------------------------------------------------")


def decrypt():
    current_dir = os.getcwd()
    print("Current directory is " + current_dir)

    try:
        while current_dir:
            file_name = input("[*] Name of file to be decrypted: ")
            print(file_name)
            try:
                def load_key():
                    return open(input("[*] Enter name of key file: "), "rb").read()

                def dec():
                    fn = file_name
                    k = load_key()

                    f = Fernet(k)

                    with open(fn, "rb") as file:
                        encrypted_data = file.read()

                    decrypted_data = f.decrypt(encrypted_data)
                    with open(fn, "wb") as file:
                        file.write(decrypted_data)
                    print(">>> Deryption successfull")

                dec()
            except Exception as e:
                print(e)
            continue
    except Exception as e:
        print(e)


def main():
    banner()
    decrypt()


if __name__ == '__main__':
    main()
