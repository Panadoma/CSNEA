import tkinter as tk   
import main
from tkinter import ttk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
import re

#Variables









#frmlogin.iconbitmap('./assets/sdf.ico')




#FUNCTIONS
###################################
def LiniarSearch(items, searchValue): #A general linar serach algorithm
    itemFound = False
    for i in items:
        if i == searchValue:
            itemFound = True
        
    return itemFound  




def BubbleSort(Values):
    for i in range(len(Values)):
        for j in range(len(Values) - 1):
            if Values[j] > Values[j+1]:
                Values[j], Values[j+1] = Values[j+1], Values[j]




def CalculateNextPrimaryKey(Values):
    nextNumber=0
    BubbleSort(Values)
    print(Values)
    LastPrimaryKey = Values[len(Values)-1]
    print("Last primary key is :"+str(LastPrimaryKey))

    TheLetters = LastPrimaryKey[:2]
    PrimaryKeyValue= LastPrimaryKey[2:] #remove the first two letters to get a number
    if(PrimaryKeyValue.isdigit()):
        nextNumber = int(PrimaryKeyValue)+1
    else:
        print("Check the file, there is problem with the format of its primary keys")

    return (TheLetters + str(nextNumber))









#This is the SHA256 Hashing function.

def SHA256(TheValue):

    h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
    hInitial=h

    #cuberoot of the first 64 primes, used as random constants


    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,0xc67178f2]





    #Bitwize functions 
    def rotateRight(value, rotations, width=8):
        #Circular shift right  
       
        if int(rotations) != abs(int(rotations)):
            rotations = width + int(rotations)
        return (int(value)<<(width-(rotations%width)) | (int(value)>>(rotations%width))) & ((1<<width)-1)





    #Internal Functions
    def sigma0(value):
       
        #Xor rotate 7, rotate18,sr 3
        v1= rotateRight(value,7,32)
        v2=rotateRight(value,18,32)
        v3=value>>3
       # print("v1 rotate right 7,",bin(v1))
       # print("v2, rotate 18," ,bin(v2))
        #print("v3 the shift right 3,", bin(v3))
        returnValue= v1^v2^v3
        return returnValue



    def sigma1(value):
       
        v1= rotateRight(value,17,32)
        v2=rotateRight(value,19,32)
        v3=value>>10
        #print("v1 rotate right 17,",bin(v1))
        #print("v2, rotate 19," ,bin(v2))
        #print("v3 the shift right 10,", bin(v3))
        returnValue= v1^v2^v3
        return returnValue




    def Sigma0(value):
       
        #Xor rotate 2, rotate 13, rotate 22
        v1= rotateRight(value,2,32)
        v2=rotateRight(value,13,32)
        v3=rotateRight(value,22,32)
       # print("v1 rotate  2,",bin(v1))
       # print("v2, rotate 13," ,bin(v2))
       # print("v3 rotate 22", bin(v3))
        returnValue= v1^v2^v3
        return returnValue


    def Sigma1(value):
       
        #Xor rotate 6, rotate 11, rotate 25
        v1= rotateRight(value,6,32)
        v2=rotateRight(value,11,32)
        v3=rotateRight(value,25,32)
       # print("v1 rotate  6,",bin(v1))
       # print("v2, rotate 11," ,bin(v2))
       # print("v3 rotate 25", bin(v3))
        returnValue= v1^v2^v3
        return returnValue






    def Choice(x,y,z):
        #Choose between two inputs(x and y) depending on the third(z)
        #ie (X or Y)XOR(NotX or Z)    in mathematical notation
        return((x&y)^(~x&z))







    def Majority(x,y,z):
        #compare the three numbers x, y and z; for each bit output the majority
        #ie (X and Y) Xor (X and Z) Xor (Y and X)
        return((x&y)^(x&z)^(y&z))
       




    #Start the hash process
   

    ascii_values = []
    for character in TheValue:
        ascii_values.append(ord(character))
    #turn the text into assci

    orignalLen=len(ascii_values)

    #apend a 1

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
    #the first 16 ws
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
       # print(bin(WB))



       
    #Expand the message schedules to 64 (the remaining 48)
    #Wi= sigma1(Wi-2)+Wi-7+sigma0(Wi-15)+Wi-16


    for i in range(16,64):
        newMessageSchedule=sigma1(WS[i-2])+WS[i-7]+sigma0(WS[i-15])+WS[i-16]
        #if newMessageSchedule is larger than 32 bits, the MSB's should be ignored
        mostSigBits = newMessageSchedule >>32
        newMessageSchedule = newMessageSchedule - mostSigBits
        WS.append(newMessageSchedule)
        #testing required deoes this section work
       
       


       
       

    #Compression

    for i in range(64):
        T1= Sigma1(h[4]) + Choice(h[4],h[5],h[6]) + k[i] +h[7]+WS[i]
        T2= Sigma0(h[0]) + Majority(h[0],h[1],h[2])
        T3 = T1 + T2
       
       

        #Move each value of h by one, insert T3 where h[0] use to be
        for j in range(7,0,-1):
            h[j]=h[j-1]

       
        h[0]=T3

        #Add T1 to the value of h[4]

        h[4]=h[4]+T1



    #Add the inital h values to the current h value, to complete the hash


    returnvalue=""
    for i in range(8):
        returnvalue=returnvalue+hex(hInitial[i]+h[i])[2:]
       
       
    return returnvalue





