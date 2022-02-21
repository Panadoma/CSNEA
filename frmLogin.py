import tkinter as tk   
import main
from tkinter import ttk
#initiolize the form
loginfrm =tk.Tk()
loginfrm.title("login")
loginfrm.geometry('400x400+50+50')
loginfrm.resizable(False,False)
loginfrm.configure(background='white')

#loginfrm.iconbitmap('./assets/sdf.ico')





def LoginButtonClick():
    loginfrm.quit()




#UI wigets#
frame = tk.Frame(loginfrm,bg='white')
frame.place(x=110,y=100)
#Userpicture
####User icon lable####
photo = tk.PhotoImage(file='./UIelements/usericon.png')
image_label = ttk.Label(
    frame,
    image=photo,
    padding=5,
    background='white'
)
###Username Textbox
UsernameText = tk.StringVar()
txtUsername = tk.Entry(frame,textvariable= UsernameText)


###Password Textbox
PasswordText= tk.StringVar()
txtPassword=tk.Entry(frame, textvariable=PasswordText, show='*')#Only show * because its  a password
###login button####
exit_button = ttk.Button(
    frame,
    text='Login',   
    command= LoginButtonClick
)




image_label.pack()
txtUsername.pack(padx=10)
txtPassword.pack(pady=5)
exit_button.pack(pady=7,expand=True)






loginfrm.mainloop()
