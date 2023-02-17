import sqlite3
from tkinter import *

Student_portal = Tk()
Student_portal.title("SCHOOL RESULT PORTAL")
Student_portal.geometry("640x480-8-100")

portal_title = Label(Student_portal, text="STUDENT PORTAL SITE")
portal_title.grid(row=0, column=0, padx=50, pady=30, sticky='nw')
ad_user = "ADMIN"
ad_pass = "admin@2023"


def admin_login():
    Student_portal.destroy()
    admin_portal = Tk()
    admin_portal.title("WELCOME TO ADMIN PORTAL")
    admin_portal.geometry("640x480-8-100")
    a_l = Label(admin_portal, text="PLEASE ENTER THE ADMIN INFO. BELOW")
    a_l.grid(row=0, column=0, padx=50, pady=20)
    a_i = Entry(admin_portal)
    a_i.grid(row=1, column=1, pady=20)
    a_i_l = Label(admin_portal, text="USERNAME")
    a_i_l.grid(row=1, column=0)
    a_p = Entry(admin_portal)
    a_p.grid(row=2, column=1, pady=30)
    a_p_l = Label(admin_portal, text="PASSWORD")
    a_p_l.grid(row=2, column=0)

    def login():
        if a_i.get().upper() == "ADMIN" and a_p.get() == "admin@2023":
            admin_portal.destroy()
            upload_face = Tk()
            upload_face.title("UPLOAD PAGE")
            upload_face.geometry("640x480-8-100")
            r_u = Label(upload_face, text="STUDENT INFO TO UPLOAD")
            r_u.grid(row=0, column=1, padx=50, pady=10)
            s_m = Entry(upload_face)
            s_m.grid(row=1, column=1, pady=5, padx=20)
            s_m_l = Label(upload_face, text="STUDENT MATRIC NO.")
            s_m_l.grid(row=1, column=0)
            s_n = Entry(upload_face)
            s_n.grid(row=2, column=1, pady=5, padx=20)
            s_n_l = Label(upload_face, text="STUDENT NAME")
            s_n_l.grid(row=2, column=0)
            math_s = Entry(upload_face)
            math_s.grid(row=3, column=1, pady=5, padx=20)
            math_s_l = Label(upload_face, text="MATHS SCORE")
            math_s_l.grid(row=3, column=0)
            english_s = Entry(upload_face)
            english_s.grid(row=4, column=1, pady=5, padx=20)
            english_s_l = Label(upload_face, text="ENGLISH SCORE")
            english_s_l.grid(row=4, column=0)
            computer_s = Entry(upload_face)
            computer_s.grid(row=5, column=1, pady=5, padx=20)
            computer_s_l = Label(upload_face, text="COMPUTER SCORE")
            computer_s_l.grid(row=5, column=0)
            biology_s = Entry(upload_face)
            biology_s.grid(row=6, column=1, pady=5, padx=20)
            biology_s_l = Label(upload_face, text="BIOLOGY SCORE")
            biology_s_l.grid(row=6, column=0)
            chemistry_s = Entry(upload_face)
            chemistry_s.grid(row=7, column=1, pady=5, padx=20)
            chemistry_s_l = Label(upload_face, text="CHEMISTRY SCORE")
            chemistry_s_l.grid(row=7, column=0)
            physics_s = Entry(upload_face)
            physics_s.grid(row=8, column=1, pady=5, padx=20)
            physics_s_l = Label(upload_face, text="PHYSICS SCORE")
            physics_s_l.grid(row=8, column=0)
            civic_s = Entry(upload_face)
            civic_s.grid(row=9, column=1, pady=5, padx=20)
            civic_s_l = Label(upload_face, text="CIVIC SCORE")
            civic_s_l.grid(row=9, column=0)
            furthermaths_s = Entry(upload_face)
            furthermaths_s.grid(row=10, column=1, pady=5, padx=20)
            furthermaths_s_l = Label(upload_face, text="FURTHERMATHS SCORE")
            furthermaths_s_l.grid(row=10, column=0)

            def upload():
                conn = sqlite3.connect('student.db')
                c = conn.cursor()
                # inserting values to the table
                c.execute("INSERT INTO student_result VALUES (:student_matric, :student_name, :maths, :english,"
                          ":computer, :biology, :chemistry, :physics, :civic, :furthermaths)",
                          {
                              "student_matric": s_m.get(),
                              "student_name": s_n.get().upper(),
                              "maths": math_s.get(),
                              "english": english_s.get(),
                              "computer": computer_s.get(),
                              "biology": biology_s.get(),
                              "chemistry": chemistry_s.get(),
                              "physics": physics_s.get(),
                              "civic": civic_s.get(),
                              "furthermaths": furthermaths_s.get(),
                          })
                conn.commit()
                conn.close()
                txt_done = f"{s_n.get().upper()}\n Added to the Student Database"
                td_l = Label(upload_face, text=txt_done)
                s_m.delete(0, END)
                s_n.delete(0, END)
                math_s.delete(0, END)
                english_s.delete(0, END)
                computer_s.delete(0, END)
                biology_s.delete(0, END)
                chemistry_s.delete(0, END)
                physics_s.delete(0, END)
                civic_s.delete(0, END)
                furthermaths_s.delete(0, END)
                td_l.grid(row=7, column=2)
            upload_b = Button(upload_face, text="UPLOAD", command=upload)
            upload_b.grid(row=6, column=2)
            ex_b = Button(upload_face, text="EXIT", command=exit)
            ex_b.grid(row=10, column=2)
        else:
            a_i.delete(0, END)
            a_p.delete(0, END)
            ans = f"ACCESS DENIED !!!"
            ans_l = Label(admin_portal, text=ans)
            ans_l.grid(row=3, column=0, pady=30, padx=80, columnspan=40)
    a_b = Button(admin_portal, text="LOGIN", command=login)
    a_b.grid(row=3, column=1, padx=50)


