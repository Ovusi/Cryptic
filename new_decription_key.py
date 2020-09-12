#!/usr/bin/python3.8
import os
from cryptography.fernet import Fernet


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


banner()


def new_key():
    current_dir = os.getcwd()
    print("Current directory is " + current_dir)

    key = Fernet.generate_key()
    with open(input("Enter name of new encryption key: "), "wb") as key_file:
        key_file.write(key)


new_key()
