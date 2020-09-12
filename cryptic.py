#!/usr/bin/python3.8
from cryptography.fernet import Fernet
import os


def cr():
    option = input("Choose option: ")

    while True:
        try:
            if option == "1":
                from encryptic import encrypt
                encrypt()

            elif option == "2":
                from decryptic import decrypt
                decrypt()

            elif option == "3":
                from new_decription_key import new_key
                new_key()

        except Exception as e:
            print(e)
        continue


cr()
