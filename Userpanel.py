from tkinter import *
import pandas as pd

user_data = pd.read_excel("Employee.xlsx")

user_id = user_data["ID"].values.tolist()
user_pw = user_data["Password"].values.tolist()
user_data_access = user_data["data_access"]
user_cam_access = user_data["cam_access"]
user_data_access_len = len(user_data_access)
user_cam_access_len = len(user_cam_access)

user_panel = Tk()
user_panel.title("LOGIN")
user_panel.geometry("500x400")
user_panel.config(bg = "#e3dac9")
user_panel.resizable(0,0)


def login():
    access_list = user_data.loc[user_data["ID"] == int(username_entry.get())]
    access_list = access_list.values.tolist()
    if username_entry.get() == str(access_list[0][0]):
            if password_entry.get() == str(access_list[0][1]):
                login_person = "Welcome "+ username_entry.get() + "."
                user_panel.destroy()
                welcome_page = Tk()
                welcome_page.title("LOGIN")
                welcome_page.geometry("500x400")
                welcome_page.config(bg = "#e3dac9")
                welcome_page.resizable(0,0)
                person_label = Label(welcome_page, text = login_person, bg = "#e3dac9", font=("Arial", 20))
                person_label.place(relx = .5, rely = .4, anchor=CENTER)
                
                if access_list[0][2] == 1 and access_list[0][3] == 1:
                    access_level = "Admin"
                elif access_list[0][2] == 1:
                    access_level = "Worker"
                else:
                    access_level = "Security"
                
                access_level_label = Label(welcome_page, text = "Your access level is " + access_level, bg = "#e3dac9", font=("Arial", 20))
                access_level_label.place(relx = .5, y= 200,anchor=CENTER)
            

user_panel_label = Label(user_panel, text = "USER PANEL", relief=SOLID, font=("Arial", 50), bg = "#e3dac9")
user_panel_label.place(x = 35, y = 30)

two_dot_label1 = Label(user_panel, text = ":",font=("Arial", 20), bg = "#e3dac9")
two_dot_label1.place(x=200, y = 150)

two_dot_label2 = Label(user_panel, text = ":",font=("Arial", 20), bg = "#e3dac9")
two_dot_label2.place(x=200, y = 200)

username_label = Label(user_panel, text = "Employee ID", font=("Arial", 20), bg = "#e3dac9")
username_label.place(x= 35, y = 150)

username_entry = Entry(user_panel)
username_entry.place(x = 215, y=  160, width= 250, height=22)

password_label = Label(user_panel, text= "Password", font=("Arial", 20), bg = "#e3dac9")
password_label.place(x = 35, y = 200)

password_entry = Entry(user_panel, show = "*")
password_entry.place(x = 215, y=  210, width= 250, height=22)

exit_button = Button(user_panel, text = "EXIT", command= exit,width= 30, height= 3, bg = "Red")
exit_button.place(x = 250, y = 300)

login_button = Button(user_panel, text = "LOGIN", command= login,width= 30, height= 3, bg = "Green")
login_button.place(x = 25, y = 300)



user_panel.mainloop()