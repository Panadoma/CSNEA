import tkinter as tk   
from tkinter import ttk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
import re
import datetime




#A simple liniar search. Given a list and a search value, output True if item found 
def LiniarSearch(items, searchValue): 
    itemFound = False
    for i in items:
        if i == searchValue:
            itemFound = True

    return itemFound




#Sort an array and output it using a bubble sort algorithm. It is used for calculating the next primary key 
def BubbleSort(Values):
    for i in range(len(Values)):
        for j in range(len(Values) - 1):
            if Values[j] > Values[j+1]:
                Values[j], Values[j+1] = Values[j+1], Values[j]





#Given an array containing a list of primary keys, it returns the next one, by incrimenting the largest primary key by one. The primary keys must be in the correct format of AA00000
def CalculateNextPrimaryKey(Values):
    nextNumber=0
    BubbleSort(Values)
    print("primary key values: "+str(Values))
    LastPrimaryKey = Values[len(Values)-1]
    print("Last primary key is: "+str(LastPrimaryKey))

    TheLetters = LastPrimaryKey[:2]
    PrimaryKeyValue= LastPrimaryKey[2:] #remove the first two letters to get a number
    if(PrimaryKeyValue.isdigit()):
        nextNumber = int(PrimaryKeyValue)+1
    else:
        print("Check the file, there is problem with the format of its primary keys")

    return (TheLetters + str(nextNumber))







#Returns a specific column of a file in the form of an array, given the file and the columnNumbeer
def LoadFileIntoArray(filePath,columnNumber):
    file = open(filePath)
    lines = file.read().splitlines()  #Load lines into an array
    primaryKeys= []
    for i in lines:
        tmp=i.split(',') #Split each line into its elemnts seperated by commas. 
        print(tmp)
        primaryKeys.append(tmp[columnNumber])    
        file.close()
    return primaryKeys


  

def LoadLineIntoArray(filePath, lineNumber):
    file = open(filePath)
    lines = file.read().splitlines()  #Load lines into an array
    file.close()
    return lines[lineNumber]
   

#This is a SHA256 hash function. Its used for the login system. 
def SHA256(TheValue):
    


        #The initial values of the hash funciton. As defult, its set to be the square root of the first primes
    h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
    hInitial=h



        #cuberoot of the first 64 primes, used as random constants
    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,0xc67178f2]





        #Rotate right bitwize function. Its a circular right shift
    def rotateRight(value, rotations, width=8):
        if int(rotations) != abs(int(rotations)):
            rotations = width + int(rotations)
        return (int(value)<<(width-(rotations%width)) | (int(value)>>(rotations%width))) & ((1<<width)-1)





            #Internal functions 
    def sigma0(value):

        #This function is defined as RotateRight(7)XOR RotateRight(18) XOR ShiftRight(3)
        v1= rotateRight(value,7,32)
        v2=rotateRight(value,18,32)
        v3=value>>3
        returnValue= v1^v2^v3
        return returnValue



    def sigma1(value):


        #This function is defined as RotateRight(17)XOR RotateRight(19) XOR ShiftRight(10)
        v1= rotateRight(value,17,32)
        v2=rotateRight(value,19,32)
        v3=value>>10
        returnValue= v1^v2^v3
        return returnValue




    def Sigma0(value):

        #This function is defined as RotateRight(2) XOR RotateRight(13) XOR RotateRight(22)
        v1= rotateRight(value,2,32)
        v2=rotateRight(value,13,32)
        v3=rotateRight(value,22,32)
        returnValue= v1^v2^v3
        return returnValue


    def Sigma1(value):

        #This function is defined as RotateRight(6) XOR RotateRight(11) XOR RotateRight(25)
        v1= rotateRight(value,6,32)
        v2=rotateRight(value,11,32)
        v3=rotateRight(value,25,32)
        returnValue= v1^v2^v3
        return returnValue






    def Choice(x,y,z):
        #Choose between two inputs(x and y) depending on the third(z)
        #ie (X or Y)XOR(NotX or Z)    in mathematical notation
        return((x&y)^(~x&z))







    def Majority(x,y,z):
        #Compare the three numbers x, y and z; for each bit output the majority
        #Formal Mathematical defenition: (X and Y) Xor (X and Z) Xor (Y and X)
        return((x&y)^(x&z)^(y&z))





    ########Start the hash process##########


    #Turn the text into assci
    ascii_values = []
    for character in TheValue:
        ascii_values.append(ord(character))

    #Store the initial length of the message
    orignalLen=len(ascii_values)

    #Apend a single 1
    ascii_values.append(0b10000000)


    #Pad 0's until multiple of 512
    varLength = len(ascii_values)
    toAdd=63-varLength
    for i in range(toAdd):
        ascii_values.append(0)


    #Apend the orignal length to the end(times by 8 since ascci is a byte)
    ascii_values.append(orignalLen*8)
    (h[4],h[5],h[6])





    ######creating message schedules
    ## Devide the message into the 16 word schedules
    WS=[]
    for i in range(0,64,4):



        #convert into binary, concatinate each group of 4, append to WS
        #0-16 the for loop is
        tmp1=int(ascii_values[i])
        tmp2=int(ascii_values[i+1])
        tmp3=int(ascii_values[i+2])
        tmp4=int(ascii_values[i+3])



        tmp1=tmp1<<24
        tmp2=tmp2<<16
        tmp3=tmp3<<8

        WB=(((tmp1|tmp2)|tmp3)|tmp4) #concatinate each group of 4
        WS.append(WB)




    #Expand the message schedules to 64 (the remaining 48)
    #Wi= sigma1(Wi-2)+Wi-7+sigma0(Wi-15)+Wi-16
    for i in range(16,64):
        newMessageSchedule=sigma1(WS[i-2])+WS[i-7]+sigma0(WS[i-15])+WS[i-16]

        #If newMessageSchedule is larger than 32 bits, the MSB's should be ignored
        mostSigBits = newMessageSchedule >>32
        newMessageSchedule = newMessageSchedule - mostSigBits
        WS.append(newMessageSchedule)







    #Compression part. The above internal functions are used to compress the message into the inital values. 
    for i in range(64):
        T1 = Sigma1(h[4]) + Choice(h[4],h[5],h[6]) + k[i] +h[7]+WS[i]
        T2 = Sigma0(h[0]) + Majority(h[0],h[1],h[2])
        T3 = T1 + T2



        #Move each value of h by one, insert T3 where h[0] use to be
        for j in range(7,0,-1):
            h[j] = h[j-1]


        h[0] = T3

        #Add T1 to the value of h[4]
        h[4] = h[4] + T1



    #Add the inital h values to the current h value, which is the last part of the hashing
    returnvalue=""
    for i in range(8):
        returnvalue=returnvalue+hex(hInitial[i]+h[i])[2:]


    return returnvalue





