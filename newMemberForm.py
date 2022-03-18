import tkinter as tk   
import main
from tkinter import ttk
from tkinter import messagebox
import re

#
#        u_id = input("Input User ID: ") #DECLARE u_id : string
#
#        rex = re.compile("^[A-Z][a-z]{2}[0-9]{3}$")
#        if rex.match(u_id):
#            print("Correct format")
#from idlelib.tooltip import Hovertip

#myTip = Hovertip(btnAddNewMember,'This is \na multiline tooltip.')



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







def ShowAddMemberForm():

    

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




ShowAddMemberForm()




w=[]
w.append("c")
w.append("b")
w.append("x")
w.append("a")
w.append("b")

print(IsUnique(w))


print(w)





























































#
#
#def ShowAddMemberForm():
#
#    
#
#    #Initiolize the AddNewAccount form
#    frmAddMember = tk.Tk()
#    frmAddMember.title("Add Users")
#    frmAddMember.geometry('400x350+50+50')
#    frmAddMember.resizable(False,False)
#    frmAddMember.configure(background='white')
#
#    MemberIDText = tk.StringVar()
#    NameText= tk.StringVar()
#    EmailText= tk.StringVar()
#    PhonnumberText= tk.StringVar()
#    SurnameText= tk.StringVar()
#    DOBText= tk.StringVar()
#    MembershipText= tk.StringVar()
#    ExtraInfoText= tk.StringVar()
#   
#   
#
#
#    #Initiolize the defult values
#
#    MembershipText.set("Gold") # default value
#
#     
#
#
#
#
#
#
#
#
#
#
#            
#
#
#
#    #############THE UI WIGETS####
#    #The Frame#
#    frame = tk.Frame(frmAddMember,bg='white')
#    frame.place(x=60,y=55)
#
#
#
#
#        #Lables######
#    lblMemberID= ttk.Label(
#        frame,
#        text='MemberID',
#        background='white'
#    )
#
#    lblName= ttk.Label(
#        frame,
#        text='Name',
#        padding=0,
#        background='white'
#    )
#
#    lblSurname= ttk.Label(
#        frame,
#        text='Surname',
#        background='white'
#        )
#    lblDOB= ttk.Label(
#        frame,
#        text='DOB (dd/mm/yy)',
#        background='white'
#        )
#
#
#    lblMembershipID= ttk.Label(
#        frame,
#        text='Membership Type',
#        background='white'
#        )
#
#
#    lblEmail= ttk.Label(
#        frame,
#        text='Email',
#        background='white'
#        )
#
#    lblPhonnumber= ttk.Label(
#        frame,
#        text='Phone Number',
#        background='white'
#        )
#
#    lblExtraInfo= ttk.Label(
#        frame,
#        text='Extra Info',
#        background='white'
#        )
#
#
#        ###Textboxes
#    txtMemberID = tk.Entry(frame,textvariable= MemberIDText)
#    txtName=tk.Entry(frame, textvariable= NameText)
#    txtSurname=tk.Entry(frame, textvariable= SurnameText)
#    txtDOB=tk.Entry(frame, textvariable=DOBText)
#    txtEmail=tk.Entry(frame, textvariable= EmailText)
#    txtPhonenumber=tk.Entry(frame, textvariable=PhonnumberText)
#    txtMembershipID=tk.Entry(frame, textvariable= MembershipText)
#    txtExtraInfo=tk.Entry(frame, textvariable= ExtraInfoText)
#
#
#
#    #ComboBOX (drop down menu)
#    cmbMembership = tk.OptionMenu(frame, MembershipText, "Gold", "Silver", "Bronz")
#
#
#
#
#
#    #Calculate the next primary key
#    def NextPK():
#        file = open("programData/Members.txt")
#        lines = file.read().splitlines()  #Load lines into an array
#        primaryKeys= []
#        for i in lines:
#            tmp=i.split(',') #Split each line into its elemnts seperated by commas. 
#            print(tmp)
#            primaryKeys.append(tmp[0])
#
#            
#        print("Primary keys are: "+str(primaryKeys))
#        file.close()
#        MemberIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
#
#
#
#
#    NextPK()#Call the next primary key function
#            
#    
#
#
#    
#
#
#
#
#
#
#
#    def AddMember():
#
#
#        MemberIDString = txtMemberID.get()
#        NameString=txtName.get()
#        SurnameString=txtSurname.get()
#        EmailString=txtEmail.get()
#        PhonenumberString=txtPhonenumber.get()
#        DOBString=txtDOB.get()
#        MembershipString=txtMembershipID.get()
#
#        #revert the colours in case they have been changed
#        ExtraInfoString=txtExtraInfo.get()        
#        txtMemberID.configure(bg="white")
#        txtPhonenumber.configure(bg='white')
#        txtName.configure(bg='white')
#        txtSurname.configure(bg='white')
#        txtEmail.configure(bg='white')
#        txtExtraInfo.configure(bg='white')
#        txtDOB.configure(bg='white')
#
#
######################Validation##############################################################33
#        ValidationPassed= True
#
#        #Length checks
#        if len(NameString)>25 or len(NameString)<3:
#            ValidationPassed=False
#            print("Name length check not passed")
#            txtName.configure(bg='pink')
#        
#        if len(SurnameString)>25 or len(SurnameString)<3:
#            ValidationPassed=False
#            print("surname length check not passed")
#            txtSurname.configure(bg='pink')
#
#
#
#        if len(EmailString)>40 or len(EmailString)<5:
#            ValidationPassed=False
#            print("email length check not passed")
#            print(len(PhonenumberString))
#            txtEmail.configure(bg='pink')
#        
#        
#        if not(len(PhonenumberString)==11):
#            ValidationPassed=False
#            print("Phone nubmer length check not passed")
#            txtPhonenumber.configure(bg='pink')
#            print(len(PhonenumberString))
#
#
#
#        
#        #Format checks
#
#
#
#
#        #MemberID in the form --> MB00001 
#        IDEx = re.compile('^[M][B][0-9]{5}$')
#        if not re.fullmatch(IDEx,MemberIDString): 
#            ValidationPassed=False 
#            print("ID check not passed")
#            txtMemberID.configure(bg='pink')
#       #email
#        emailEx = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#        if not re.fullmatch(emailEx,EmailString):
#            ValidationPassed=Falsee
#
#