def ShowNewMemberForm():

    

    #Initiolize the AddNewAccount form
    frmAddMember = tk.Tk()
    frmAddMember.title("Add Users")
    frmAddMember.geometry('400x350+50+50')
    frmAddMember.resizable(False,False)
    frmAddMember.configure(background='white')

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
    frame = tk.Frame(frmAddMember,bg='white')
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

            
        print("Primary keys are: "+str(primaryKeys))
        file.close()
        MemberIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
        print("MemberIDText set to "+str(CalculateNextPrimaryKey(primaryKeys)))




    NextPK()#Call the next primary key function
            
    


    


    def BackHome():
        frmAddMember.destroy()
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
 
            print("Email type check not passed")
            txtSurname.configure(bg='pink')
        #DOB
        DOBEx =re.compile('^[0-3][0-9][/][0-1][0-9][/][0-9][0-9]$')
        if not re.fullmatch(DOBEx,DOBString):
            ValidationPassed=False
            txtDOB.configure(bg='pink')




        #Type checks

        #phone number
        tmp=  PhonenumberString
        if not tmp.isdigit():
            ValidationPassed=False
            print("Is digit not passed")
            txtPhonenumber.configure(bg='pink')
            




        

            
            

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
    btnHome = ttk.Button(
        frame,
        text='Home',
        command= BackHome
    )



    #Caclutate the date and display it as default

    #Calutlate the next MemberID

    #Calculate the next 

    #Grid and placements

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
    btnAddNewMember.grid(column=2,row=9,pady=15)
    btnHome.grid(column=1,row=9,pady=15)





    frmAddMember.mainloop()



















def ShowMainForm():

    #Initiolize the form
    frm =tk.Tk()
    frm.title("Main Menu")
    frm.geometry('280x140+50+50')
    frm.resizable(False,False)
    frm.configure(background='white')
    
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
        ShowAddUserForm()
    def NewStaff():
        a=0
    def NewMember():

        frm.destroy()
        ShowNewMemberForm()
    def NewRecord():
        ShowAddRecordForm()
    def SrchStaff():
        a=0
    def SrchMember():
        a=0
    def SrchRecord():
        a=0 

    

    #############THE UI WIGETS####
    #The Frame#
    frame = tk.Frame(frm,bg='white')
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


    
    #Tool tips
    myTip = Hovertip(btnNewAccount,'Add a new account')
    myTip2 = Hovertip(btnNewStaff,'Add a new member of staff')
    myTip3 = Hovertip(btnNewRecord,'Add a new record')
    myTip4 = Hovertip(btnNewMember,'Add a member')
    myTip5 = Hovertip(btnSearchStaff,'Browse the staff')
    myTip6 = Hovertip(btnSearchRecord,'Browse the records')
    myTip7 = Hovertip(btnSearchMember,'Brorwse the members')

  

    btnNewAccount.grid(column=2,row=1,pady=2,padx=2)
    btnNewStaff.grid(column=3,row=1,pady=2,padx=2)
    btnNewRecord.grid(column=4,row=1,pady=2,padx=2)
    btnNewMember.grid(column=5,row=1,pady=2,padx=2)


    btnSearchStaff.grid(column=3,row=2,pady=2,padx=2)
    btnSearchRecord.grid(column=4,row=2,pady=2,padx=2)
    btnSearchMember.grid(column=5,row=2,pady=2,padx=2)






    frm.mainloop()








