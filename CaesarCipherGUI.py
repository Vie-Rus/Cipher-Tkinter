"""
Created by V I E R U S   ||   Date 07/03/2023
This code is a python Tkinter Caesar Cipher program.
It has an adjustable shift section and you will be able to print both your encryption and decryption personal message.
It also has a file encryption and decryption file.
-
TODO
Be able to clear form on file text file save, not found, error
Add file random variable on shift
-
Please Enjoy
"""
from tkinter import *
from tkinter import filedialog

def fileEncrypDecrypt():
    def enfilecipher():
        try:
            with open(fileText, 'r') as file:
                text = file.read()
                cipherText = caesar_encrypt(text, shift)
    
            with open(output_file, 'w') as file:
                file.write(cipherText)
            
            Label(endefileframe, text="File successfully encoded.").place(x=190, y=18)
        except FileNotFoundError:
            Label(endefileframe, text="File not found.").place(x=190, y=18)
        except Exception as e:
            Label(endefileframe, text=("An error occurred:", str(e))).place(x=190, y=18)

    def caesar_encrypt(text, shift):
        character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = '0123456789'
        cipherText = ''
        for chara in text:
            if chara in character:
                symbol_index = character.find(chara)
                translationIndex = symbol_index - shift
                if translationIndex >= len(character):
                    translationIndex -= len(character)
                elif translationIndex < 0:
                    translationIndex += len(character)
                cipherText += character[translationIndex]
            else:
                cipherText += chara
        return cipherText

    def defilecipher():
        try:
            with open(fileText, 'r') as file:
                text = file.read()
                plainText = caesar_decrypt(text, shift)
            with open(output_file, 'w') as file:
                file.write(plainText)
            Label(endefileframe, text="File successfully encoded.").place(x=190, y=48)
        except FileNotFoundError:
            Label(endefileframe, text="File not found.").place(x=190, y=48)
        except Exception as e:
            Label(endefileframe, text=("An error occurred:", str(e))).place(x=190, y=48)

    def caesar_decrypt(text, shift):
        character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        plainText = ''
        for chara in text:
            if chara in character:
                symbol_index = character.find(chara)
                translationIndex = symbol_index + shift
                if translationIndex >= len(character):
                    translationIndex -= len(character)
                elif translationIndex < 0:
                    translationIndex += len(character)
                plainText += character[translationIndex]
            else:
                plainText += chara
        return plainText

    fileText = filedialog.askopenfilename(title="open Text", filetypes=(("Text File", "*.txt"), ("Doc File", "*.docx"),))
    output_file = fileText
    shift = shiftchange.get()
    Button(endefileframe, text='Encrypt >', command=enfilecipher).place(x=110, y=15)
    Button(endefileframe, text='Decrypt >', command=defilecipher).place(x=110, y=45)

def encryptMess():
    mode = 'encrypt'
    shift = shiftchange.get()
    EncryptMessage = plaintextEn.get()
    character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    cipherText = ''
    for chara in EncryptMessage:
        if chara in character:
            symbol_index = character.find(chara)
            #encrypt
            if mode == 'encrypt':
                translationIndex = symbol_index - shift
            if translationIndex >= len(character):
                translationIndex -= len(character)
            elif translationIndex < 0:
                translationIndex += len(character)

            cipherText += character[translationIndex]
        else:
            cipherText += chara
            
    cenMessage = ("Your Encrypted message is: %s" % (cipherText))
    cipherEncryption.set(cenMessage)

def decryptMess():
    mode = 'decrypt'
    shift = shiftchange.get()
    DecryptMessage = plaintextDe.get()
    character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipherText = ''
    for chara in DecryptMessage:
        if chara in character:
            symbol_index = character.find(chara)
            # decrypt
            if mode == 'decrypt':
                translationIndex = symbol_index + shift
            if translationIndex >= len(character):
                translationIndex -= len(character)
            elif translationIndex < 0:
                translationIndex += len(character)

            cipherText += character[translationIndex]
        else:
            cipherText += chara
            
    cdeMessage = ("Your Decrypted message is: %s" % (cipherText))
    cipherDecryption.set(cdeMessage)

