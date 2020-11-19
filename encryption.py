import time
import os
clear = lambda: os.system("cls")

def encryption():
    clear()
    print("ENCRYPTION")
    print("----------")
    print()
    print("AVAILABLE OPTIONS:")
    print()
    print("1 - Encrypt Text")
    print("2 - Decrypt Text")
    print()
    user_option = input("Choose An Option: ").lower()
    if user_option == "1":
        encrypt()
    elif user_option == "2":
        decrypt()
    else:
        encryption()


def encrypt():
    clear()
    print("ENCRYPT")
    print("-------")
    while True:
        print()
        text = input("Enter Text: ")
        if text != '':
            break
    while True:
        print()
        key = input("Enter Key: ")
        if key.isdigit():
            break
        else:
            print()
            print("Key Must Be A Number")
    print()
    key = int(key)
    encrypt_text = ''

    for i in range(len(text)):
        crypt = (chr(ord(text[i]) + key))
        encrypt_text += crypt



    print("------------" + "-" *len(encrypt_text) if len(encrypt_text) <= 120 else "-"*120)
    print("ENCRYPTED: ["+encrypt_text+"]")
    print()
    print("------------" + "-" * len(encrypt_text) if len(encrypt_text) <= 120 else "-" * 120)
    while True:
        print()
        back = input("Press (B) To Go Back: ").lower()
        if back == "b":
            encryption()
            break




def decrypt():
    clear()
    print("DECRYPT")
    print("-------")
    print()
    while True:
        print()
        text = input("Enter Encrypted Text: ")
        if text != '':
            break
    while True:
        print()
        have_key = input("Do You Have A Key? ").lower()
        if (have_key == "yes" or have_key == "y") or (have_key == "no" or have_key == "n"):
            break
    if have_key == "yes" or have_key == "y":
        while True:
            key = input("Enter Key: ")
            if key.isdigit():
                break
            else:
                print()
                print("Key Must Be a Number")
        key = int(key)
        decrypt = ''
        for i in range(len(text)):
            plain_text = (chr(ord(text[i]) - key))
            decrypt += plain_text

        if " " in decrypt:
            print()
            print("DECRYPTED: [", decrypt,"]")
            print()
            encryption_back()

        else:
            print()
            print("KEY DOES NOT MATCH")
            print()
            encryption_back()


    elif have_key == "no" or have_key == "n":
        print()
        while True:
            rep_times = input("Enter How Many Times This Algorithm Runs:\nPress (R) To Run Until Encryption Is Broken:\n").lower()
            if rep_times == "r" or rep_times.isdigit():
                break
            else:
                print("Enter 'B' Or An Integer")
        if rep_times == "r":
            key = 0
            while rep_times != 0:
                decrypt = ''
                for i in range(len(text)):
                    plain_text = (chr(ord(text[i]) - key))
                    decrypt += plain_text

                key += 1
                print(decrypt)
                time.sleep(0.04)

                if " " in decrypt:
                    print()
                    print("-------------" + "-" * len(decrypt) if len(decrypt) <= 120 else "-"*120)
                    print("DECRYPTED:", decrypt)
                    print("KEY:", key - 1)
                    print("-------------" + "-" * len(decrypt) if len(decrypt) <= 120 else "-"*120)
                    print()
                    encryption_back()

        rep_times = int(rep_times)
        key = 0
        while rep_times != 0:
            decrypt = ''
            for i in range(len(text)):
                plain_text = (chr(ord(text[i]) - key))
                decrypt += plain_text
            rep_times -= 1
            key += 1
            print(decrypt)
            time.sleep(0.04)


            if " " in decrypt:
                print()
                print("-----------" + "-" * len(decrypt) if len(decrypt) <= 120 else "-"*120)
                print("DECRYPTED:", decrypt)
                print("KEY:", key-1)
                print("-----------" + "-" * len(decrypt))
                print()
                encryption_back()


    if " " not in decrypt:
        print()
        print("----------------------------------------------")
        print("UNABLE TO BREAK ENCRYPTION WITH GIVEN ATTEMPTS")
        print("----------------------------------------------")
        print()
        go_on = input("Press (E) To Continue Running Algorithm: \nPress (B) To Go Back:").lower()
        if go_on == "e":
            # key = key
            while key != 0:
                decrypt = ''
                for i in range(len(text)):
                    plain_text = (chr(ord(text[i]) - key))
                    decrypt += plain_text
                key += 1
                print(decrypt)

                time.sleep(0.04)
                if " " in decrypt:
                    print()
                    print("-----------" + "-" * len(decrypt) if len(decrypt) <= 120 else "-"*120)
                    print("DECRYPTED:", decrypt)
                    print("KEY:", key - 1)
                    print("-----------" + "-" * len(decrypt) if len(decrypt) <= 120 else "-"*120)
                    print()
                    encryption_back()





def encryption_back():
    while True:
        print()
        back = input("Press (B) To Go Back: ").lower()
        if back == "b":
            encryption()
            break
# MAIN
encryption()