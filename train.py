from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Pannel")

        
        
        img=Image.open(r"D:\face_recognition_system\Image\bg5.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=790)

        
         #title section
        title_lb1 = Label(f_lb1,text="Data Train",font=("verdana",30),bg="black",fg="lightgrey")
        title_lb1.place(x=0,y=0,width=1530,height=60)

        train_frame = LabelFrame(f_lb1,bd=2,bg="lightgrey",relief=RIDGE,font=("verdana",12,),fg="darkblue")
        train_frame.place(x=500,y=150,width=600,height=600)

        img=Image.open(r"D:\face_recognition_system\Image\bg.png")
        img=img.resize((600,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=503,y=152,width=598,height=150)

         # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
     

        std_b1_1 = Button(train_frame,text="Train Data", command=self.train_classifier,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        std_b1_1.place(x=200,y=300,width=180,height=45)


        
    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # convert into gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

          

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("code.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)

        

if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()