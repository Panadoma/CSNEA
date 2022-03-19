def ShowAddUserForm():



    #Initiolize the AddNewAccount form
    frmAddAccount =tk.Tk()
    frmAddAccount.title("Add Users")
    frmAddAccount.geometry('400x250+50+50')
    frmAddAccount.resizable(False,False)
    frmAddAccount.configure(background='white')

    
    Usernametext = tk.StringVar()
    PasswordText= tk.StringVar()
    rPasswordText= tk.StringVar()




    def AddAccount():#When the add button is pressed


        #Validation
        validationPassed= True


        
        

        if validationPassed:
            #Salt the username and password, then hash it
            SaltedPassword = txtAddPassword.get() + txtAddUsername.get()
            HashedPassword= SHA256(SaltedPassword)
            

            #Check if the user already exists



            IsNewUser = True
            if IsNewUser:
                with open('programData/HashedPasswords.txt', 'a') as file:
                    HashedPassword=HashedPassword + '\n'
                    file.write(HashedPassword)


        else:

            tkMessageBox.showerror("Error","Please Enter a valid username and password")
                








            



    #############THE UI WIGETS####
    #The Frame#
    frame = tk.Frame(frmAddAccount,bg='white')
    frame.place(x=60,y=55)


    #Lables######
    lblUsername= ttk.Label(
        frame,
        text='Username',
        background='white'
    )

    lblPassword= ttk.Label(
        frame,
        text='Password',
        padding=0,
        background='white'
    )

    lblRAddPassword= ttk.Label(
        frame,
        text='Repeat Password',
        background='white'
    )
    ###Username Textbox
    txtAddUsername = tk.Entry(frame,textvariable=Usernametext)

    ###Password Textbox
    txtAddPassword=tk.Entry(frame, textvariable=PasswordText, show='*')#Only show * because its  a password
    txtRAddPassword=tk.Entry(frame, textvariable=rPasswordText, show='*')#Only show * because its  a password

    ###Add button####
    btnAddNewAccount = ttk.Button(
        frame,
        text='Add',
        command= AddAccount
    )





    #Grid and placements
    lblUsername.grid(column=0,row=1,padx=7,sticky='W')
    txtAddUsername.grid(column=2,row=1)
    lblPassword.grid(column=0,row=2,pady=4,padx=7,sticky='W')
    txtAddPassword.grid(column=2,row=2,pady=4)
    lblRAddPassword.grid(column=0,row=3,pady=4,padx=7,sticky='W')
    txtRAddPassword.grid(column=2,row=3,pady=4)
    btnAddNewAccount.grid(column=2,row=5,pady=25,columnspan=2)






    frmAddAccount.mainloop()