#
#
#         _                 _        ______                   
#        | |               (_)       |  ___|                  
#        | |     ___   __ _ _ _ __   | |_ ___  _ __ _ __ ___  
#        | |    / _ \ / _` | | '_ \  |  _/ _ \| '__| '_ ` _ \ 
#        | |___| (_) | (_| | | | | | | || (_) | |  | | | | | |
#        \_____/\___/ \__, |_|_| |_| \_| \___/|_|  |_| |_| |_|
#                      __/ |                                  
#                     |___/                                   
#
#




def ShowLoginForm():


    

    #initiolize the login form
    frmlogin =tk.Tk()
    frmlogin.title("login")
    frmlogin.geometry('400x400+50+50')
    frmlogin.resizable(False,False)
    frmlogin.configure(background='white')



    UsernameText = tk.StringVar()
    PasswordText= tk.StringVar()

    #UI wigets#
    frame = tk.Frame(frmlogin,bg='white')
    frame.place(x=110,y=100) 
    photo = tk.PhotoImage(file='./UIelements/usericon.png')
    image_label = ttk.Label(
    frame,
    image=photo,
    padding=5,
    background='white'
    )








    def LoginButtonClick():#When Login button is clicked: first the input is validated. If passed, login is attempted. If passed, the mainform is shown 
     


        enteredPassword = txtPassword.get()     
        enteredUsername = txtUsername.get() 
        
        #############Validating Username and password


        validationPassed= True
        loginSuccess= False

        #length check: 4<x<25; 
        if len(enteredUsername)>25 or len(enteredUsername)<=3 or  len(enteredPassword)<=3 or  len(enteredPassword)<=3:
            validationPassed=False  
            messagebox.showerror("Error", "Your username or password does not contain the valid length")

        #Format check: see if it contains any spaces ---> " "
        if (' ' in enteredPassword) == True or (' ' in enteredUsername) == True:
            validationPassed=False  
            messagebox.showerror("Error", "Spaces are not allowed. Please entere a valid username or password")



        
        




        #Attempt login
        if validationPassed:
            file = open("programData/HashedPasswords.txt")
            HashedPasswords = file.read().splitlines()  #Load lines into an array
            file.close()
            print(HashedPasswords)
            SaltedUsrPwd = enteredUsername+enteredPassword
            HashedUsrPwd= SHA256(SaltedUsrPwd)
            print(HashedUsrPwd)
            loginSuccess= LiniarSearch(HashedPasswords, HashedUsrPwd)#perfrom a liniar serach in order to find the matching password








        if loginSuccess:
            #ShowMainForm()
            print("login Successful")
            frmlogin.destroy()
            ShowMainForm()
        else:
            print("login Unsuccessful")
            messagebox.showwarning("Failed", "Please entere a valid username or password")


        


    ###Username Textbox
    txtUsername = tk.Entry(frame,textvariable= UsernameText)


    ###Password Textbox
    txtPassword=tk.Entry(frame, textvariable=PasswordText, show='*')#Only show * because its  a password


    ###login button####
    btnLogin = ttk.Button(
        frame,
        text='Login',   
        command= LoginButtonClick
    )




    image_label.pack()
    txtUsername.pack(padx=10)
    txtPassword.pack(pady=5)
    btnLogin.pack(pady=7,expand=True)






    frmlogin.mainloop()





#
#
#
#         _   _                ______                       _ 
#        | \ | |               | ___ \                     | |
#        |  \| | _____      __ | |_/ /___  ___ ___  _ __ __| |
#        | . ` |/ _ \ \ /\ / / |    // _ \/ __/ _ \| '__/ _` |
#        | |\  |  __/\ V  V /  | |\ \  __/ (_| (_) | | | (_| |
#        \_| \_/\___| \_/\_/   \_| \_\___|\___\___/|_|  \__,_|
#                                                             
#                                                             
#
   


def ShowAddRecordForm():

    

    #Initiolize the AddNewAccount form
    frmAddRecord = tk.Tk()
    frmAddRecord.title("Add Records")
    frmAddRecord.geometry('400x250+50+50')
    frmAddRecord.resizable(False,False)
    frmAddRecord.configure(background='white')
    #Definet he StringVars
    RecordIDText = tk.StringVar()
    DateText= tk.StringVar()
    MemberIDText= tk.StringVar()
    ActivityIDText= tk.StringVar()
   


    #Initiolize the defult values
    ActivityIDText.set("Gym") # default value

        #Today's date
    today = datetime.datetime.now()
    DateText.set(today.strftime("%x"))



    #############THE UI WIGETS########

         #The Frame#
    frame = tk.Frame(frmAddRecord,bg='white')
    frame.place(x=60,y=55)


         #Lables######
    lblRecordID= ttk.Label(
        frame,
        text='RecordID',
        background='white'
    )

    lblDate= ttk.Label(
        frame,
        text='Date',
        padding=0,
        background='white'
    )

    lblMemberID= ttk.Label(
        frame,
        text='MemberID',
        background='white'
        ) 
    lblActivity= ttk.Label(
        frame,
        text='Activity',  
        background='white'
        )

          ###Textboxes
    txtRecordID = tk.Entry(frame,textvariable=RecordIDText)
    txtDate=tk.Entry(frame, textvariable=DateText)
    txtActivityID=tk.Entry(frame, textvariable=ActivityIDText)
    txtMemberID=tk.Entry(frame, textvariable=MemberIDText)
        
####Load the the defult primary key
    primaryKeys=LoadFileIntoArray("programData/Records.txt",0)
    RecordIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
    print(CalculateNextPrimaryKey(primaryKeys))




    def BackHome():
        frmAddRecord.destroy()
        ShowMainForm()