def ShowNewMemberForm():

    

    #Initiolize the AddNewAccount form
    frmAddMember = tk.Tk()
    frmAddMember.title("Add Users")
    frmAddMember.geometry('400x350+50+50')
    frmAddMember.resizable(False,False)
    frmAddMember.configure(background='white')

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
    frame = tk.Frame(frmAddMember,bg='white')
    frame.place(x=60,y=55)




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

            
        print("Primary keys are: "+str(primaryKeys))
        file.close()
        MemberIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
        print("MemberIDText set to "+str(CalculateNextPrimaryKey(primaryKeys)))




    NextPK()#Call the next primary key function
            
    


    







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
 
            print("Email type check not passed")
            txtEmail.configure(bg='pink')
        #DOB
        DOBEx =re.compile('^[0-3][0-9][/][0-1][0-9][/][0-9][0-9]$')
        if not re.fullmatch(DOBEx,DOBString):
            ValidationPassed=False
            txtDOB.configure(bg='pink')




        #Type checks

        #phone number
        tmp=  PhonenumberString
        if not tmp.isdigit():
            ValidationPassed=False
            print("Is digit not passed")
            txtPhonenumber.configure(bg='pink')
            




        

            
            

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


    #Caclutate the date and display it as default

    #Calutlate the next MemberID

    #Calculate the next 

    #Grid and placements

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
    btnAddNewMember.grid(column=2,row=9,pady=10)




    frmAddMember.mainloop()

































def ShowAddRecordForm():

    

    #Initiolize the AddNewAccount form
    frmAddRecord = tk.Tk()
    frmAddRecord.title("Add Users")
    frmAddRecord.geometry('400x250+50+50')
    frmAddRecord.resizable(False,False)
    frmAddRecord.configure(background='white')

    RecordIDText = tk.StringVar()
    DateText= tk.StringVar()
    MemberIDText= tk.StringVar()
    ActivityIDText= tk.StringVar()
   


    #Initiolize the defult values

    ActivityIDText.set("Gym") # default value


    





    def AddRecord():
        
        #j

        #Validatin, add the split
        ValidationPassed= True

        

        if ValidationPassed:
            p=1
        
        






            



    #############THE UI WIGETS####
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
        text='Activity Type',
        background='white'
        )

    ###Textboxes
    txtRecordID = tk.Entry(frame,textvariable=RecordIDText)
    txtDate=tk.Entry(frame, textvariable=DateText)
    txtMemberID=tk.Entry(frame, textvariable=MemberIDText)
    txtActivityID=tk.Entry(frame, textvariable=ActivityIDText)

    ###Add button####
    btnAddNewRecord = ttk.Button(
        frame,
        text='Add',
        command= AddRecord
    )
    cmbActivityID = tk.OptionMenu(frame, ActivityIDText, "Gym", "Swimming pool", "tenis")


    #Caclutate the date and display it as default

    #Calutlate the next RecordID

    #Calculate the next 

    #Grid and placements
    lblRecordID.grid(column=0,row=1,padx=7,sticky='W')
    txtRecordID.grid(column=2,row=1)
    lblDate.grid(column=0,row=2,pady=4,padx=7,sticky='W')
    txtDate.grid(column=2,row=2,pady=4)
    lblMemberID.grid(column=0,row=3,pady=4,padx=7,sticky='W')
    txtMemberID.grid(column=2,row=3,pady=4)
    lblActivity.grid(column=0,row=4,pady=4,padx=7,sticky='W')
   # txtActivityID.grid(column=2,row=4,pady=4)
    cmbActivityID.grid(column=2,row=4,pady=4) 
    btnAddNewRecord.grid(column=2,row=6,pady=25,columnspan=1)




    frmAddRecord.mainloop()












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

        validationPassed=True
        #length check: 4<x<25; 
        if len(txtAddPassword.get() )>25 or len(txtAddPassword.get() )<=3 or  len(txtAddUsername.get())<=3 or  len( txtAddUsername.get())<=3:
            validationPassed=False  
            messagebox.showerror("Error", "Your username and password have to meet the valid length")

        #Type check: see if it contains any spaces ---> " "
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
            frmAddAccount.destroy()
            

    




                
            with open('programData/HashedPasswords.txt', 'a') as file:
                HashedPassword=HashedPassword + '\n'
                file.write(HashedPassword)
                
                print("Password added ")
            

                messagebox.showinfo("Success", "New username and password has been added")












            



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

        #Type check: see if it contains any spaces ---> " "
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













ShowLoginForm()
#ShowNewMemberForm()
