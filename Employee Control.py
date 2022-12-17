import pandas as pd
from tkinter import *

data_id_list = []
data_name_list = []
data_pw_list = []
data_data_access_list = []
data_cam_access_list = []
data_workstation_list = []

user_add_page = Tk()
user_add_page.title("Employee Control")
user_add_page.geometry("500x500")
user_add_page.resizable(0,0)
user_add_page.config(bg = "#e3dac9")

employee = pd.read_excel("Employee.xlsx")
employee_id = employee["ID"].values.tolist()
employee_pw = employee["Password"].values.tolist()
employee_data_access = employee["data_access"].values.tolist()
employee_cam_access = employee["cam_access"].values.tolist()
employee_workstation = employee["work_station"].values.tolist()



id_list = []
pw_list = []
data_access_list = []
cam_access_list = []
workstation_list = []


for i in employee_id:
    id_list.append(i)
    
for i in employee_pw:
    pw_list.append(i)
    
for i in employee_data_access:
    data_access_list.append(i)
    
for i in employee_cam_access:
    cam_access_list.append(i)
    
for i in employee_workstation:
    workstation_list.append(i)

employee_list = []
employee_list.append(id_list)
employee_list.append(pw_list)
employee_list.append(data_access_list)
employee_list.append(cam_access_list)
employee_list.append(workstation_list)




new_id = Label(user_add_page, text = "ID",font=("Arial", 13), bg = "#e3dac9")
new_id.place(x = 25, y = 25)

new_name = Label(user_add_page,text = "Fullname",font=("Arial", 13), bg = "#e3dac9")
new_name.place(x = 25, y = 75)

new_pw = Label(user_add_page, text = "Password",font=("Arial", 13), bg = "#e3dac9")
new_pw.place(x = 25, y = 125)

two_dot_label1 = Label(user_add_page, text = ":",font=("Arial", 18), bg = "#e3dac9")
two_dot_label1.place(x=130, y = 20)



two_dot_label2 = Label(user_add_page, text = ":",font=("Arial", 18), bg = "#e3dac9")
two_dot_label2.place(x=130, y = 70)

id_entry = Entry(user_add_page)
id_entry.place(x = 145, y=  27, width= 250, height=20)

name_entry = Entry(user_add_page)
name_entry.place(x = 145, y=  77, width= 250, height=20)

two_dot_label7 = Label(user_add_page, text = ":",font=("Arial", 18), bg = "#e3dac9")
two_dot_label7.place(x=130, y = 120)

pw_entry = Entry(user_add_page)
pw_entry.place(x = 145, y=  127, width= 250, height=20)

data_access_radio_label = Label(user_add_page, text = "Data Access",font=("Arial", 13), bg = "#e3dac9")
data_access_radio_label.place(x = 25, y = 175)

var_data = IntVar()

data_access_radio = Radiobutton(user_add_page, text = "Yes",variable = var_data,value=1, bg = "#e3dac9")
data_access_radio.place(x = 145, y = 175)

data_access_radio = Radiobutton(user_add_page, text = "No",variable = var_data,value = 0, bg = "#e3dac9")
data_access_radio.place(x = 195, y = 175)

two_dot_label3 = Label(user_add_page, text = ":",font=("Arial", 18), bg = "#e3dac9")
two_dot_label3.place(x=130, y = 170)

var_cam = IntVar()

cam_access_radio_label = Label(user_add_page, text = "Cam Access",font=("Arial", 13), bg = "#e3dac9")
cam_access_radio_label.place(x = 25, y = 225)

cam_access_radio = Radiobutton(user_add_page, text = "Yes",variable = var_cam,value=1, bg = "#e3dac9")
cam_access_radio.place(x = 145, y = 225)

cam_access_radio = Radiobutton(user_add_page, text = "No",variable = var_cam,value = 0, bg = "#e3dac9")
cam_access_radio.place(x = 195, y = 225)

two_dot_label4 = Label(user_add_page, text = ":",font=("Arial", 18), bg = "#e3dac9")
two_dot_label4.place(x=130, y = 220)

work_station_label = Label(user_add_page, text = "Work Station",font=("Arial", 13), bg = "#e3dac9")
work_station_label.place( x = 25, y = 275)

two_dot_label5 = Label(user_add_page, text = ":",font=("Arial", 18), bg = "#e3dac9")
two_dot_label5.place(x=130, y = 270)

work_station_var = StringVar(user_add_page)
work_station_var.set("")

warehouse_list =[
        "All",
        "Warehouse Ankara",
        "Warehouse Istanbul",
        "Warehouse Izmir",
        "Warehouse Çanakkale"
]

work_station_optionmenu = OptionMenu(user_add_page, work_station_var, *warehouse_list)
work_station_optionmenu.place(x = 145, y = 275)







def add_user():
    data_id_list.append(id_entry.get())
    data_name_list.append(name_entry.get())
    data_pw_list.append(pw_entry.get())
    data_data_access_list.append(var_data.get())
    data_cam_access_list.append(var_cam.get())
    data_workstation_list.append(work_station_var.get())
    
    



add_button = Button(user_add_page, text = "ADD",font=("Arial", 13), bg = "#e3dac9",command = add_user)
add_button.place(x = 165, y = 325)

def delete():
    pass

data = {
        "ID" : data_id_list,
        "Fullname" : data_name_list,
        "Password" : data_pw_list,
        "data_access" : data_data_access_list,
        "cam_access" : data_cam_access_list,
        "work_station" : data_workstation_list
        }
        
for x in data_id_list:
        data["ID"].append(data_id_list(x))

for x in data_name_list:
        data["Fullname"].append(data_name_list(x))
        
for x in data_pw_list:
        data["Password"].append(data_pw_list(x))
        
for x in data_data_access_list:
        data["data_access"].append(data_data_access_list(x))
        
for x in data_cam_access_list:
        data["cam_access"].append(data_cam_access_list(x))
        
for x in data_workstation_list:
        data["work_station"].append(data_workstation_list(x))

        
user_add_page.mainloop()
data_previous = pd.read_excel("Employee.xlsx")

data = pd.DataFrame(data)
print(data)
new_data = pd.concat([employee,data], ignore_index=True)

new_data.drop("Unnamed: 0", inplace = True, axis = 1)

new_data.to_excel("Employee.xlsx")