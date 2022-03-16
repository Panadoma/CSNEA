import tkinter as tk   
import main
from tkinter import ttk
from tkinter import messagebox

def ShowMainForm():
    



    #Initiolize the AddNewAccount form
    frmAddAccount =tk.Tk()
    frmAddAccount.title("Main Menu")
    frmAddAccount.geometry('280x140+50+50')
    frmAddAccount.resizable(False,False)
    frmAddAccount.configure(background='white')

    
    Usernametext = tk.StringVar()
    PasswordText= tk.StringVar()
    rPasswordText= tk.StringVar()


    userAdd48 = tk.PhotoImage(file='./UIelements/UserAdd48.png') 
    staffAdd48 = tk.PhotoImage(file='./UIelements/StaffAdd48.png')
    memberAdd48 = tk.PhotoImage(file='./UIelements/MembersAdd48.png')
    recordAdd48 = tk.PhotoImage(file='./UIelements/folderAdd48')
    
    


    userSrch48 = tk.PhotoImage(file='./UIelements/UserSearch48.png') 
    staffSrch48 = tk.PhotoImage(file='./UIelements/StaffSearch48.png')
    memberSrch48 = tk.PhotoImage(file='./UIelements/MemberSearch48.png')
    recordSrch48 = tk.PhotoImage(file='./UIelements/folderSearch48')
    
    
    






    def NewAccount():#When the add button is pressed
        a=0
    def NewStaff():
        a=0
    def NewMember():
        a=0
    def NewRecord():
        a=0
    def SrchStaff():
        a=0
    def SrchMember():
        a=0
    def SrchRecord():
        a=0


    








            



    #############THE UI WIGETS####
    #The Frame#
    frame = tk.Frame(frmAddAccount,bg='white')
    frame.place(x=10,y=10)
    #The buttons
    btnNewAccount = ttk.Button(
        frame,
        image= userAdd48,
        text=' ',
        command= NewAccount
    )


    btnNewStaff = ttk.Button(
        frame,
        image= staffAdd48,
        text=' ',
        command= NewStaff
    )

    btnNewRecord = ttk.Button(
        frame,
        image= recordAdd48,
        text=' ',
        command= NewRecord
    )


    btnNewMember = ttk.Button(
        frame,
        image= memberAdd48,
        text=' ',
        command= NewMember
    )









    btnSearchStaff = ttk.Button(
        frame,
        image= staffSrch48,
        text=' ',
        command= SrchStaff
    )

    btnSearchRecord = ttk.Button(
        frame,
        image= recordSrch48,
        text=' ',
        command= SrchRecord
    )


    btnSearchMember = ttk.Button(
        frame,
        image= memberSrch48,
        text=' ',
        command= SrchMember
    )


    #Grid and placement

    btnNewAccount.grid(column=2,row=1,pady=2,padx=2)
    btnNewStaff.grid(column=3,row=1,pady=2,padx=2)
    btnNewRecord.grid(column=4,row=1,pady=2,padx=2)
    btnNewMember.grid(column=5,row=1,pady=2,padx=2)


    btnSearchStaff.grid(column=3,row=2,pady=2,padx=2)
    btnSearchRecord.grid(column=4,row=2,pady=2,padx=2)
    btnSearchMember.grid(column=5,row=2,pady=2,padx=2)






    frmAddAccount.mainloop()


ShowMainForm()





