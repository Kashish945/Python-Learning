from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
root=Tk()

def login():
    email=email_input.get()
    password=password_input.get()
    if email=="kashishpimpalshende@gmail.com" and password=="1234":
        messagebox.showinfo("Yayyyy", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Email or Password")

# replacing title
root.title("Login Form")

# replacing icon
# root.iconbitmap("icon_file_name.ico")

# manupulating size of window
root.geometry("350x500")

# changing background color
root.configure(bg="light blue")

# adding image
img=Image.open("image.png")
resized_img=img.resize((70, 70))
img=ImageTk.PhotoImage(resized_img)
img_label=Label(root, image=img)
img_label.pack(pady=10)

text_label=Label(root,text='Dream School',fg='white',bg='light blue',font=('italic',18,'bold'))
text_label.pack()

email_lable=Label(root,text='Enter Email',fg='white',bg='light blue',font=('verdana',12,"bold"))
email_lable.pack(pady=(20,5))

email_input=Entry(root,width=45)
email_input.pack(ipady=6,ipadx=15)

password_lable=Label(root,text='Enter Password',fg='white',bg='light blue',font=('verdana',12,"bold"))
password_lable.pack(pady=(20,5))

password_input=Entry(root,width=45)
password_input.pack(ipady=6,ipadx=15)

# adding button
login_button=Button(root,text='Login',fg='blue',bg='white',font=('verdana',10,"bold"),width=5,command=login)
login_button.pack(pady=(10,20))

root.mainloop()

