from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from detector import Face_Recognition
from attendance import Attendance
from train import Train
import os
import tkinter



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
    obj=Vision(root)
    root.mainloop()