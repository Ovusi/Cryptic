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


def encrypt():
    current_dir = os.getcwd()
    print("\nCurrent directory is " + current_dir)

    try:
        while current_dir:
            file_name = input("\n[*] Name of file to be encrypted: ")

            try:
                def load_key():
                    return open(input("[*] Enter name of key file: "), "rb").read()

                def enc():
                    fn = file_name
                    k = load_key()

                    f = Fernet(k)

                    with open(fn, "rb") as file:
                        file_data = file.read()
                        encrypted_data = f.encrypt(file_data)

                    with open(fn, "wb") as file:
                        file.write(encrypted_data)
                        print("\n>>> Encryption successful")

                enc()
            except Exception as e:
                print(e)
            continue
    except Exception as e:
        print(e)


def main():
    banner()
    encrypt()


if __name__ == '__main__':
    main()
