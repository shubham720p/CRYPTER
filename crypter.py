
from tkinter import  *
from tkinter import messagebox
import base64
import os 


# encrypts mtext
def Encrypt():
    passkey = key.get()
    
    if passkey =="634518":
        win2 = Toplevel(window)
        win2.title("encrypted")
        image_ico = PhotoImage(file = "enc.png")
        win2.iconphoto(False , image_ico)
        win2.geometry("350x250")
        win2.configure(bg = "green")
        message = text1.get(1.0 , END)
        encoded_msg = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_msg)
        encrypt = base64_bytes.decode("ascii")

        Label(win2 , text = "Encrypted Text" , font = "ivy 12 bold " , fg = "white" , bg = "green").place(x = 10 , y = 0)
        text2 = Text(win2, font = "ivy 10 bold", bg = "green" , relief = GROOVE , wrap = WORD )
        text2.place(x = 0 , y = 40 , width = 350 , height = 150)
        text2.insert(END , encrypt)
        win2.mainloop()
    elif passkey =="":
        messagebox.showerror("Encrption" , "input passkey")
    elif passkey != "634518":
        messagebox.showerror("Encrption" , "invalid passkey")
    # dencrypts text
def Decrypt():
    passkey = key.get()
    
    if passkey =="634518":
        win3 = Toplevel(window)
        image_ico = PhotoImage(file = "enc.png")
        win3.iconphoto(False , image_ico)
        win3.title("Decryption")
        win3.geometry("350x250")
        win3.configure(bg = "red")
        message = text1.get(1.0 , END)
        decoded_msg = message.encode("ascii")
        base64_bytes = base64.b64decode(decoded_msg)
        decrypt = base64_bytes.decode("ascii")

        Label(win3 , text = "Decrypted text" , font = "ivy  12 bold" , fg = "white" , bg = "red").place(x = 10 , y = 0)
        text2 = Text(win3, font = "rpbote 10 bold", bg = "red" , relief = GROOVE , wrap = WORD )
        text2.place(x = 0 , y = 40 , width = 350 , height = 150)
        text2.insert(END , decrypt)
        win3.mainloop()
    elif passkey =="":
        messagebox.showerror("Dncrption" , "input passkey")
    elif passkey != "634518":
        messagebox.showerror("Dncrption" , "invalid passkey")
def window():
    global window
    global key 
    global text1
    window = Tk()
    window.geometry("375x300")
    # resets text
    def reset():
        key.set("")
        text1.delete(1.0 , END)


    image_ico = PhotoImage(file = "enc.png")
    window.iconphoto(False , image_ico)
    window.title("EncDec")
    Label(text = "Enter message for Encryption and Decryption", fg = "black" , font = "ivy 12 bold").place(x = 10 , y = 10)
    text1 = Text(font = "Ivy 20 bold" , bg = "yellow" , relief = GROOVE,wrap= WORD , bd =0 )
    text1.place(x = 0, y = 40, height = 75)

    Label(text = "Enter key for Encryption And Decryption" , fg = "black" , font = "Ivy 12 bold").place(x=10 , y = 125)
    text2 = Text(font = "Ivy 20 bold" , bg = "White" , relief = GROOVE,wrap= WORD , bd =0 )
    key = StringVar()
    Entry(textvariable = key , width = 19 , bd = 2 , font = "ivy 25",show = "*").place(x= 10 , y = 147)


    Button(text = "Encrypt" , height = 2 , width = 22,bg = "green" , bd = 1,command = Encrypt).place(x = 10 , y = 200)
    Button(text = "Decrypt" , height = 2 , width = 22,bg = "red" , bd = 1,command = Decrypt).place(x = 196 , y = 200)
    Button(text = "RESET" , height = "2" , width = 22 , bg = "#1089ff" , fg = "white", bd = 1 , command = reset).place(x = 100 , y = 250)
    window.mainloop()

window()