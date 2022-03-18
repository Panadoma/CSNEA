import tkinter as tk   
import main
from tkinter import ttk
from tkinter import messagebox
import re
#from idlelib.tooltip import Hovertip

#myTip = Hovertip(btnAddNewRecord,'This is \na multiline tooltip.')

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


    def NextPK():
        file = open("programData/Records.txt")
        lines = file.read().splitlines()  #Load lines into an array
        primaryKeys= []
        for i in lines:
            tmp=i.split(',') #Split each line into its elemnts seperated by commas. 
            print(tmp)
            primaryKeys.append(tmp[0])

            
        print("Primary keys are: "+str(primaryKeys))
        file.close()
        RecordIDText.set(CalculateNextPrimaryKey(primaryKeys))#Calculate the Next Primary key using its function
        print(CalculateNextPrimaryKey(primaryKeys))

    NextPK()


    def AddRecord():
        

        ValidationPassed= True

        

        if ValidationPassed:
            p=1
        

    ###Add button####
    btnAddNewRecord = ttk.Button(
        frame,
        text='Add',
        command= AddRecord
    )
    ###Home button####
    btnHome= ttk.Button(
        frame,
        text='Home',
        command= AddRecord
    )
    cmbActivityID = tk.OptionMenu(frame, ActivityIDText, "Gym", "Swimming pool", "tenis")

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
    btnHome.grid(column=1,row=6,pady=25,columnspan=1)




    frmAddRecord.mainloop()

ShowAddRecordForm()
