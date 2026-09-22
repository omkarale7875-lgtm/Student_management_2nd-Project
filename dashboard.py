from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from course import courseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox 
import os      
import sys
from datetime import datetime
import time 
from math import sin, cos, radians
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x655+0+0")
        self.root.config(bg="white")

        #  Icons & Title 
        try:
            self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
            title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)
        except Exception:
            title = Label(self.root, text="Student Result Management System", padx=10, font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        #  Menus Frame 
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1330, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=10, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=225, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=440, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=655, y=5, width=210, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=880, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_).place(x=1095, y=5, width=200, height=40)

        #  Content Window Image 
        try:
            self.bg_img = Image.open("images/bg.png")
            self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
            self.lbl_bg = Label(self.root, image=self.bg_img).place(x=340, y=180, width=920, height=350)
        except Exception:
            self.lbl_bg = Label(self.root, bg="#f0f0f0").place(x=340, y=180, width=920, height=350)

        #    Live Statistics Cards 
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=340, y=530, width=300, height=90)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=650, y=530, width=300, height=90)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=960, y=530, width=300, height=90)

        #    Live Clock 
        self.lbl = Label(self.root, text="Clock", font=("Book Antiqua", 25, "bold"), fg="white", compound=BOTTOM, bg="#081923", bd=0)
        self.lbl.place(x=10, y=170, height=450, width=310)

        self.working()

        #    Footer 
        footer = Label(self.root, text="SRMS - Student Result Management System | Developed by Web Code", font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()

    #    Methods 
    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[ {len(cr)} ]")

            cur.execute("select * from student")
            sr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[ {len(sr)} ]")

            cur.execute("select * from result")
            rr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[ {len(rr)} ]")

            # Update every 2 seconds
            self.lbl_course.after(2000, self.update_details)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def working(self):
        now = datetime.now().time()
        h, m, s = now.hour, now.minute, now.second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360

        self.clock_image(hr, min_, sec_)
        try:
            self.img = ImageTk.PhotoImage(file="images/clock_new.png")
            self.lbl.config(image=self.img)
        except Exception:
            self.lbl.config(text=f"{h:02d}:{m:02d}:{s:02d}")
        self.lbl.after(1000, self.working)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        try:
            bg = Image.open("images/c.png")
            bg = bg.resize((300, 300), Image.LANCZOS)
            clock.paste(bg, (50, 50))
        except Exception:
            draw.ellipse((50, 50, 350, 350), outline="white", width=4)

        origin = 200, 200
        # Hour line
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="#DF005E", width=4)
        # Min line
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)
        # Sec line
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)
        # Center pivot
        draw.ellipse((195, 195, 205, 205), fill="#1AD5D5")

        os.makedirs("images", exist_ok=True)
        clock.save("images/clock_new.png")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = courseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()
            os.system(f'"{sys.executable}" login.py')

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