#When the add record button is pressed ......
    def AddRecord():

        
        #Load the Strings
        RecordIDString= txtRecordID.get()
        MemberIDString= txtMemberID.get()
        DateString=txtDate.get()
        ActivityString=txtActivityID.get()

        
        #######Validate the inputs#####
        ValidationPassed= True


         
        #Format check: RecirdID in the form --> RC10000
        IDEx = re.compile('^[R][C][0-9]{5}$')
        if not re.fullmatch(IDEx,RecordIDString): 
            ValidationPassed=False 
            print("ID check not passed")
            txtRecordID.configure(bg='pink')
        

        if ValidationPassed:

                #Write to file
            with open('programData/Records.txt', 'a') as file: 
               file.write(RecordIDString+","+DateString+","+MemberIDString+","+ActivityString+"\n") 

                 #Reload everything for the next adding of a record
            MemberIDText.set("")
                        #Calculate the next primary key
            primaryKeys=LoadFileIntoArray("programData/Records.txt",0)
            RecordIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
            print(CalculateNextPrimaryKey(primaryKeys))
          


        

            messagebox.showinfo("Success", "New Record Has been added")

        else:
            messagebox.showerror("Error", "Please make sure all the entries are valid")




        

    ###Add the buttons####
    btnAddNewRecord = ttk.Button(
        frame,
        text='Add',
        command= AddRecord
    )
    btnHome= ttk.Button(
        frame,
        text='Home',
        command= BackHome
    )






    #Add the comboboxe
    cmbActivityID = tk.OptionMenu(frame, ActivityIDText, "Gym", "Swimming", "Tenis")
        #Load the primary keys of the members into the combobox
    MemberPrimaryKeys=LoadFileIntoArray("programData/Members.txt",0)
    cmbMemberID=tk.OptionMenu(frame,MemberIDText,*MemberPrimaryKeys)

    #Grid and placements
    lblRecordID.grid(column=0,row=1,padx=7,sticky='W')
    txtRecordID.grid(column=2,row=1)
    lblDate.grid(column=0,row=2,pady=4,padx=7,sticky='W')
    txtDate.grid(column=2,row=2,pady=4)
    lblMemberID.grid(column=0,row=3,pady=4,padx=7,sticky='W')
    cmbMemberID.grid(column=2,row=3,pady=4)
    lblActivity.grid(column=0,row=4,pady=4,padx=7,sticky='W')
    cmbActivityID.grid(column=2,row=4,pady=4) 
    btnAddNewRecord.grid(column=2,row=6,pady=25,columnspan=1)
    btnHome.grid(column=1,row=6,pady=25,columnspan=1)



    #Show the form
    frmAddRecord.mainloop()






#
#
#
#
#          _   _                  _____ _         __  __ 
#         | \ | |                / ____| |       / _|/ _|
#         |  \| | _____      __ | (___ | |_ __ _| |_| |_ 
#         | . ` |/ _ \ \ /\ / /  \___ \| __/ _` |  _|  _|
#         | |\  |  __/\ V  V /   ____) | || (_| | | | |  
#         |_| \_|\___| \_/\_/   |_____/ \__\__,_|_| |_|  
#                                                        
#                                                    
#
#
#



def ShowAddStaffForm():

    

    #Initiolize the form
    frmAddStaff = tk.Tk()
    frmAddStaff.title("Add Staff")
    frmAddStaff.geometry('400x370+50+50')
    frmAddStaff.resizable(False,False)
    frmAddStaff.configure(background='white')

    StaffIDText = tk.StringVar()
    NameText= tk.StringVar()
    SurnameText= tk.StringVar()
    EmailText= tk.StringVar()
    PhonnumberText= tk.StringVar()
    DOBText= tk.StringVar()
    NaNumberText= tk.StringVar()
    ExtraInfoText= tk.StringVar()


    

        #Calculate the next primary key
    primaryKeys=LoadFileIntoArray("programData/Staff.txt",0)
    StaffIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
    print(CalculateNextPrimaryKey(primaryKeys))






    def BackHome():
        frmAddStaff.destroy()
        ShowMainForm()
    def AddStaff():
     

        StaffIDString = txtStaffID.get() 
        NameString = txtName.get() 
        SurnameString = txtSurname.get()
        DOBString = txtDOB.get() 
        NaNumberString = txtNaNumber.get()
        ExtraInfoString = txtExtraInfo.get() 
        EmailString=txtEmail.get()
        PhonenumberString=txtPhonenumber.get()


        
        txtStaffID.configure(bg="white")
        txtPhonenumber.configure(bg='white')
        txtName.configure(bg='white')
        txtSurname.configure(bg='white')
        txtEmail.configure(bg='white')
        txtExtraInfo.configure(bg='white')
        txtNaNumber.configure(bg='white')
        txtDOB.configure(bg='white')



#####################Validation##############################################################33
        ValidationPassed= True

        #Length checks
        if len(NameString)>25 or len(NameString)<3:
            ValidationPassed=False
            print("Name length check not passed")
            txtName.configure(bg='pink')

        if len(SurnameString)>25 or len(SurnameString)<3:
            ValidationPassed=False

            print("Surname check not passed")
            txtSurname.configure(bg='pink')


        if not (len(PhonenumberString)==11):
            ValidationPassed=False

            print("Phone number lengthcheck not passed")
            txtPhonenumber.configure(bg='pink')







        #Format checks

        #phone number
        tmp=  PhonenumberString
        if not tmp.isdigit():
            ValidationPassed=False
            print("Is digit not passed")
            txtPhonenumber.configure(bg='pink')

        #StaffID in the form --> MB00001
        IDEx = re.compile('^[S][F][0-9]{5}$')
        if not re.fullmatch(IDEx,StaffIDString):
            ValidationPassed=False
            print("ID check not passed")
            txtStaffID.configure(bg='pink')
       #email
        emailEx = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(emailEx,EmailString):
            ValidationPassed=False
            txtEmail.configure(bg='pink')
        #DOB
        DOBEx =re.compile('^[0-3][0-9][/][0-1][0-9][/][0-9][0-9]$')
        if not re.fullmatch(DOBEx,DOBString):
            ValidationPassed=False
            txtDOB.configure(bg='pink')



        NaNoEx =re.compile('^[A-Z]{2}[0-9]{6}[A-D]$')
        if not re.fullmatch(NaNoEx,NaNumberString):
            ValidationPassed=False
            txtNaNumber.configure(bg='pink')








        

        if ValidationPassed:
                   #Write to file
            with open('programData/Staff.txt', 'a') as file: 
                file.write(StaffIDString+","+NameString+","+SurnameString+","+EmailString+','+PhonenumberString+","+DOBString+","+NaNumberString+","+txtExtraInfo.get()+"\n")


                 #Reload everything for the next adding of a record
            StaffIDText.set("")
            NameText.set("")
            EmailText.set("")
            PhonnumberText.set("")
            SurnameText.set("")
            DOBText.set("")
            NaNumberText.set("")
            ExtraInfoText.set("")
                            #Calculate the next primary key
            primaryKeys=LoadFileIntoArray("programData/Staff.txt",0)
            StaffIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
            print(CalculateNextPrimaryKey(primaryKeys))
          


        

            messagebox.showinfo("Success", "New staff member Has been added")
        
        






            



    #############THE UI WIGETS####
    #The Frame#
    frame = tk.Frame(frmAddStaff,bg='white')
    frame.place(x=65,y=55)


    #Lables######
    lblStaffID= ttk.Label(
        frame,
        text='StaffID',
        background='white'
    )

    lblName= ttk.Label(
        frame,
        text='Name',
        padding=0,
        background='white'
    )

    lblSurname= ttk.Label(
        frame,
        text='Surname',
        background='white'
        ) 
    lblDOB= ttk.Label(
        frame,
        text='Date of Birth',
        background='white'
        )

        
    lblNaNumber= ttk.Label(
        frame,
        text='Na/Number',
        background='white'
        )
        
    lblExtraInfo= ttk.Label(
        frame,
        text='Extra Info',
        background='white'
        )

    lblEmail= ttk.Label(
        frame,
        text='Email',
        background='white'
        )

    lblPhonnumber= ttk.Label(
        frame,
        text='Phone Number',
        background='white'
        )

    ###Textboxes
    txtStaffID = tk.Entry(frame,textvariable=StaffIDText)
    txtName=tk.Entry(frame, textvariable=NameText)
    txtSurname=tk.Entry(frame, textvariable=SurnameText)
    txtDOB=tk.Entry(frame, textvariable=DOBText)
    txtNaNumber=tk.Entry(frame, textvariable=NaNumberText)
    txtExtraInfo=tk.Entry(frame, textvariable=ExtraInfoText)
    txtEmail=tk.Entry(frame, textvariable= EmailText)
    txtPhonenumber=tk.Entry(frame, textvariable=PhonnumberText)

    ###Add button####
    btnAddNewStaff = ttk.Button(
        frame,
        text='Add',
        command= AddStaff
    )
    btnHome= ttk.Button(
        frame,
        text='Home',
        command= BackHome
    )




    lblStaffID.grid(column=0,row=1,padx=7,sticky='W')
    txtStaffID.grid(column=2,row=1)
    lblName.grid(column=0,row=2,pady=4,padx=7,sticky='W')
    txtName.grid(column=2,row=2,pady=4)
    lblSurname.grid(column=0,row=3,pady=4,padx=7,sticky='W')
    txtSurname.grid(column=2,row=3,pady=4)
    lblDOB.grid(column=0,row=4,pady=4,padx=7,sticky='W')
    txtDOB.grid(column=2,row=4,pady=4)
    lblEmail.grid(column=0,row=5,pady=4,padx=7,sticky='W')
    txtEmail.grid(column=2,row=5,pady=4)
    lblPhonnumber.grid(column=0,row=6,pady=4,padx=7,sticky='W')
    txtPhonenumber.grid(column=2,row=6,pady=4)
    lblNaNumber.grid(column=0,row=7,pady=4,padx=7,sticky='W')
    txtNaNumber.grid(column=2,row=7,pady=4)
    lblExtraInfo.grid(column=0,row=8,pady=4,padx=7,sticky='W')
    txtExtraInfo.grid(column=2,row=8,pady=4)
    btnAddNewStaff.grid(column=2,row=9,pady=25)
    btnHome.grid(column=1,row=9,pady=25)




    frmAddStaff.mainloop()


