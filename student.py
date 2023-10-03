from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Pannel")

         #-----------Variables-------------------
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_tu_no=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mobile_no=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        
        img=Image.open(r"D:\face_recognition_system\Image\bg5.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=790)

        
         #title section

        title_lb1 = Label(f_lb1,text="Student Details",font=("verdana",30),bg="black",fg="lightgrey")
        title_lb1.place(x=0,y=0,width=1530,height=45)



         

              # Current Course 
        current_course_frame = LabelFrame(f_lb1,bd=2,bg="lightgrey",relief=RIDGE,text="Course",font=("verdana",12,),fg="darkblue")
        current_course_frame.place(x=10,y=69,width=600,height=150)

        #label Department
        dep_label=Label(current_course_frame,text="Department",font=("verdana",10),bg = "lightgrey",fg="black")
        dep_label.grid(row=0,column=0,padx=5,pady=15)

         #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department,width=16,font=("verdana",8),state="readonly")
        dep_combo["values"]=("Select Department","Science","Management","Humanities")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

         #label Course
        cou_label=Label(current_course_frame,text="Course",font=("verdana",10),bg="lightgrey",fg="black")
        cou_label.grid(row=0,column=2,padx=5,pady=15)

        #combo box 
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=16,font=("verdana",8),state="readonly")
        cou_combo["values"]=("Select Course","BSCCSIT","BBM","BIM","BHM","BCA")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)

        #label Semester 
        year_label=Label(current_course_frame,text="Semester",font=("verdana",10),bg="lightgrey",fg="black")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=16,font=("verdana",8),state="readonly")
        year_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)


         #Class Student Information
        class_Student_frame = LabelFrame(f_lb1,bd=2,bg="lightgrey",relief=RIDGE,text="Student Information",font=("verdana",12),fg="darkblue")
        class_Student_frame.place(x=10,y=250,width=600,height=520)

          #Student id
        studentId_label = Label(class_Student_frame,text="ID:",font=("verdana",11),fg="black",bg="lightgrey")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_id,width=31,font=("verdana",10))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
         # TU No
        student_roll_label = Label(class_Student_frame,text="TU_No:",font=("verdana",11),fg="black",bg="lightgrey")
        student_roll_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_tu_no,width=25,font=("verdana",12))
        student_roll_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

          #Student name
        student_name_label = Label(class_Student_frame,text="Name:",font=("verdana",11),fg="black",bg="lightgrey")
        student_name_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_name,width=31,font=("verdana",10))
        student_name_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

         #Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",11),fg="black",bg="lightgrey")
        student_gender_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",10),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Date of Birth
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",11),fg="black",bg="lightgrey")
        student_dob_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=30,font=("verdana",10))
        student_dob_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

         #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",11),fg="black",bg="lightgrey")
        student_address_label.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=30,font=("verdana",10))
        student_address_entry.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",11),fg="black",bg="lightgrey")
        student_email_label.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=30,font=("verdana",10))
        student_email_entry.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        #Phone Number
        student_mob_label = Label(class_Student_frame,text="Mobile_No:",font=("verdana",11),fg="black",bg="lightgrey")
        student_mob_label.grid(row=7,column=0,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mobile_no,width=30,font=("verdana",10))
        student_mob_entry.grid(row=7,column=1,padx=5,pady=5,sticky=W)


        #Teacher Name
        student_tutor_label = Label(class_Student_frame,text="Teacher Name:",font=("verdana",11),fg="black",bg="lightgrey")
        student_tutor_label.grid(row=8,column=0,padx=5,pady=5,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=30,font=("verdana",10))
        student_tutor_entry.grid(row=8,column=1,padx=5,pady=5,sticky=W)

         #Radio Buttons

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take Photo",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=11,column=0,padx=5,pady=5,sticky=W)

        
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=11,column=1,padx=5,pady=5,sticky=W)

      
         #Button Frame
        btn_frame = Frame(class_Student_frame,bd=2,bg="lightgrey",relief=RIDGE)
        btn_frame.place(x=9,y=350,width=480,height=65)

         #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=7,font=("verdana",11),fg="Black",bg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=7,font=("verdana",11),fg="Black",bg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

         #delete button
        del_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=7,font=("verdana",11),fg="Black",bg="white")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=7,font=("verdana",11),fg="black",bg="white")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo",width=9,font=("verdana",11),fg="black",bg="white")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

      


          #Student details
        Student_frame = LabelFrame(f_lb1,bd=2,bg="lightgrey",relief=RIDGE,text="Student Information",font=("verdana",12),fg="darkblue")
        Student_frame.place(x=700,y=75,width=750,height=650)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(Student_frame,bd=2,bg="lightgrey",relief=RIDGE,text="Search System",font=("verdana",11),fg="black")
        search_frame.place(x=50,y=40,width=640,height=80)

        search_label = Label(search_frame,text="Search:",font=("verdana",11),fg="black",bg="lightgrey")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",11),state="readonly")
        search_combo["values"]=("Select","ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)
        
        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",11))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",11),fg="black",bg="white")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=9,font=("verdana",11),fg="black",bg="white")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)



        table_frame = Frame(Student_frame,bd=2,bg="lightgrey",relief=RIDGE)
        table_frame.place(x=20,y=150,width=698,height=360)

        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
       
        self.student_table = ttk.Treeview(table_frame,column=("Department","Course","Semester","ID","TU_No","Name","Gender","DOB","Address","Email","Mobile_No","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("TU_No",text="TU_No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Mobile_No",text="Mobile-No")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

               # Set Width of Colums 

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("TU_No",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Mobile_No",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
         # ==================Function Decleration==============================
    def add_data(self):
     if self.var_department.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_tu_no.get()==""or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mobile_no.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
        messagebox.showerror("Error","Please fill all the details!",parent=self.root)
     else:
              try:
                conn = mysql.connector.connect(host="localhost",username="root",password="sudina123",database="vision")
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                       self.var_department.get(),
                                                                                                       self.var_course.get(), 
                                                                                                       self.var_semester.get(),
                                                                                                       self.var_id.get(),
                                                                                                       self.var_tu_no.get(),
                                                                                                       self.var_name.get(),
                                                                                                       self.var_gender.get(),
                                                                                                       self.var_dob.get(),
                                                                                                       self.var_mobile_no.get(),
                                                                                                       self.var_address.get(),
                                                                                                       self.var_email.get(),
                                                                                                       self.var_teacher.get(),
                                                                                                       self.var_radio1.get()
                                                                                                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
              except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

   # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username="root", password="sudina123",host="localhost",database="vision")
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        
    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_id.set(data[3]),
        self.var_tu_no.set(data[4]),
        self.var_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_address.set(data[8]),
        self.var_email.set(data[9]),
        self.var_mobile_no.set(data[10]),
        self.var_teacher.set(data[11]),
        self.var_radio1.set(data[12])

         # ========================================Update Function==========================
    def update_data(self):
       if self.var_department.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_tu_no.get()==""or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mobile_no.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
          messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
       else:
            try:
                 Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                 if Update > 0:
                    conn = mysql.connector.connect(username="root", password="sudina123",host="localhost",database="vision")
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Department=%s,Course=%s,Semester=%s,TU_No=%s,Name=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Email=%s,Teacher=%s,Photo=%s where ID=%s",( 
                                                                        self.var_department.get(),
                                                                        self.var_course.get(), 
                                                                        self.var_semester.get(),
                                                                        self.var_tu_no.get(),
                                                                        self.var_name.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_mobile_no.get(),
                                                                        self.var_address.get(),
                                                                        self.var_email.get(),
                                                                        self.var_teacher.get(),
                                                                        self.var_radio1.get(),
                                                                        self.var_id.get()                     
                                                                    ))
                 else:
                     if not Update:
                        return
                 messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
      
         #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username="root", password="sudina123",host="localhost",database="vision")
                    mycursor = conn.cursor() 
                    sql="delete from student where ID=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_department.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_tu_no.set(""),
        self.var_name.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_mobile_no.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

         # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username="root", password="sudina123",host="localhost",database="vision")
                my_cursor = conn.cursor()
                sql = "SELECT Department,Course,Semester,TU_No,Name,Gender,DOB,Email,Mobile_No,Address,Teacher,Photo FROM student where ID='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)

                rows=my_cursor.fetchall() 
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

                #=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_tu_no.get()==""or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mobile_no.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
          messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username="root", password="sudina123",host="localhost",database="vision")
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1
                mycursor.execute("update student set Department=%s,Course=%s,Semester=%s,TU_No=%s,Name=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Email=%s,Teacher=%s,Photo=%s where ID=%s",( 
                                                                        self.var_department.get(),
                                                                        self.var_course.get(), 
                                                                        self.var_semester.get(),
                                                                        self.var_tu_no.get(),
                                                                        self.var_name.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_mobile_no.get(),
                                                                        self.var_address.get(),
                                                                        self.var_email.get(),
                                                                        self.var_teacher.get(),
                                                                        self.var_radio1.get(),
                                                                        self.var_id.get()==id+1                     
                                                                    ))
                    
      
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                 # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum neighbhor 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 




        


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
