from tkinter import *
from pip import ImageTk
from tkinter import messagebox

class Login:

    def __init__(self,root):
        self.root=root
        self.root.title("Imagcon ")
        self.root.geometry("1366x700")
        self.loginform()
        
    def loginform(self):
        Frame_login=Frame(self,root,bg="white")
        frame_input=Frame(self,root,bg="white")
        label1=Label(frame_input,text="LoginHere")
        label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"))
        self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

        
        
root=Tk()
ob=Login(root)
ob=loginform()
root.mainloop()


from tkinter import *



from tkinter import messagebox

import pymysql
import sqlite3

class Login:

   def __init__(self,root):

      self.root=root

      self.root.title("Imagecon Apps")

      self.root.geometry("1366x700+0+0")

      self.root.resizable(False,False)

      self.loginform()

   def loginform(self):

      Frame_login=Frame(self.root,bg="white")

      Frame_login.place(x=0,y=0,height=700,width=1366)

      



      

      frame_input=Frame(self.root,bg='white')

      frame_input.place(x=320,y=130,height=450,width=350)


      label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=75,y=20)


      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label2.place(x=30,y=95)

      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.email_txt.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.password=Entry(frame_input,font=("times new roman",15,"bold"),

                        bg='lightgray')

      self.password.place(x=30,y=245,width=270,height=35)

   

      btn1=Button(frame_input,text="forgot password?",cursor='hand2',

                  font=('calibri',10),bg='white',fg='black',bd=0)

      btn1.place(x=125,y=305)


      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",

                  font=("times new roman",15),fg="white",bg="orangered",

                  bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input,command=self.Register,text="Not Registered?register"

                  ,cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)


   def login(self):

      if self.email_txt.get()=="" or self.password.get()=="":

         messagebox.showerror("Error","All fields are required",parent=self.root)



   def save():
      a=uname.get()
      b=pwd.get()
      c=cpwd.get()
      mix=a+"-"+b+"-"+c
      if a!="" and b!="" and c!="" :
         
         with open("Login.txt","r") as fi:
            d=fi.readlines()
         if str(mix) in str(d):
            tsmg.showerror("Error","You Already Have An Account, Please Login")
            uname.set("")
            pwd.set("")
            cpwd.set("")
         elif str(a) in str(d):
            tsmg.showerror("Error","Username Already Exist")
            uname.set("")
            pwd.set("")
            cpwd.set("")
         else:
            if b==c:
               with open("Login.txt","a") as f:
                  f.write(f"{a}-{b}-{c}\n")
               tsmg.showinfo("Success","Your Account Has Been Created")
               uname.set("")
               pwd.set("")
               cpwd.set("")
            else:
               tsmg.showerror("Error","Both Password Are Different")   
               uname.set("")
               pwd.set("")
               cpwd.set("") 
   def appscreen(self):
      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=1366)
      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=130,height=450,width=630)
      Label(root, text="ENTER YOUR DETAILS BELOW").grid(row=0,column=6)
      Label(root, text="Enter your name*:",foreground="violet",background="white",height="2",width="30", font=('Times',10,'bold')).grid(row=1,sticky=SE)
      Label(root, text="Enter your age*:",foreground="violet",background="white",height="2",width="30", font=('Times',10,'bold')).grid(row=2,sticky=SE)
      Label(root, text="Date of birth*:",foreground="violet",background="white",height="2",width="30", font=('Times',10,'bold')).grid(row=3,sticky=SE)
      Label(root, text="Gender*:",foreground="violet",background="white",height="2",width="30", font=('Times',10,'bold')).grid(row=4,sticky=SE)
      Label(root, text="contact*:", foreground="violet",background="white",height="2",width="30",font=('Times',10,'bold')).grid(row=5,sticky=SE)
      Label(root, text="email*:",foreground="violet",background="white",height="2",width="30", font=('Times',10,'bold')).grid(row=6,sticky=SE)
      Label(root, text="Address*:", foreground="violet",background="white",height="2",width="30",font=('Times',10,'bold')).grid(row=7,sticky=SE)
      Label(root, text="user ID:",foreground="violet",background="white", height="2",width="30",font=('Times',10,'bold')).grid(row=8,sticky=SE)
      Label(root, text="Password:",foreground="violet",background="white",height="2",width="30", font=('Times',10,'bold')).grid(row=9,sticky=SE)


      e1 = Entry(root,foreground="blue",background="white")
      e2 = Entry(root,foreground="blue",background="white")
      e3 = Entry(root,foreground="blue",background="white")
      var=IntVar()
      e4 = Radiobutton(root,text="Male",variable=var,value=1,foreground="blue",background="white")
      e5 = Radiobutton(root,text="Female",variable=var,value=2,foreground="blue",background="white")
      e6 = Entry(root,foreground="blue",background="white")
      e7 = Entry(root,foreground="blue",background="white")
      e8 = Entry(root,foreground="blue",background="white")
      e9 = Entry(root,foreground="blue",background="white")
      e10 = Entry(root,show="*",foreground="blue",background="white")

      e1.grid(row=1, column=6)
      e2.grid(row=2, column=6)
      e3.grid(row=3, column=6)
      e4.grid(row=4, column=6)
      e5.grid(row=4, column=7)
      e6.grid(row=5, column=6)
      e7.grid(row=6, column=6)
      e8.grid(row=7, column=6)
      e9.grid(row=8, column=6)
      e10.grid(row=9, column=6)

      button=Button(root, text= "save details",foreground="Green", command=lambda:print("Your Details Saved Successfully"))
      button.grid(row=10,column=6)


            

   def Register(self):


      Frame_login1=Frame(self.root,bg="white")

      Frame_login1.place(x=0,y=0,height=700,width=1366)

      



      

      frame_input2=Frame(self.root,bg='white')

      frame_input2.place(x=320,y=130,height=450,width=630)


      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=45,y=20)


      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),

                        bg='lightgray')

      self.entry2.place(x=30,y=245,width=270,height=35)


      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry3.place(x=330,y=145,width=270,height=35)


      label5=Label(frame_input2,text="Confirm Password",

                   font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry4.place(x=330,y=245,width=270,height=35)


      btn2=Button(frame_input2,command=self.register,text="Register"

                  ,cursor="hand2",font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input2,command=self.loginform,

                  text="Already Registered?Login",cursor="hand2",

                  font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)



   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.entry2.get()!=self.entry4.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same"

                              ,parent=self.root)

      else:

         try:
            coe=sqlite3.connect('datareg.sqlite')
