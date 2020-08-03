#importing required libraries
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *
import base64
import hashlib
import pyperclip

#master variable, window options
root=Tk()
root.title("PyCrypt")
root.resizable(False,False)
root.iconbitmap("./res/favicon.ico")

#input variables
s=StringVar(root)
result=StringVar(root)
key=StringVar(root)

#dictionary for morse code
d1={' ':'|','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
d2={'|':' ','.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'}

#function for program information
def hello():
    lines=["Cryption tool made using python.","https://github.com/Devansh3712"]
    tkinter.messagebox.showinfo("PyCrypt","\n".join(lines))

#function for text -> Base16
def base16e():
    n=str(s.get())
    m=n.encode("ascii")
    a=base64.b16encode(m)
    c=a.decode("ascii")
    global result
    result.set(str(c))

#function for Base16 -> text
def base16d():
    n=str(s.get())
    m=n.encode("ascii")
    a=base64.b16decode(m)
    c=a.decode("ascii")
    global result
    result.set(str(c))

#function for text -> Base85
def base85e():
    n=str(s.get())
    m=n.encode("ascii")
    a=base64.b85encode(m)
    c=a.decode("ascii")
    global result
    result.set(str(c))

#function for Base85 -> text
def base85d():
    n=str(s.get())
    m=n.encode("ascii")
    a=base64.b85decode(m)
    c=a.decode("ascii")
    global result
    result.set(str(c))

#function for text -> MD5
def md5():
    n=str(s.get())
    n=n.encode()
    c=hashlib.md5(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> SHA-224
def sha224():
    n=str(s.get())
    n=n.encode()
    c=hashlib.sha224(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> SHA-256
def sha256():
    n=str(s.get())
    n=n.encode()
    c=hashlib.sha256(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> SHA-384
def sha384():
    n=str(s.get())
    n=n.encode()
    c=hashlib.sha384(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> SHA-512
def sha512():
    n=str(s.get())
    n=n.encode()
    c=hashlib.sha512(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> SHA-3-256
def sha3256():
    n=str(s.get())
    n=n.encode()
    c=hashlib.sha3_256(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> SHA-3-512
def sha3512():
    n=str(s.get())
    n=n.encode()
    c=hashlib.sha3_512(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> 256-bit BLAKE2
def blake2s():
    n=str(s.get())
    n=n.encode()
    c=hashlib.blake2s(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> 512-bit BLAKE2
def blake2b():
    n=str(s.get())
    n=n.encode()
    c=hashlib.blake2b(n).hexdigest()
    global result
    result.set(str(c))

#function for text -> Vigenere Cipher
def vce():
    n=str(s.get())
    k=str(key.get())
    c=''
    a=[ord(i) for i in (n)]
    b=[ord(j) for j in (k)]
    for x in range (len(n)):
        d=(a[x]+b[x%len(k)])%26
        c=c+chr(65+d)
    global result
    result.set(str(c))

#for Vigenere Cipher -> text
def vcd():
    n=str(s.get())
    k=str(key.get())
    c=''
    a=[ord(i) for i in (n)]
    b=[ord(j) for j in (k)]
    for x in range (len(n)):
        d=(a[x]-b[x%len(k)])%26
        c=c+chr(65+d)
    global result
    result.set(str(c))

#function for text -> Caesar Cipher
def cce():
    n=str(s.get())
    k=int(key.get())
    c=''
    for i in range (len(n)):
        a=n[i]
        if a.isupper():
            c+=chr((ord(a)+k-65)%26+65)
        else:
            c+=chr((ord(a)+k-97)%26+97)
    global result
    result.set(str(c))

#function for Caesar Cipher -> text
def ccd():
    n=str(s.get())
    k=int(key.get())
    c=''
    for i in range (len(n)):
        a=n[i]
        if a.isupper():
            c+=chr((ord(a)-k-65)%26+65)
        else:
            c+=chr((ord(a)-k-97)%26+97)
    global result
    result.set(str(c))

#function for text -> ASCII
def enascii():
    n=str(s.get())
    c=''
    for i in n:
        c=c+str(ord(i))
        c=c+' '
    global result
    result.set(str(c))

#function for ASCII -> text
def deascii():
    n=str(s.get())
    n=n.split(' ')
    c=''
    for i in n:
        c=c+str(chr(int(i)))
    global result
    result.set(str(c))

#function for text -> Base32
def base32e():
    n=str(s.get())
    m=n.encode("ascii")
    a=base64.b32encode(m)
    c=a.decode("ascii")
    global result
    result.set(str(c))

#function for Base32 -> text
def base32d():
    n=str(s.get())
    m=n.encode("ascii")
    a=base64.b32decode(m)
    c=a.decode("ascii")
    global result
    result.set(str(c))

#function for text -> Base64
def base64e():
    n=str(s.get())
    m=n.encode("ascii")
    a=base64.b64encode(m)
    c=a.decode("ascii")
    global result
    result.set(str(c))

#function for Base64 -> text
def base64d():
    n=str(s.get())
    m=n.encode("ascii")
    a=base64.b64decode(m)
    c=a.decode("ascii")
    global result
    result.set(str(c))

#function for text -> Binary (base 2)
def binary():
    n=int(s.get())
    c=bin(n)[2:]
    global result
    result.set(str(c))

#function for text -> Octal (base 8)
def octal():
    n=int(s.get())
    c=oct(n)[2:]
    global result
    result.set(str(c))

#function for text -> Hexadecimal (base 16)
def hexad():
    n=int(s.get())
    c=hex(n)[2:]
    global result
    result.set(str(c))

#function for text -> Morse Code
def encrypt():
    a=str(s.get())
    b=''
    for i in a:
        if i in d1:
            b=b+d1[i]
        else:
            b=b+'#'
        b=b+' '
    global result
    result.set(str(b))

#function for Morse Code -> text
def decrypt():
    a=str(s.get())
    a=a.split()
    b=''
    for i in a:
        if i in d2:
            b=b+d2[i]
        else:
            b=b+'#'
    global result
    result.set(str(b))

#function for Binary -> text
def dbin():
    n=str(s.get())
    c=int(n,2)
    global result
    result.set(str(c))

#function for Octal -> text
def doct():
    n=str(s.get())
    c=int(n,8)
    global result
    result.set(str(c))

#function for Hexadecimal -> text
def dhex():
    n=str(s.get())
    c=int(n,16)
    global result
    result.set(str(c))

#copy to clipboard
def copy_to_clipboard():
    pyperclip.copy(result.get())

#overall encode function for checkbuttons
def cl1():
    if var1.get()==1:
        encrypt()
    elif var2.get()==1:
        binary()
    elif var3.get()==1:
        octal()
    elif var4.get()==1:
        hexad()
    elif var5.get()==1:
        base64e()
    elif var6.get()==1:
        base32e()
    elif var7.get()==1:
        enascii()
    elif var8.get()==1:
        cce()
    elif var9.get()==1:
        vce()
    elif var10.get()==1:
        md5()
    elif var11.get()==1:
        sha224()
    elif var12.get()==1:
        sha256()
    elif var13.get()==1:
        sha384()
    elif var14.get()==1:
        sha512()
    elif var15.get()==1:
        sha3256()
    elif var16.get()==1:
        sha3512()
    elif var17.get()==1:
        blake2s()
    elif var18.get()==1:
        blake2b()
    elif var19.get()==1:
        base16e()
    elif var20.get()==1:
        base85e()

#overall decode function for checkbuttons
def cl2():
    if var1.get()==1:
        decrypt()
    elif var2.get()==1:
        dbin()
    elif var3.get()==1:
        doct()
    elif var4.get()==1:
        dhex()
    elif var5.get()==1:
        base64d()
    elif var6.get()==1:
        base32d()
    elif var7.get()==1:
        deascii()
    elif var8.get()==1:
        ccd()
    elif var9.get()==1:
        vcd()
    elif var19.get()==1:
        base16d()
    elif var20.get()==1:
        base85d()

#variables for checkbuttons
var1=IntVar(root)
var2=IntVar(root)
var3=IntVar(root)
var4=IntVar(root)
var5=IntVar(root)
var6=IntVar(root)
var7=IntVar(root)
var8=IntVar(root)
var9=IntVar(root)
var10=IntVar(root)
var11=IntVar(root)
var12=IntVar(root)
var13=IntVar(root)
var14=IntVar(root)
var15=IntVar(root)
var16=IntVar(root)
var17=IntVar(root)
var18=IntVar(root)
var19=IntVar(root)
var20=IntVar(root)

#labels, texts and buttons
img=PhotoImage(file="./res/main.PNG")
chk1=Checkbutton(root,text='Morse Code',variable=var1)
chk2=Checkbutton(root,text='Binary',variable=var2)
chk3=Checkbutton(root,text='Octal',variable=var3)
chk4=Checkbutton(root,text='Hexadecimal',variable=var4)
chk5=Checkbutton(root,text='Base64',variable=var5)
chk6=Checkbutton(root,text='Base32',variable=var6)
chk7=Checkbutton(root,text='ASCII',variable=var7)
chk8=Checkbutton(root,text='Caesar Cipher',variable=var8)
chk9=Checkbutton(root,text='Vigenere Cipher',variable=var9)
chk10=Checkbutton(root,text='MD5',variable=var10)
chk11=Checkbutton(root,text='SHA224',variable=var11)
chk12=Checkbutton(root,text='SHA256',variable=var12)
chk13=Checkbutton(root,text='SHA384',variable=var13)
chk14=Checkbutton(root,text='SHA512',variable=var14)
chk15=Checkbutton(root,text='SHA-3-216',variable=var15)
chk16=Checkbutton(root,text='SHA-3-512',variable=var16)
chk17=Checkbutton(root,text='256-bit BLAKE2',variable=var17)
chk18=Checkbutton(root,text='512-bit BLAKE2',variable=var18)
chk19=Checkbutton(root,text='Base16',variable=var19)
chk20=Checkbutton(root,text='Base85',variable=var20)
label2=Label(root,text='Enter the string: ')
text1=Entry(root,textvariable=s)
button1=Button(root,text='Encrypt',command=cl1)
button2=Button(root,text='Decrypt',command=cl2)
label3=Entry(root,textvariable=result)
button3=Button(root,text='Quit',command=root.quit)
label4=Label(root,text='Select one of the options:')
label5=Label(root,text='Enter the key (if any): ')
text2=Entry(root,textvariable=key)
button4=Button(root,text='Info',command=hello)
label6=Label(root,text='Final String: ')
label7=Label(image=img)
button5=Button(root,text='Copy',command=copy_to_clipboard)

#labels, texts and buttons alignment
label7.grid(row=1,column=2,columnspan=2,rowspan=2,sticky=W+N+E+S)
label2.grid(row=1,column=0)
text1.grid(row=1,column=1)
label4.grid(row=3)
label5.grid(row=2,column=0)
text2.grid(row=2,column=1,sticky=W)
chk1.grid(row=4,column=0,sticky=W)
chk2.grid(row=4,column=1,sticky=W)
chk3.grid(row=5,column=0,sticky=W)
chk4.grid(row=5,column=1,sticky=W)
chk5.grid(row=4,column=2,sticky=W)
chk6.grid(row=5,column=2,sticky=W)
chk7.grid(row=6,column=0,sticky=W)
chk8.grid(row=6,column=1,sticky=W)
chk9.grid(row=8,column=3,sticky=W)
chk10.grid(row=4,column=3,sticky=W)
chk11.grid(row=5,column=3,sticky=W)
chk12.grid(row=6,column=3,sticky=W)
chk13.grid(row=7,column=0,sticky=W)
chk14.grid(row=7,column=1,sticky=W)
chk15.grid(row=7,column=2,sticky=W)
chk16.grid(row=7,column=3,sticky=W)
chk17.grid(row=8,column=0,sticky=W)
chk18.grid(row=8,column=1,sticky=W)
chk19.grid(row=8,column=2,sticky=W)
chk20.grid(row=6,column=2,sticky=W)
button1.grid(row=9,column=1,sticky=W)
button2.grid(row=9,column=2,sticky=W)
label3.grid(row=10,column=1)
label6.grid(row=10,column=0)
button3.grid(row=11,column=3)
button4.grid(row=11,column=0)
button5.grid(row=10,column=2,sticky=W)

#mainloop
root.mainloop()
