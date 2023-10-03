from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from main import Vision
from student import Student
from detector import Face_Recognition
from attendance import Attendance
from train import Train
import tkinter
import os

def main():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")
        
        img=Image.open(r"D:\face_recognition_system\Image\bg3.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=790)


        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=190,width=350,height=450)


        img1=Image.open(r"D:\face_recognition_system\Image\log1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=690,y=190, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

          #label1 
        username =lb1= Label(frame1,text="Email:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)

         #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


      
        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)

          # Creating Button Registration
        loginbtn=Button(frame1,text="Register",command=self.register_window,font=("times new roman",12,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=60,height=20)


        

#this function for open register wimdow 

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif self.txtuser.get()=="admin" and self.txtpwd.get()=="admin":
            messagebox.showinfo("Sussessfully","Welcome to Vision")

        else:
            conn = mysql.connector.connect(username='root', password='sudina123',host='localhost',database='vision')
            mycursor = conn.cursor()
            mycursor.execute("select*from registes where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpwd.get() 
                                                                                      ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Are you sure?")
                if open_main>0:
                      self.new_window=Toplevel(self.root)
                      self.app=Vision(self.new_window)
                else:
                    if not open_main:
                      return

        conn.comit()
        conn.close()





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_pwd=StringVar()
        self.var_check=IntVar()



        self.bg=ImageTk.PhotoImage(file=r"D:\face_recognition_system\Image\bg1.jpg")
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,width=1530,height=790)
        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=350,y=100,width=850,height=580)

        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=340,y=100)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)

        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=225,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        gender =lb1= Label(frame,text="Gender:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        gender.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Male","female","Other")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


    
       
        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=350)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=375,width=270)


       
        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=280,y=480,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=280,y=510,width=270,height=35)

        


    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="Select" or self.var_pwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
       # elif(self.var_pwd.get() != self.var_cpwd.get()):
          #  messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(username='root', password='sudina123',host='localhost',database='vision')
                mycursor = conn.cursor()
                query=("select * from registes where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into registes values(%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_cnum.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

class Vision:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Vision")

     
        img=Image.open(r"D:\face_recognition_system\Image\bg3.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=790)

            #title section
        title_lb1 = Label(f_lb1,text="Vision",font=("verdana",30,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=60)

         # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"D:\face_recognition_system\Image\std1.png")
        std_img_btn=std_img_btn.resize((200,200),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(f_lb1,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=300,y=150,width=200,height=200)

        std_b1_1 = Button(f_lb1,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("tahoma",15),bg="white",fg="darkblue")
        std_b1_1.place(x=300,y=352,width=200,height=45)

         # Detect Face  button 2
        det_img_btn=Image.open(r"D:\face_recognition_system\Image\det1.jpg")
        det_img_btn=det_img_btn.resize((200,200),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(f_lb1,command=self.recog,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=600,y=150,width=200,height=200)

        det_b1_1 = Button(f_lb1,command=self.recog,text="Face Detector",cursor="hand2",font=("tahoma",15),bg="white",fg="darkblue")
        det_b1_1.place(x=600,y=353,width=200,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\face_recognition_system\Image\att.png")
        att_img_btn=att_img_btn.resize((200,200),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(f_lb1,command=self.attend,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=913,y=150,width=200,height=200)

        att_b1_1 = Button(f_lb1,text="Attendance",command=self.attend,cursor="hand2",font=("tahoma",15),bg="white",fg="darkblue")
        att_b1_1.place(x=913,y=353,width=200,height=45)

         # Train   button 5
        tra_img_btn=Image.open(r"D:\face_recognition_system\Image\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((200,200),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(f_lb1,command=self.train,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=300,y=450,width=200,height=200)

        tra_b1_1 = Button(f_lb1,command=self.train,text="Data Train",cursor="hand2",font=("tahoma",15),bg="white",fg="darkblue")
        tra_b1_1.place(x=300,y=652,width=200,height=45)

         # photo  button 5
        gall_img_btn=Image.open(r"D:\face_recognition_system\Image\gall1.jpg")
        gall_img_btn=gall_img_btn.resize((200,200),Image.ANTIALIAS)
        self.gall_img1=ImageTk.PhotoImage(gall_img_btn)

        gall_b1 = Button(f_lb1,command=self.open_img,image=self.gall_img1,cursor="hand2")
        gall_b1.place(x=600,y=450,width=200,height=200)

        gall_b1_1 = Button(f_lb1,command=self.open_img,text="Photo",cursor="hand2",font=("tahoma",15),bg="white",fg="darkblue")
        gall_b1_1.place(x=600,y=652,width=200,height=45)
        

         # exit   button 8
        exi_img_btn=Image.open(r"D:\face_recognition_system\Image\exi.png")
        exi_img_btn=exi_img_btn.resize((200,200),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(f_lb1,image=self.exi_img1,cursor="hand2",command=self.iExit)
        exi_b1.place(x=913,y=450,width=200,height=200)

        exi_b1_1 = Button(f_lb1,text="Exit",command=self.iExit,cursor="hand2",font=("tahoma",15),bg="white",fg="darkblue")
        exi_b1_1.place(x=913,y=652,width=200,height=45)



    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Vision","Are you sure to exit ?",parent=self.root)
        if self.iExit >0:
           self.root.destroy()
        else:
            return   




        

        # ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)




        







if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()
    
