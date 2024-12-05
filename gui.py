from tkinter import *
root = Tk()
def studentInfoPage():
    loginFrame.pack_forget()
    displayFrame.pack_forget()
    addStudentFrame.pack_forget()
    searchFrame.pack_forget()
    studentInfoFrame.pack(fill='both',expand=True)
def displayPage():
    loginFrame.pack_forget()
    studentInfoFrame.pack_forget()
    searchFrame.pack_forget()
    addStudentFrame.pack_forget()
    displayFrame.pack(fill='both',expand=True)
def addPage():
    loginFrame.pack_forget()
    studentInfoFrame.pack_forget()
    searchFrame.pack_forget()
    displayFrame.pack_forget()
    addStudentFrame.pack(fill='both',expand=True)     
def searchPage():
    loginFrame.pack_forget()
    studentInfoFrame.pack_forget()
    addStudentFrame.pack_forget()
    displayFrame.pack_forget()
    searchFrame.pack(fill='both',expand=True)
def logout():
    studentInfoFrame.pack_forget()
    addStudentFrame.pack_forget()
    displayFrame.pack_forget()
    searchFrame.pack_forget()
    loginFrame.pack(fill='both',expand=True)
    
         
menuFrame = Label(root,bg ='black',width=150,height=4)
menuFrame.pack()
loginFrame = Frame(root,bg='#f9f9f9')
studentInfoFrame = Frame(root,bg='black')
displayFrame = Frame(root,bg='blue')
addStudentFrame = Frame(root,bg='red')
searchFrame = Frame(root,bg='yellow')

StudInfoBtn = Button(menuFrame,bg='#f9f9f9',width=15,height = 2,text="Student Information",command=studentInfoPage)
displayBtn = Button(menuFrame,bg='#f9f9f9',width=15,height=2,text='Display All Students',command = displayPage)
addBtn = Button(menuFrame,bg='#f9f9f9',width=15,height=2,text = 'Add a Student',command = addPage)
searchBtn = Button(menuFrame,bg='#f9f9f9',width=15,height=2,text = 'Search Student',command = searchPage)
logoutBtn = Button(menuFrame,bg='#f9f9f9',width=15,height=2,text = 'Log Out',command=logout)
userlabel = Label(menuFrame,bg = 'black',fg = 'white',text = 'Current User: wala pa')
userstatus = Label(menuFrame,bg = 'black',fg = 'white',text = 'Login Status: Admin')

StudInfoBtn.place(x=10,y=8)
displayBtn.place(x=130,y=8)
addBtn.place(x=250,y=8)
searchBtn.place(x=370,y=8)
logoutBtn.place(x=490,y=8)
userlabel.place(x=610,y=8)
userstatus.place(x=610,y=28)       

root.title('Student Information Management System'),root.geometry('750x400+650+350'),root.mainloop()
