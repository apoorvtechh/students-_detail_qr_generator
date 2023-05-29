from tkinter import*
import qrcode
from resizeimage import resizeimage
from PIL import Image,ImageTk
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("OR Generator | Developed By Apoorv")
        self.root.resizable(False,False)

        title=Label(self.root,text="   Qr Code Generator", font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        #====Students detail window=====#
        #======VAriable=====#
        self.var_emp_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_course=StringVar()
        self.var_emp_year=StringVar()
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)

        emp_title=Label(emp_Frame,text="Students Details", font=("goudy old style",20),bg='#043246',fg='white',).place(x=0,y=0,relwidth=1)
        emp_id=Label(emp_Frame,text="Students ID", font=("times new roman",15),bg='white',).place(x=20,y=60)
        emp_name=Label(emp_Frame,text="Students Name", font=("times new roman",15),bg='white',).place(x=20,y=100)
        emp_course=Label(emp_Frame,text="Students Course", font=("times new roman",15),bg='white',).place(x=20,y=140)
        emp_year=Label(emp_Frame,text="Students Year", font=("times new roman",15),bg='white',).place(x=20,y=180)


        txt_id=Entry(emp_Frame, font=("times new roman",15),textvariable=self.var_emp_id,bg='Lightyellow',).place(x=200,y=60)
        txt_name=Entry(emp_Frame, font=("times new roman",15),textvariable=self.var_emp_name,bg='lightyellow',).place(x=200,y=100)
        txt_course=Entry(emp_Frame, font=("times new roman",15),textvariable=self.var_emp_course,bg='lightyellow',).place(x=200,y=140)
        txt_year=Entry(emp_Frame, font=("times new roman",15),textvariable=self.var_emp_year,bg='lightyellow',).place(x=200,y=180)



        btn_generate=Button(emp_Frame,text='GENERATE QR',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear=Button(emp_Frame,text='CLEAR',command=self.clear,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=280,y=250,width=110,height=30)
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg, font=("times new roman",20,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)
        #======students qr code window======#
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        emp_title=Label(qr_Frame,text="Student Qr Code", font=("goudy old style",20),bg='#043246',fg='white',).place(x=0,y=0,relwidth=1)
        self.qr_code=Label(qr_Frame,text="Qr Code \nNot Available",font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)


    def clear(self):
        self.var_emp_id.set('')
        self.var_emp_name.set('')
        self.var_emp_course.set('')
        self.var_emp_year.set('')
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_emp_course.get()==''or self.var_emp_id.get()==''or self.var_emp_name.get()==''or self.var_emp_year.get()=='':
            self.msg="ALL Fields are Required!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            #======updating notifiactio======+#
            qr_data=(f"Student ID:{self.var_emp_id.get()}\nStudent Name:{self.var_emp_name.get()}\nStudent Course:{self.var_emp_course.get()}\nStudent Year:{self.var_emp_year.get()}\n")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("student_detail/stu_"+str(self.var_emp_id.get())+'.png')
            #======qr code image update=====#
            self.im=ImageTk.PhotoImage(file="student_detail/stu_"+str(self.var_emp_course.get())+'.png')
            self.qr_code.config(image=self.im)
            self.msg='QR Generated Succesfully!!'
            self.lbl_msg.config(text=self.msg,fg='green')
root=Tk()
obj=Qr_Generator(root)  
root.mainloop()   