admin_button = Button(Student_portal, text="UPLOAD RESULT(admin only)", command=admin_login)
admin_button.grid(row=1, column=0, columnspan=5)


def st_page():
    Student_portal.destroy()
    stud_portal = Tk()
    stud_portal.title("WELCOME TO STUDENT PORTAL")
    stud_portal.geometry("640x480-8-100")
    s_l = Label(stud_portal, text="PLEASE ENTER THE STUDENT INFO. BELOW")
    s_l.grid(row=0, column=0, padx=50, pady=20)
    s_i = Entry(stud_portal)
    s_i.grid(row=1, column=1, pady=20)
    s_i_l = Label(stud_portal, text="USERNAME")
    s_i_l.grid(row=1, column=0)
    s_p = Entry(stud_portal)
    s_p.grid(row=2, column=1, pady=30)
    s_p_l = Label(stud_portal, text="PASSWORD")
    s_p_l.grid(row=2, column=0)

    def login_std():
        if s_i.get().upper() == "STUDENT" and s_p.get() == "student@2023":
            std_m_l = Label(stud_portal, text="ENTER YOUR MATRIC NO.")
            std_m_l.grid(row=3, column=0, padx=50, pady=20)
            std_m = Entry(stud_portal)
            std_m.grid(row=3, column=1)

            def check_but():
                # stud_portal.destroy()
                # result = Tk()
                # result.title("STUDENT RESULT VIEW")
                # result.geometry("640x450")
                # result_l = Label(result, text="STUDENT RESULT VIEW")
                # result_l.grid(row=0, column=0, padx=80, pady=20)
                cl = std_m.get()
                conn = sqlite3.connect('student.db')
                c = conn.cursor()
                c.execute("SELECT * FROM student_result WHERE std_matric = {}".format(cl))
                d = (c.fetchall())
                for row in d:
                    subjects = f"{row[1]}, these are your scores:- \n" \
                             f"MATHS - {row[2]}\n" \
                             f"ENGLISH - {row[3]}\n" \
                             f"COMPUTER - {row[4]}\n" \
                             f"BIOLOGY - {row[5]}\n" \
                             f"CHEMISTRY - {row[6]}\n" \
                             f"PHYSICS - {row[7]}\n" \
                             f"CIVIC - {row[8]}\n" \
                             f"FURTHERMATHS - {row[9]}"
                    ov_ll = (row[2] + row[3] + row[4] + row[5] + row[6] + row[7] + row[8] + row[9]) / 800 * 100
                    final_result = ov_ll.__round__()
                    text_r = f"Your overall percentage is ({final_result}%)"
                    f_l = Label(stud_portal, text=text_r)
                    f_l.grid(row=5, column=1)
                    # print(subjects)
                    std_result = Label(stud_portal, text=subjects)
                    std_result.grid(row=5, column=0, padx=50)
            result_check = Button(stud_portal, text="CHECK RESULT", command=check_but)
            result_check.grid(row=4, column=1, padx=30)
    a_b = Button(stud_portal, text="LOGIN", command=login_std)
    a_b.grid(row=3, column=1, padx=50)


std_button = Button(Student_portal, text="CHECK YOUR RESULT ", command=st_page)
std_button.grid(row=2, column=0, pady=30)

Student_portal.mainloop()

# conn = sqlite3.connect('student.db')
# c = conn.cursor()
# c.execute("""SELECT * FROM student_result """)
# items = c.fetchall()
# for item in items:
#     print(item)
# conn.commit()
# conn.close()