##            coe.excute("""
##               CREATE TABLE IF NOT EXISTS login datas(
##                     Username TEXT NOT NULL,
##                     Password TEXT NOT NULL,
####                     Email_id TEXT NOT NULL,)
##                     """)
            
            curr=coe.cursor()
            

           

            curr.execute("select * from register where emailid=%s"

                        ,self.entry3.get())

            row=curr.fetchone()

            if row!=None:

               messagebox.showerror("Error"

               ,"User already Exist,Please try with another Email"

                                    ,parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)"

                           ,(self.entry.get(),self.entry3.get(),

                           self.entry2.get(),

                           self.entry4.get()))

               con.commit()

               con.close()

               messagebox.showinfo("Success","Register Succesfull"

                                   ,parent=self.root)

               self.regclear()

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}"

                                 ,parent=self.root)


   def appscreen(self):


      Frame_login=Frame(self.root,bg="white")

      Frame_login.place(x=0,y=0,height=700,width=1366)

      label1=Label(Frame_login,text="Hi! Welcome To Seek coding"

                   ,font=('times new roman',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=375,y=100)

      label2=Label(Frame_login,text="Youtube Channel.If you are New to Channel"

                   ,font=('times new roman',32,'bold'),

                   fg="black",bg='white')

      label2.place(x=235,y=160)

      label3=Label(Frame_login,text="Please Subscribe,Like And Share"

                   ,font=('times new roman',32,'bold'),

                   fg="black",bg='white')

      label3.place(x=340,y=220)

      btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",

                  font=("times new roman",15),fg="white",bg="orangered",

                  bd=0,width=15,height=1)

      btn2.place(x=1000,y=10)


   def regclear(self):

      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)


   def loginclear(self):

      self.email_txt.delete(0,END)

      self.password.delete(0,END)


root=Tk()

ob=Login(root)

root.mainloop()
from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="orangered", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="orangered", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
