def clear():
    shiftchange.get()
    plaintextEn.get()
    cipherEncryption.get()
    plaintextDe.get()
    cipherDecryption.get()
    #cipherText1.get()
    #plainText1.get()
    # clearErrorMessage = StringVar()
    if plaintextEn.get()=="" and plaintextDe.get()=="" and cipherEncryption.get=="" and cipherDecryption.get()=="":
        Label(bottomFrame, text="clearErrorMessage").place(x=50, y=35)
    else:
        shiftchange.set(4)
        plaintextEn.set("")
        cipherEncryption.set("")
        plaintextDe.set("")
        cipherDecryption.set("")


#Main--------------------------------------------------------------------------------------------------------------------------------------------
root =  Tk() #before anything else
root.title("Caesar Cipher")
root.geometry('450x675')
filenamePath = StringVar()
filename = StringVar()
#Shift------------------------------------------------------------------------------------------------------------------------
shiftframe = LabelFrame(root, text="Change the shift or keep Default", padx=5, pady=5)
shiftframe.pack(padx=10, pady=10, expand='yes', fill='both') 

shiftchange = IntVar()
shiftchange.set(4)
Radiobutton(shiftframe, text="4", value=4, variable=shiftchange).place(x=5, y=5)
Radiobutton(shiftframe, text="5", value=5, variable=shiftchange).place(x=45, y=5)
Radiobutton(shiftframe, text="6", value=6, variable=shiftchange).place(x=85, y=5)
Radiobutton(shiftframe, text="7", value=7, variable=shiftchange).place(x=125, y=5)
Radiobutton(shiftframe, text="8", value=8, variable=shiftchange).place(x=165, y=5)
Radiobutton(shiftframe, text="9", value=9, variable=shiftchange).place(x=205, y=5)
Radiobutton(shiftframe, text="10", value=10, variable=shiftchange).place(x=245, y=5)

#Encrypt------------------------------------------------------------------------------------------------------------------------
encryptframe = LabelFrame(root, text="Encrypt Your Message", padx=5, pady=5)
encryptframe.pack(padx=10, pady=10, expand='yes', fill='both') 

cipherEncryption = StringVar()
plaintextEn = StringVar()
Entry(encryptframe, textvariable=plaintextEn, width=50).place(x=5, y=5)
Button(encryptframe, text=" Encrypt >", command=encryptMess).place(x=310, y=2)
Label(encryptframe, textvariable=cipherEncryption).place(x=5, y=35)

# Decrypt--------------------------------------------------------------------------------------------------------------------------
decryptframe = LabelFrame(root, text="Decrypt Your Message", padx=5, pady=5)
decryptframe.pack(padx=10, pady=10, expand='yes', fill='both') 

cipherDecryption = StringVar()
plaintextDe = StringVar()
Entry(decryptframe, textvariable=plaintextDe, width=50).place(x=5, y=5)
Button(decryptframe, text=" Decrypt >", command=decryptMess).place(x=310, y=2)
Label(decryptframe, textvariable=cipherDecryption).place(x=5, y=35)

# File---------------------------------------
endefileframe = LabelFrame(root, text="Encrypt/Decrypt Your File", padx=5, pady=5)
endefileframe.pack(padx=10, pady=10, expand='yes', fill='both') 

#cipherText1 = StringVar()
#plainText1 = StringVar()
Button(endefileframe, text='Choose a File >', command=fileEncrypDecrypt).place(x=5, y=30)

#Exit/clear form-------------------------------------------------------------------
bottomFrame = LabelFrame(root, text="Exit/Clear Form", padx=5, pady=5)
bottomFrame.pack(padx=10, pady=10, expand='yes', fill='both') 

clearErrorMessage = StringVar()
Button(bottomFrame, text=" Exit ", command=root.destroy).place(x=10, y=5)
Button(bottomFrame, text=" Clear Form ", command=clear).place(x=50, y=5)

root.mainloop()