from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import re
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog



#Global variable for importCsv Function 
mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance pannel")

            #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()
         

        img=Image.open(r"D:\face_recognition_system\Image\bg5.jpg")
        img=img.resize((1530,789),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=789)

        title_lb1 = Label(f_lb1,text="Student Attendance Management System",font=("verdana",30),bg="black",fg="lightgrey")
        title_lb1.place(x=0,y=0,width=1530,height=45)



    


        class_Student_frame = LabelFrame(f_lb1,bd=2,bg="lightgrey",relief=RIDGE,text="Student Information",font=("verdana",12),fg="darkblue")
        class_Student_frame.place(x=10,y=100,width=600,height=500)

          #Student id
        studentId_label = Label(class_Student_frame,text="ID:",font=("verdana",11),fg="black",bg="lightgrey")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_id,width=31,font=("verdana",10))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

         #Student name
        student_name_label = Label(class_Student_frame,text="Name:",font=("verdana",11),fg="black",bg="lightgrey")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_name,width=31,font=("verdana",10))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        
         #label Course
        cou_label=Label(class_Student_frame,text="Course",font=("verdana",11),bg="lightgrey",fg="black")
        cou_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        cou_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_course,width=23,font=("verdana",11),state="readonly")
        cou_combo["values"]=("Select Course","BSCCSIT","BBM","BIM","BHM","BCA")
        cou_combo.current(0)
        cou_combo.grid(row=2,column=1,padx=5,pady=15,sticky=W)




        #time
        time_label = Label(class_Student_frame,text="Time:",font=("verdana",11),fg="black",bg="lightgrey")
        time_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(class_Student_frame,textvariable=self.var_time,width=25,font=("verdana",11))
        time_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(class_Student_frame,text="Date:",font=("verdana",11),fg="black",bg="lightgrey")
        date_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(class_Student_frame,textvariable=self.var_date,width=25,font=("verdana",11))
        date_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #attendance
        student_attend_label = Label(class_Student_frame,text="Attendance-status:",font=("verdana",11),fg="black",bg="lightgrey")
        student_attend_label.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_attend,width=23,font=("verdana",11),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=5,column=1,padx=5,pady=5,sticky=W)

         #Button Frame
        btn_frame = Frame(class_Student_frame,bd=2,bg="lightgrey",relief=RIDGE)
        btn_frame.place(x=20,y=300,width=450,height=65)

         #import button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("verdana",11),fg="Black",bg="white")
        save_btn.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #export button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("verdana",11),fg="Black",bg="white")
        update_btn.grid(row=0,column=2,padx=5,pady=8,sticky=W)

         #update button
        del_btn=Button(btn_frame,text="Update",width=8,font=("verdana",11),fg="Black",bg="white")
        del_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=8,font=("verdana",11),fg="black",bg="white")
        reset_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        
         #Attendance details
        Student_frame = LabelFrame(f_lb1,bd=2,bg="lightgrey",relief=RIDGE,text="Attendance",font=("verdana",12),fg="darkblue")
        Student_frame.place(x=700,y=75,width=750,height=650)


           #table
        table_frame = Frame(Student_frame,bd=2,bg="lightgrey",relief=RIDGE)
        table_frame.place(x=20,y=80,width=698,height=450)

        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
       
        self.attend_table = ttk.Treeview(table_frame,column=("ID","Name","Course","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attend_table.xview)
        scroll_y.config(command=self.attend_table.yview)

        self.attend_table.heading("ID",text="ID")
        self.attend_table.heading("Name",text="Name")
        self.attend_table.heading("Course",text="Course")
        self.attend_table.heading("Time",text="Time")
        self.attend_table.heading("Date",text="Date")
        self.attend_table.heading("Status",text="Status")
        self.attend_table["show"]="headings"


        self.attend_table.column("ID",width=100)
        self.attend_table.column("Name",width=100)
        self.attend_table.column("Course",width=100)
        self.attend_table.column("Time",width=100)
        self.attend_table.column("Date",width=100)
        self.attend_table.column("Status",width=100)
        
        self.attend_table.pack(fill=BOTH,expand=1)
        self.attend_table.bind("<ButtonRelease>",self.get_cursor_right)



         # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attend_table.delete(*self.attend_table.get_children())
        for i in rows:
            self.attend_table.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  



                    #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attend_table.focus()
        content = self.attend_table.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_course.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])  

          #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_course.set("Select Course")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status") 

        




      


     
       





       














if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()