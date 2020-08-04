from tkinter import *
class gui:
    def __init__(self,master):
        self.master=master
        master.title("PyCrypt")

        self.string=StringVar(master)
        self.result=StringVar(master)

        self.var1=IntVar(master)
        self.var2=IntVar(master)
        self.var3=IntVar(master)
        self.var4=IntVar(master)

        self.label2=Label(master,text='Enter the string: ')
        self.label2.pack()

        self.text1=Entry(master,textvariable=self.string)
        self.text1.pack()

        self.label4=Label(master,text='Select one of the options:')
        self.label4.pack()

        self.chk1=Checkbutton(master,text='Morse Code',variable=self.var1)
        self.chk1.pack()

        self.chk2=Checkbutton(master,text='Binary',variable=self.var2)
        self.chk2.pack()

        self.chk3=Checkbutton(master,text='Octal',variable=self.var3)
        self.chk3.pack()

        self.chk4=Checkbutton(master,text='Hexadecimal',variable=self.var4)
        self.chk4.pack()

        self.button1=Button(master,text='Encrypt',command=self.cl1)
        self.button1.pack()

        self.button2=Button(master,text='Decrypt',command=self.cl2)
        self.button2.pack()

        self.label3=Entry(master,textvariable=self.result)
        self.label3.pack()

        self.button3=Button(master,text='Quit',command=master.destroy,anchor=CENTER)
        self.button3.pack()
    
    def binary(self):
        n=int(self.string.get())
        l=[]
        while n>=1:
            if n%2==0:
                l.append(0)
            elif n%2==1:
                l.append(1)
            else:
                l.append(1)
                break
            n=n//2
        l=l[::-1]
        c=''
        for i in l:
            c=c+str(i)
        self.result.set(str(c))

    def octal(self):
        n=int(self.string.get())
        l=[]
        while True:
            if n//8<8:
                l.append(n%8)
                l.append(n//8)
                break
            else:
                l.append(n%8)
            n=n//8
        l=l[::-1]
        c=''
        for i in l:
            c=c+str(i)
        self.result.set(str(c))

    def hexad(self):
        n=int(self.string.get())
        l=[]
        while True:
            if n//16<16:
                l.append(n%16)
                l.append(n//16)
                break
            else:
                l.append(n%16)
            n=n//16
        l=l[::-1]
        c=''
        for i in l:
            if i==10:
                c=c+'A'
            elif i==11:
                c=c+'B'
            elif i==12:
                c=c+'C'
            elif i==13:
                c=c+'D'
            elif i==14:
                c=c+'E'
            elif i==15:
                c=c+'F'
            else:
                c=c+str(i)
        self.result.set(str(c))

    def encode(self):
        d1={' ':'|','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
        a=str(self.string.get())
        b=''
        for i in a:
            if i in d1:
                b=b+d1[i]
            else:
                b=b+'#'
            b=b+' '
        self.result.set(str(b))

    def decode(self):
        d2={'|':' ','.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'}                                                                                                                            
        a=str(self.string.get())
        a=a.split()
        b=''
        for i in a:
            if i in d2:
                b=b+d2[i]
            else:
                b=b+'#'
        self.result.set(str(b))

    def dbin(self):
        n=int(self.string.get())
        a=str(n)[::-1]
        c=0
        for i in range (len(a)):
            c=c+(int(a[i])*(2**i))
        self.result.set(str(c))

    def doct(self):
        n=int(self.string.get())
        a=str(n)[::-1]
        c=0
        for i in range (len(a)):
            c=c+(int(a[i])*(8**i))
        self.result.set(str(c))

    def dhex(self):
        n=str(self.string.get())
        a=n[::-1]
        c=0
        for i in range (len(a)):
            if a[i]=='A':
                c=c+(10*(16**i))
            elif a[i]=='B':
                c=c+(11*(16**i))
            elif a[i]=='C':
                c=c+(12*(16**i))
            elif a[i]=='D':
                c=c+(13*(16**i))
            elif a[i]=='E':
                c=c+(14*(16**i))
            elif a[i]=='F':
                c=c+(15*(16**i))
            else:
                c=c+(int(a[i])*(16**i))
        self.result.set(str(c))

    def cl1(self):
        if self.var1.get()==1:
            self.encode()
        elif self.var2.get()==1:
            self.binary()
        elif self.var3.get()==1:
            self.octal()
        elif self.var4.get()==1:
            self.hexad()

    def cl2(self):
        if self.var1.get()==1:
            self.decode()
        if self.var2.get()==1:
            self.dbin()
        if self.var3.get()==1:
            self.doct()
        if self.var4.get()==1:
            self.dhex()

root=Tk()
mygui=gui(root)
root.mainloop()