#
#
#
#         _____                     _      
#        /  ___|                   | |     
#        \ `--.  ___  __ _ _ __ ___| |__   
#         `--. \/ _ \/ _` | '__/ __| '_ \  
#        /\__/ /  __/ (_| | | | (__| | | | 
#        \____/ \___|\__,_|_|  \___|_| |_| 
#                                          
#                                          
#



def ShowSearchForm():

    

    #Initiolize the AddNewAccount form
    frmSearch = tk.Tk()
    frmSearch.title("Browse Files")
    frmSearch.geometry('700x700+50+50')
    frmSearch.resizable(False,False)
    frmSearch.configure(background='white')
    #Definet he StringVars
    SearchText = tk.StringVar()
    TableText = tk.StringVar()
    ColumnText= tk.StringVar()


   


    #Initiolize the defult values
    TableText.set("Select table") # default value


    #############THE UI WIGETS########

         #The Frame#
    frame = tk.Frame(frmSearch,bg='white')
    frame.place(x=60,y=55)

    lableframe = tk.Frame(frame,bg='white')


         #Lables######
    lblTable= ttk.Label(
        frame,
        text='Tables: ',
        background='white'
        ) 

    lblIn= ttk.Label(
        frame,
        text='In',
        background='white'
        ) 


          ###Textboxes
    txtSearch = tk.Entry(frame,textvariable=SearchText)


    listbox=tk.Listbox(frame)
    


    #Add the comboboxe
    cmbTable = tk.OptionMenu(frame, TableText, "Records","Staff","Members")
    cmbColumn= tk.OptionMenu(frame,ColumnText, "")
    cmbColumn.grid(column=3,row=2)

    def BackHome():
        frmSearch.destroy()
        ShowMainForm()
        
        
    def SearchPress():
    
        path =""
        Titles = []
        SearchValue= txtSearch.get()
        if TableText.get()== "Records":
            path= "programData/Records.txt"
            Titles = ['RecordID','Date','MemberID','Activity']
        if TableText.get()== "Members":
            path= "programData/Members.txt"
            Titles = ['MemberID','Name','Surname','Email','Phone','DOB','Membership', 'Extra info']
        if TableText.get()== "Staff":
            path= "programData/Staff.txt" 
            Titles = ['StaffID','Name','Surname','Email','Phone','DOB','Na#No', 'Extra info']

        index = 0
        for i in Titles:
            if i == ColumnText.get():
                break
            index= index +1
        array = LoadFileIntoArray(path,index)
        found = LiniarSearch(array,SearchValue)


        if found:
            messagebox.showinfo(":)", "The item is present in the databas")
        else:
            messagebox.showinfo("!", "The item was not found ")


        





        





    def LoadTable(*args):
        path =""
        listbox.delete(0,tk.END)
        Titles = []

        if TableText.get()== "Records":
            path= "programData/Records.txt"
            Titles = ['RecordID','Date','MemberID','Activity']
        if TableText.get()== "Members":
            path= "programData/Members.txt"
            Titles = ['MemberID','Name','Surname','Email','Phone','DOB','Membership', 'Extra info']
        if TableText.get()== "Staff":
            path= "programData/Staff.txt" 
            Titles = ['StaffID','Name','Surname','Email','Phone','DOB','Na#No', 'Extra info']
        primaryKeys= LoadFileIntoArray(path,0)
        for i in range(len(primaryKeys)):
            listbox.insert(i,primaryKeys[i])


        cmbColumn= tk.OptionMenu(frame,ColumnText,*Titles)
        cmbColumn.grid(column=3,row=2)
        print("option menue generated")







    def UpdateLable(data,index):
        theOpenTable = data[:1]
        Titles =[]
        
        if TableText.get()== "Records":
            path= "programData/Records.txt"
            Titles = ['RecordID: ','Date: ','MemberID: ','Activity: ']
        if TableText.get()== "Members":
            path= "programData/Members.txt"
            Titles = ['MemberID: ','Name: ','Surname: ','Email: ','','Phone: ','DOB: ','Membership: ', 'Extra info: ']
        if TableText.get()== "Staff":
            path= "programData/Staff.txt" 
            Titles = ['StaffID: ','Name: ','Surname: ','Email: ','Phone:  ','DOB:  ','Na#No: ', 'Extra info: ']
        primaryKeys= LoadFileIntoArray(path,0)
        for i in range(len(primaryKeys)):
            listbox.insert(i,primaryKeys[i])


        






    def UpdateLable(data,index):
        theOpenTable = data[:1]
        Titles =[]
        if theOpenTable =='R':  
            path= "programData/Records.txt"
            Titles = ['RecordID: ','Date: ','MemberID: ','Activity: ']

        
        if theOpenTable =='M':  
            path= "programData/Members.txt"
            Titles = ['MemberID: ','Name: ','Surname: ','Email: ','','Phone: ','DOB: ','Membership: ', 'Extra info: ']


        if theOpenTable =='S':  
            path= "programData/Staff.txt"
            Titles = ['StaffID: ','Name: ','Surname: ','Email: ','Phone:  ','DOB:  ','Na#No: ', 'Extra info: ']


        array1=LoadLineIntoArray(path,index)
        array2= array1.split(",")
        
        j=0
        for widget in lableframe.winfo_children():
            widget.destroy()
        for i in array2:
            print(i)
            tmpStr=Titles[j]+str(i)
            lbltmp= ttk.Label(lableframe,text=tmpStr,background='white')
            lbltmp.grid(column=0,row=j,sticky= 'W')
            j=j+1
            

        


        print(array2)

    def ListBoxClicked(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            print(data)
            listboxvalue=data
            UpdateLable(data,index)
      
   


    






    TableText.trace("w", LoadTable)
        

    ###Add the buttons#### 
    btnSearch= ttk.Button(
        frame,
        text='Search',
        command= SearchPress
    )
    btnHome= ttk.Button(
        frame,
        text='Home',
        command= BackHome
    )

    ####Add the listbox
    listbox.bind("<<ListboxSelect>>", ListBoxClicked)






    #Grid and placements
    lblTable.grid(column=0,row=1,padx=7,sticky='W')
    cmbTable.grid(column=1,row=1)
    txtSearch.grid(column=0,row=2,padx='4',pady=4)
    btnSearch.grid(column=1,row=2,pady=4)
    lblIn.grid(column=2,row=2)
    listbox.grid(column=0,row=3,pady=25)
    lableframe.grid(column=3,row=3)
    btnHome.grid(column=0,row=4,pady=25)

    

    #Show the form
    frmSearch.mainloop()






#                                ___                            _   
#                               / _ \                          | |  
#         _ __   _____      __ / /_\ \ ___ ___ ___  _   _ _ __ | |_ 
#        | '_ \ / _ \ \ /\ / / |  _  |/ __/ __/ _ \| | | | '_ \| __|
#        | | | |  __/\ V  V /  | | | | (_| (_| (_) | |_| | | | | |_ 
#        |_| |_|\___| \_/\_/   \_| |_/\___\___\___/ \__,_|_| |_|\__|
#                                                                   
#                                                                   
#
#
#


def ShowAddAccountForm():



    #Initiolize the AddNewAccount form
    frmAddAccount =tk.Tk()
    frmAddAccount.title("Add Users")
    frmAddAccount.geometry('400x250+50+50')
    frmAddAccount.resizable(False,False)
    frmAddAccount.configure(background='white')


    Usernametext = tk.StringVar()
    PasswordText= tk.StringVar()
    rPasswordText= tk.StringVar()



    def BackHome():
        frmAddAccount.destroy()
        ShowMainForm()

    def AddAccount():#When the add button is pressed


        #Validation

        validationPassed=True
        #length check: 4<x<25;
        if len(txtAddPassword.get() )>25 or len(txtAddPassword.get() )<=3 or  len(txtAddUsername.get())<=3 or  len( txtAddUsername.get())<=3:
            validationPassed=False
            messagebox.showerror("Error", "Your username and password have to meet the valid length")

        #Format check: see if it contains any spaces ---> " "
        if (' ' in txtAddPassword.get()) == True or (' ' in txtAddUsername.get()) == True:
            validationPassed=False
            messagebox.showerror("Error", "Spaces are not allowed")

        #Do the Passwords match
        if not(txtAddPassword.get() == txtRAddPassword.get()):
            messagebox.showerror("Error", "Passwords do not match")
            validationPassed=False







        if validationPassed:
            #Salt the username and password, then hash it
            SaltedPassword = txtAddUsername.get()+ txtAddPassword.get()
            print("salted password is:"+str(SaltedPassword ))
            HashedPassword= SHA256(SaltedPassword)

            print("Validation Passed")

            with open('programData/HashedPasswords.txt', 'a') as file:
                HashedPassword=HashedPassword + '\n'
                file.write(HashedPassword)

                print("Password added ")


                messagebox.showinfo("Success", "New username and password has been added")



            BackHome()





















    #############THE UI WIGETS####
    #The Frame#
    frame = tk.Frame(frmAddAccount,bg='white')
    frame.place(x=30,y=55)


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
    btnBackHome = ttk.Button(
        frame,
        text='Home',
        command= BackHome
    )





    #Grid and placements
    lblUsername.grid(column=0,row=1,padx=7,sticky='W')
    txtAddUsername.grid(column=2,row=1)
    lblPassword.grid(column=0,row=2,pady=4,padx=7,sticky='W')
    txtAddPassword.grid(column=2,row=2,pady=4)
    lblRAddPassword.grid(column=0,row=3,pady=4,padx=7,sticky='W')
    txtRAddPassword.grid(column=2,row=3,pady=4)
    btnAddNewAccount.grid(column=2,row=5,pady=25,columnspan=2)
    btnBackHome.grid(column=1,row=5,pady=25)






    frmAddAccount.mainloop()
















#      _   _                 __  __                _               
#     | \ | |               |  \/  |              | |              
#     |  \| | _____      __ | \  / | ___ _ __ ___ | |__   ___ _ __ 
#     | . ` |/ _ \ \ /\ / / | |\/| |/ _ \ '_ ` _ \| '_ \ / _ \ '__|
#     | |\  |  __/\ V  V /  | |  | |  __/ | | | | | |_) |  __/ |   
#     |_| \_|\___| \_/\_/   |_|  |_|\___|_| |_| |_|_.__/ \___|_|   
#                                                                  
#    
#
def ShowNewMemberForm():



    #Initiolize the form
    frmNewMemberForm = tk.Tk()
    frmNewMemberForm.title("Add Users")
    frmNewMemberForm.geometry('400x350+50+50')
    frmNewMemberForm.resizable(False,False)
    frmNewMemberForm.configure(background='white')
    #Define the String vars
    MemberIDText = tk.StringVar()
    NameText= tk.StringVar()
    EmailText= tk.StringVar()
    PhonnumberText= tk.StringVar()
    SurnameText= tk.StringVar()
    DOBText= tk.StringVar()
    MembershipText= tk.StringVar()
    ExtraInfoText= tk.StringVar()
    #Initiolize the defult values
    MembershipText.set("Gold") # default value  

    #############THE UI WIGETS####
        #The Frame#
    frame = tk.Frame(frmNewMemberForm,bg='white')
    frame.place(x=30,y=55)

        #Lables######
    lblMemberID= ttk.Label(
        frame,
        text='MemberID',
        background='white'
    )

    lblName= ttk.Label(
        frame,
        text='Name',
        padding=0,
        background='white'
    )

    lblSurname= ttk.Label(
        frame,
        text='Surname',
        background='white'
        )
    lblDOB= ttk.Label(
        frame,
        text='DOB (dd/mm/yy)',
        background='white'
        )


    lblMembershipID= ttk.Label(

        frame,
        text='Membership Type',
        background='white'
        )


    lblEmail= ttk.Label(
        frame,
        text='Email',
        background='white'
        )

    lblPhonnumber= ttk.Label(
        frame,
        text='Phone Number',
        background='white'
        )

    lblExtraInfo= ttk.Label(
        frame,
        text='Extra Info',
        background='white'
        )



        ###Textboxes
    txtMemberID = tk.Entry(frame,textvariable= MemberIDText)
    txtName=tk.Entry(frame, textvariable= NameText)
    txtSurname=tk.Entry(frame, textvariable= SurnameText)
    txtDOB=tk.Entry(frame, textvariable=DOBText)
    txtEmail=tk.Entry(frame, textvariable= EmailText)
    txtPhonenumber=tk.Entry(frame, textvariable=PhonnumberText)
    txtMembershipID=tk.Entry(frame, textvariable= MembershipText)
    txtExtraInfo=tk.Entry(frame, textvariable= ExtraInfoText)

    #ComboBOX (drop down menu)
    cmbMembership = tk.OptionMenu(frame, MembershipText, "Gold", "Silver", "Bronz")





    #Calculate the next primary key
    def NextPK():
        file = open("programData/Members.txt")
        lines = file.read().splitlines()  #Load lines into an array
        primaryKeys= []
        for i in lines:
            tmp=i.split(',') #Split each line into its elemnts seperated by commas.
            print(tmp)
            primaryKeys.append(tmp[0])
    #Caclutate the date and display it as default

    #Calutlate the next MemberID

    #Calculate the next

    #Grid and placements



        print("Primary keys are: "+str(primaryKeys))
        file.close()
        MemberIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function




    NextPK()#Call the next primary key function











    def BackHome():
        frmNewMemberForm.destroy()
        ShowMainForm()

    def AddMember():


        MemberIDString = txtMemberID.get()
        NameString=txtName.get()
        SurnameString=txtSurname.get()
        EmailString=txtEmail.get()
        PhonenumberString=txtPhonenumber.get()
        DOBString=txtDOB.get()
        MembershipString=txtMembershipID.get()

        #revert the colours in case they have been changed
        ExtraInfoString=txtExtraInfo.get()
        txtMemberID.configure(bg="white")
        txtPhonenumber.configure(bg='white')
        txtName.configure(bg='white')
        txtSurname.configure(bg='white')
        txtEmail.configure(bg='white')
        txtExtraInfo.configure(bg='white')
        txtDOB.configure(bg='white')


#####################Validation##############################################################33
        ValidationPassed= True

        #Length checks
        if len(NameString)>25 or len(NameString)<3:
            ValidationPassed=False
            print("Name length check not passed")
            txtName.configure(bg='pink')

        if len(SurnameString)>25 or len(SurnameString)<3:
            ValidationPassed=False

            print("Surname check not passed")
            txtSurname.configure(bg='pink')


        if not (len(PhonenumberString)==11):
            ValidationPassed=False

            print("Phone number lengthcheck not passed")
            txtPhonenumber.configure(bg='pink')







        #Format checks

        #phone number
        tmp=  PhonenumberString
        if not tmp.isdigit():
            ValidationPassed=False
            print("Is digit not passed")
            txtPhonenumber.configure(bg='pink')

        #MemberID in the form --> MB00001
        IDEx = re.compile('^[M][B][0-9]{5}$')
        if not re.fullmatch(IDEx,MemberIDString):
            ValidationPassed=False
            print("ID check not passed")
            txtMemberID.configure(bg='pink')
       #email
        emailEx = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(emailEx,EmailString):
            ValidationPassed=False
            txtEmail.configure(bg='pink')
        #DOB
        DOBEx =re.compile('^[0-3][0-9][/][0-1][0-9][/][0-9][0-9]$')
        if not re.fullmatch(DOBEx,DOBString):
            ValidationPassed=False
            txtDOB.configure(bg='pink')









 ###############Write to file#################

        if ValidationPassed:
           with open('programData/Members.txt', 'a') as file:
               file.write(MemberIDString+","+NameString+","+SurnameString+","+EmailString+','+PhonenumberString+","+DOBString+","+MembershipString+","+txtExtraInfo.get()+"\n")

           #Reload everything for the next adding of a record
           MemberIDText.set("")
           NameText.set("")
           EmailText.set("")
           PhonnumberText.set("")
           SurnameText.set("")
           DOBText.set("")
           MembershipText.set("Gold")
           ExtraInfoText.set("")
           NextPK()#Load the next default primary key

           messagebox.showinfo("Success", "The new member has been added!")
        else:
            messagebox.showerror("Error", "Please make sure all the entries are valid")





    ###Add button####
    btnAddNewMember = ttk.Button(
        frame,
        text='Add',
        command= AddMember
    )
    btnHome= ttk.Button(
        frame,
        text='Home',
        command= BackHome
    )

    #Grid and placement
    lblMemberID.grid(column=0,row=1,padx=7,sticky='W')
    txtMemberID.grid(column=2,row=1)
    lblName.grid(column=0,row=2,pady=4,padx=7,sticky='W')
    txtName.grid(column=2,row=2,pady=4)
    lblSurname.grid(column=0,row=3,pady=4,padx=7,sticky='W')
    txtSurname.grid(column=2,row=3,pady=4)
    lblEmail.grid(column=0,row=4,pady=4,padx=7,sticky='W')
    txtEmail.grid(column=2,row=4,pady=4)
    lblPhonnumber.grid(column=0,row=5,pady=4,padx=7,sticky='W')
    txtPhonenumber.grid(column=2,row=5,pady=4)
    lblDOB.grid(column=0,row=6,pady=4,padx=7,sticky='W')
    txtDOB.grid(column=2,row=6,pady=4)
    lblMembershipID.grid(column=0,row=7,pady=4,padx=7,sticky='W')
    cmbMembership.grid(column=2,row=7,pady=4)
    lblExtraInfo.grid(column=0,row=8,pady=4,padx=7,sticky='W')
    txtExtraInfo.grid(column=2,row=8,pady=4)
    btnAddNewMember.grid(column=2,row=9,pady=30)
    btnHome.grid(column=1, row=9, pady=30)




    frmNewMemberForm.mainloop()








#  _____ _                     _____ _                          ______                   
# /  ___| |                   /  __ \ |                         |  ___|                  
# \ `--.| |__   _____      __ | /  \/ | __ _ ___ ___  ___  ___  | |_ ___  _ __ _ __ ___  
#  `--. \ '_ \ / _ \ \ /\ / / | |   | |/ _` / __/ __|/ _ \/ __| |  _/ _ \| '__| '_ ` _ \ 
# /\__/ / | | | (_) \ V  V /  | \__/\ | (_| \__ \__ \  __/\__ \ | || (_) | |  | |            \____/|_| |_|\___/ \_/\_/    \____/_|\__,_|___/___/\___||___/ \_| \___/|_|  |_| |_| |_,                                                                                               
#                                                                                                 






def ShowClassesForm():


  #Initiolize the AddNewClasses form
    frmAddClass = tk.Tk()
    frmAddClass.title("Add new Classes")
    frmAddClass.geometry('400x320+50+50')
    frmAddClass.resizable(False,False)
    frmAddClass.configure(background='white')
    #Definet he StringVars
    ClassIDText = tk.StringVar()
    TitleText = tk.StringVar()
    DateText= tk.StringVar()
    StaffIDText= tk.StringVar()
   



        #Today's date
    today = datetime.datetime.now()
    DateText.set(today.strftime("%x"))



    #############THE UI WIGETS########

         #The Frame#
    frame = tk.Frame(frmAddClass,bg='white')
    frame.place(x=60,y=55)


         #Lables######
    lblClassID= ttk.Label(
        frame,
        text='ClassID',
        background='white'
    )

    lblTitle= ttk.Label(
        frame,
        text='Title',
        background='white'
    )
    lblDate= ttk.Label(
        frame,
        text='Date',
        padding=0,
        background='white'
    )

    lblStaffID= ttk.Label(
        frame,
        text='Teacher',
        background='white'
        ) 

          ###eextboxes
    txtClassID = tk.Entry(frame,textvariable=ClassIDText)
    txtTitle = tk.Entry(frame,textvariable=TitleText)
    txtDate=tk.Entry(frame, textvariable=DateText)
    txtStaffID=tk.Entry(frame, textvariable=StaffIDText)
        
####Load the the defult primary key
    primaryKeys=LoadFileIntoArray("programData/Classes.txt",0)
    ClassIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
    print(CalculateNextPrimaryKey(primaryKeys))




    def BackHome():
        frmAddClass.destroy()
        ShowMainForm()

#When the add record button is pressed ......
    def AddClass():

        
        #Load the Strings
        ClassIDString= txtClassID.get()
        TitleString= txtClassID.get()
        StaffIDString= txtStaffID.get()
        DateString=txtDate.get()

        
        #######Validate the inputs#####
        ValidationPassed= True


         
        #Format check: RecirdID in the form --> RC10000
        IDEx = re.compile('^[C][L][0-9]{5}$')
        if not re.fullmatch(IDEx,ClassIDString): 
            ValidationPassed=False 
            print("ID check not passed")
            txtClassID.configure(bg='pink')
        

        if ValidationPassed:

                #Write to file
            with open('programData/Classes.txt', 'a') as file: 
               file.write(ClassIDString+","+TitleString+","+DateString+","+StaffIDString+","+"\n") 

                 #Reload everything for the next adding of a record
            StaffIDText.set("")
            TitleText.set("")
                        #Calculate the next primary key
            primaryKeys=LoadFileIntoArray("programData/Classes.txt",0)
            ClassIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
            print(CalculateNextPrimaryKey(primaryKeys))
          


        

            messagebox.showinfo("Success", "New Class Has been added")

        else:
            messagebox.showerror("Error", "Please make sure all the entries are valid")




        

    ###Add the buttons####
    btnAddNewClass = ttk.Button(
        frame,
        text='Add',
        command= AddClass
    )
    btnHome= ttk.Button(
        frame,
        text='Home',
        command= BackHome
    )






        #Load the primary keys of the staffs into the combobox
    StaffPrimaryKeys=LoadFileIntoArray("programData/Staff.txt",0)
    cmbStaffID=tk.OptionMenu(frame,StaffIDText,*StaffPrimaryKeys)

    #Grid and placements
    lblClassID.grid(column=0,row=1,padx=7,sticky='W')
    txtClassID.grid(column=2,row=1)
    lblTitle.grid(column=0,row=2,padx=7,sticky='W')
    txtTitle.grid(column=2,row=2,pady=4)
    lblDate.grid(column=0,row=3,pady=4,padx=7,sticky='W')
    txtDate.grid(column=2,row=3,pady=4)
    lblStaffID.grid(column=0,row=4,pady=4,padx=7,sticky='W')
    cmbStaffID.grid(column=2,row=4,pady=4)
    btnAddNewClass.grid(column=2,row=6,pady=25,columnspan=1)
    btnHome.grid(column=1,row=6,pady=25,columnspan=1)



    #Show the form
    frmAddClass.mainloop()















#
#     ____  _                     _____       _                _____                    
#    / ___|| |__   _____      __ | ____|_ __ | |_ _ __ _   _  |  ___|__  _ __ _ __ ___  
#    \___ \| '_ \ / _ \ \ /\ / / |  _| | '_ \| __| '__| | | | | |_ / _ \| '__| '_ ` _ \ 
#     ___) | | | | (_) \ V  V /  | |___| | | | |_| |  | |_| | |  _| (_) | |  | | | | | |
#    |____/|_| |_|\___/ \_/\_/   |_____|_| |_|\__|_|   \__, | |_|  \___/|_|  |_| |_| |_|
#                                                          |___/                
#
def ShowEntryForm():
    #Initiolize the AddNewAccount form
    frmAddMemberToClass = tk.Tk()
    frmAddMemberToClass.title("Add Users")
    frmAddMemberToClass.geometry('400x250+50+50')
    frmAddMemberToClass.resizable(False,False)
    frmAddMemberToClass.configure(background='white')
    #Definet he StringVars
    EntryIDText = tk.StringVar()
    MemberIDText= tk.StringVar()
    ClassIDText= tk.StringVar()
   




    #############THE UI WIGETS########

         #The Frame#
    frame = tk.Frame(frmAddMemberToClass,bg='white')
    frame.place(x=60,y=55)


         #Lables######
    lblEntryID= ttk.Label(
        frame,
        text='EntryID',
        background='white'
    )

    lblClassID= ttk.Label(
        frame,
        text='ClassID',
        background='white'
    )
    lblMemberID= ttk.Label(
        frame,
        text='MemberID',
        background='white'
        ) 
          

    ###Textboxes
    txtEntryID = tk.Entry(frame,textvariable=EntryIDText)
    txtMemberID=tk.Entry(frame, textvariable=MemberIDText)
    txtClassID=tk.Entry(frame, textvariable=ClassIDText)
        
####Load the the defult primary key
    primaryKeys=LoadFileIntoArray("programData/MemberToClass.txt",0)
    EntryIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
    print(CalculateNextPrimaryKey(primaryKeys))


    def BackHome():
        frmAddMemberToClass.destroy()
        ShowMainForm()



#When the add record button is pressed ......
    def AddEntry():

        
        #Load the Strings
        EntryIDString= txtEntryID.get()
        MemberIDString= txtMemberID.get()
        ClassIDString= txtClassID.get()

        
        #######Validate the inputs#####
        ValidationPassed= True


         
        #Format check: RecirdID in the form --> RC10000
        IDEx = re.compile('^[E][N][0-9]{5}$')
        if not re.fullmatch(IDEx,EntryIDString): 
            ValidationPassed=False 
            print("ID check not passed")
            txtEntryID.configure(bg='pink')
        

        if ValidationPassed:

                #Write to file
            with open('programData/MemberToClass.txt', 'a') as file: 
               file.write(EntryIDString+","+ClassIDString+","+MemberIDString+"\n") 

                 #Reload everything for the next adding of a record
            MemberIDText.set("")
                        #Calculate the next primary key
            primaryKeys=LoadFileIntoArray("programData/MemberToClass.txt",0)
            EntryIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
            print(CalculateNextPrimaryKey(primaryKeys))
          


        

            messagebox.showinfo("Success", "New Entry Has been added")

        else:
            messagebox.showerror("Error", "Please make sure all the entries are valid")




        

    ###Add the buttons####
    btnAddNewRecord = ttk.Button(
        frame,
        text='Add',
        command= AddEntry
    )
    btnHome= ttk.Button(
        frame,
        text='Home',
        command= BackHome
    )






        #Load the primary keys of the members into the combobox
    MemberPrimaryKeys=LoadFileIntoArray("programData/Members.txt",0)
    cmbMemberID=tk.OptionMenu(frame,MemberIDText,*MemberPrimaryKeys)


        #Load the primary keys of the classes into the combobox
    ClassesPrimaryKeys=LoadFileIntoArray("programData/Classes.txt",0)
    cmbClassID=tk.OptionMenu(frame,ClassIDText,*ClassesPrimaryKeys)

    #Grid and placements
    lblEntryID.grid(column=0,row=1,padx=7,sticky='W')
    txtEntryID.grid(column=2,row=1)
    lblMemberID.grid(column=0,row=3,pady=4,padx=7,sticky='W')
    cmbMemberID.grid(column=2,row=3,pady=4)
    lblClassID.grid(column=0,row=4,pady=4,padx=7,sticky='W')
    cmbClassID.grid(column=2,row=4,pady=4)
    btnAddNewRecord.grid(column=2,row=6,pady=25,columnspan=1)
    btnHome.grid(column=1,row=6,pady=25,columnspan=1)



    #Show the form
    frmAddMemberToClass.mainloop()























#
#
#                                                                                    
#          __  __       _         _____                    
#         |  \/  | __ _(_)_ __   |  ___|__  _ __ _ __ ___  
#         | |\/| |/ _` | | '_ \  | |_ / _ \| '__| '_ ` _ \ 
#         | |  | | (_| | | | | | |  _| (_) | |  | | | | | |
#         |_|  |_|\__,_|_|_| |_| |_|  \___/|_|  |_| |_| |_|
#                                                          
#
#    #
#    
#

#The main form is the form that is showed when the user logs in. It doesn't do any computations, merely acting as a menue. Each button opens up another form 
def ShowMainForm():
    



    #Initiolize the AddNewAccount form
    frmMain =tk.Tk()
    frmMain.title("Main Menu")
    frmMain.geometry('280x140+50+50')
    frmMain.resizable(False,False)
    frmMain.configure(background='white') 

    #Define the Stringvar's 
    Usernametext = tk.StringVar()
    PasswordText= tk.StringVar()
    rPasswordText= tk.StringVar()

    #Define the images
    userAdd48 = tk.PhotoImage(file='./UIelements/UserAdd48.png') 
    staffAdd48 = tk.PhotoImage(file='./UIelements/StaffAdd48.png')
    memberAdd48 = tk.PhotoImage(file='./UIelements/MembersAdd48.png')
    recordAdd48 = tk.PhotoImage(file='./UIelements/folderAdd48')
    Searching= tk.PhotoImage(file='./UIelements/Search.png') 
    Entryimg= tk.PhotoImage(file='./UIelements/Entry.png') 
    Classimg= tk.PhotoImage(file='./UIelements/Classes.png') 
    
    
    




    #When the buttons are pressed
    
    def NewAccount():   
        frmMain.destroy()
        ShowAddAccountForm()
    def NewStaff():
        frmMain.destroy()
        ShowAddStaffForm()
    def NewMember():    
        frmMain.destroy()
        ShowNewMemberForm()
    def NewRecord():
        frmMain.destroy()
        ShowAddRecordForm()
    def Srch(): 
        frmMain.destroy()
        ShowSearchForm()        
    def NewClass(): 
        frmMain.destroy()
        ShowClassesForm() 
    def NewEntry(): 
        frmMain.destroy()
        ShowEntryForm()
            
            
            
            
            
            
            
            
            
           

            



    #############THE UI WIGETS########
    #The Frame#
    frame = tk.Frame(frmMain,bg='white')
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


    btnSearch= ttk.Button(
        frame,
        image= Searching,
        text=' ',
        command= Srch
    )
    
    btnClass= ttk.Button(
        frame,
        image= Classimg,
        text=' ',
        command= NewClass
    )


    btnEntry= ttk.Button(
        frame,
        image= Entryimg,
        text=' ',
        command= NewEntry
    )
    #Tool tips (when hovering the mouse over the butons a text is showed)
    myTip = Hovertip(btnNewAccount,'Add a new account')
    myTip2 = Hovertip(btnNewStaff,'Add a new member of staff')
    myTip3 = Hovertip(btnNewRecord,'Add a new record')
    myTip4 = Hovertip(btnNewMember,'Add a member')
    myTip5 = Hovertip(btnSearch,'Browse the files')
    myTip6 = Hovertip(btnEntry,'Enter members into classes')
    myTip7 = Hovertip(btnClass,'Add a new Class')









    #Grid and placement
    btnNewAccount.grid(column=2,row=1,pady=2,padx=2)
    btnNewStaff.grid(column=3,row=1,pady=2,padx=2)
    btnNewRecord.grid(column=4,row=1,pady=2,padx=2)
    btnNewMember.grid(column=5,row=1,pady=2,padx=2)
    btnSearch.grid(column=2,row=2,pady=2,padx=2)
    btnEntry.grid(column=3,row=2,pady=2,padx=2)
    btnClass.grid(column=4,row=2,pady=2,padx=2)

    #Show the form
    frmMain.mainloop()




























ShowLoginForm()






