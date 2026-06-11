from tkinter import *
from tkinter import messagebox
import sqlite3
import webbrowser

# Database Connection
conn = sqlite3.connect("placement.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")
conn.commit()

# Functions
def home():
    clear_frame()
    Label(frame, text="Campus Placement Registration System",
          font=("Arial", 18, "bold")).pack(pady=20)

    total = cur.execute("SELECT COUNT(*) FROM student").fetchone()[0]

    Label(frame, text=f"Total Registered Students: {total}",
          font=("Arial", 14)).pack(pady=10)


def about():
    clear_frame()
    Label(frame, text="About Project", font=("Arial", 18, "bold")).pack(pady=10)

    Label(frame, text="""
Campus Placement Registration System

Features:
• Register Student
• View Students
• Delete Student
• Login
• Update Profile
• Total Student Count
• Open Company Website after Login
""", justify=LEFT).pack()


def register_student():
    clear_frame()

    Label(frame, text="Register Student", font=("Arial", 18, "bold")).pack(pady=10)

    Label(frame, text="Name").pack()
    name_entry = Entry(frame)
    name_entry.pack()

    Label(frame, text="Email").pack()
    email_entry = Entry(frame)
    email_entry.pack()

    def save():
        name = name_entry.get()
        email = email_entry.get()

        if name and email:
            cur.execute(
                "INSERT INTO student(name,email) VALUES(?,?)",
                (name, email)
            )
            conn.commit()
            messagebox.showinfo("Success", "Student Registered")
            home()
        else:
            messagebox.showerror("Error", "Fill all fields")

    Button(frame, text="Register", command=save).pack(pady=10)


def view_students():
    clear_frame()

    Label(frame, text="Student Records",
          font=("Arial", 18, "bold")).pack(pady=10)

    students = cur.execute("SELECT * FROM student").fetchall()

    text = Text(frame, width=60, height=15)
    text.pack()

    text.insert(END, "ID\tName\tEmail\n")
    text.insert(END, "-"*50 + "\n")

    for s in students:
        text.insert(END, f"{s[0]}\t{s[1]}\t{s[2]}\n")


def delete_student():
    clear_frame()

    Label(frame, text="Delete Student",
          font=("Arial", 18, "bold")).pack(pady=10)

    Label(frame, text="Enter Email").pack()

    email_entry = Entry(frame)
    email_entry.pack()

    def delete():
        email = email_entry.get()

        cur.execute("DELETE FROM student WHERE email=?", (email,))
        conn.commit()

        messagebox.showinfo("Success", "Student Deleted")

    Button(frame, text="Delete", command=delete).pack(pady=10)


def login():
    clear_frame()

    Label(frame, text="Login", font=("Arial", 18, "bold")).pack(pady=10)

    Label(frame, text="Email").pack()
    email_entry = Entry(frame)
    email_entry.pack()

    def check():
        email = email_entry.get()

        data = cur.execute(
            "SELECT * FROM student WHERE email=?",
            (email,)
        ).fetchone()

        if data:
            messagebox.showinfo("Success", "Login Successful")

            # Open company website
            webbrowser.open("https://www.tcs.com")

        else:
            messagebox.showerror("Error", "Student Not Found")

    Button(frame, text="Login", command=check).pack(pady=10)


def update_profile():
    clear_frame()

    Label(frame, text="Update Profile",
          font=("Arial", 18, "bold")).pack(pady=10)

    Label(frame, text="Existing Email").pack()
    old_email = Entry(frame)
    old_email.pack()

    Label(frame, text="New Name").pack()
    new_name = Entry(frame)
    new_name.pack()

    Label(frame, text="New Email").pack()
    new_email = Entry(frame)
    new_email.pack()

    def update():
        cur.execute("""
        UPDATE student
        SET name=?, email=?
        WHERE email=?
        """,
        (new_name.get(), new_email.get(), old_email.get()))

        conn.commit()

        messagebox.showinfo("Success", "Profile Updated")

    Button(frame, text="Update", command=update).pack(pady=10)


def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()


# Main Window
root = Tk()
root.title("Campus Placement Registration System")
root.geometry("700x500")

menu = Frame(root)
menu.pack(side=LEFT, fill=Y)

Button(menu, text="Home", width=20, command=home).pack(pady=2)
Button(menu, text="About", width=20, command=about).pack(pady=2)
Button(menu, text="Register Student", width=20,
       command=register_student).pack(pady=2)
Button(menu, text="View Students", width=20,
       command=view_students).pack(pady=2)
Button(menu, text="Delete Student", width=20,
       command=delete_student).pack(pady=2)
Button(menu, text="Login", width=20,
       command=login).pack(pady=2)
Button(menu, text="Update Profile", width=20,
       command=update_profile).pack(pady=2)

frame = Frame(root)
frame.pack(side=RIGHT, fill=BOTH, expand=True)

home()

root.mainloop()

conn.close()