"""
Created by V I E R U S   ||   Date 6/1/2023
This code is a python Tkinter Caesar Cipher program.
It has an adjustable shift section and you will be able to print both your encryption and decryption personal message
-
TODO v2.0
Next update will fix the spacing problem, include a file encryption and decryption section, and fix clearErrorMessage message
-
Please Enjoy
"""

import tkinter
from tkinter import *
from tkinter import ttk

def encryptMess():
    mode = 'encrypt'
    shift = shiftchange.get()
    EncryptMessage = plaintextEn.get()
    character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.!?$'
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
    character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.!?$'
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
    plaintextDe.get()
    
    if plaintextEn.get()=="" and plaintextDe.get()=="":
        clearErrorMessage = ("Error, Already cleared")
    else:
        shiftchange.set(4)
        plaintextEn.set("")
        plaintextDe.set("")
        cipherEncryption.set("")
        cipherDecryption.set("")
        

#main--------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("Caesar Cipher")
root.geometry("750x400")

#Intro-------------------------------------------------------------------------------------------------------------------------
ttk.Label(root, text="""Hello welcome to the Caesar Cipher. The Caesar Cipher was orginial made so Caesar could communicate in code to his armies.\n
          With this code you, yourself can use the code and will be able to enter your code, change the shift and decrypt the code as well.\n
          This code currently does not accept any numbers and only certain amount of symbols.\n
          Enjoy!""").grid(column=0, row=1, columnspan=4)
ttk.Label(root, text='').grid(column=0, row=2)

#Shift--------------------------------------------------------------------------------------------------------------------------
ttk.Label(text="You can change the shift or keep the default of 4").grid(column=0,row=3)
shiftchange = IntVar()
shiftchange.set(4)
ttk.Radiobutton(text="4", value=4, variable=shiftchange).grid(sticky="W", column=1, row=3)
ttk.Radiobutton(text="5", value=5, variable=shiftchange).grid(sticky="W", column=1, row=4)
ttk.Radiobutton(text="6", value=6, variable=shiftchange).grid(sticky="W", column=1, row=5)
ttk.Radiobutton(text="7", value=7, variable=shiftchange).grid(sticky="W", column=2, row=3)
ttk.Radiobutton(text="8", value=8, variable=shiftchange).grid(sticky="W", column=2, row=4)
ttk.Radiobutton(text="9", value=9, variable=shiftchange).grid(sticky="W", column=2, row=5)

#Encrypt--------------------------------------------------------------------------------------------------------------------------
cipherEncryption = StringVar()
ttk.Label(root, text='').grid(column=0, row=6)
ttk.Label(text="Encrypt Your Message:").grid(sticky="W", column=0, row=7)
plaintextEn = StringVar()
ttk.Entry(textvariable=plaintextEn, width=50).grid(column=1, row=7)
ttk.Button(text="Encrypt >", command=encryptMess).grid(sticky="W", column=2, row=7)
ttk.Label(root, textvariable=cipherEncryption).grid(column=1, row=9)

# Decrypt--------------------------------------------------------------------------------------------------------------------------
cipherDecryption = StringVar()
ttk.Label(root, text='').grid(column=0, row=10)
ttk.Label(text="Decrypt the Message:").grid(sticky="W", column=0, row=11)
plaintextDe = StringVar()
ttk.Entry(textvariable=plaintextDe, width=50).grid(column=1, row=11)
ttk.Button(text="Decrypt >", command=decryptMess).grid(sticky="W", column=2, row=11)
ttk.Label(root, textvariable=cipherDecryption).grid(column=1, row=12)

#Clear/Exit-----------------------------------------------------------------------------------------------------------------------------
clearErrorMessage = StringVar()
ttk.Label(root, text='').grid(column=0, row=13, rowspan=14)

exitForm = ttk.Button(root, text="Exit", command=root.destroy).grid(column=0, row=15)
clearForm = ttk.Button(root, text="Clear Form", command=clear).grid(column=1, row=15)
ttk.Label(root, textvariable=clearErrorMessage).grid(column=1, row=16)
root.mainloop()