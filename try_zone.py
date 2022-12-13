import pandas as pd
from abc import *
from tkinter import *

class depot_management(ABC):    
        pass
class warehouse_management(depot_management):
        
        @abstractmethod
        def set_warehouse_id(self):
                pass
        
        @abstractmethod
        def get_warehouse_id(self):
                pass
        
class item_management(depot_management,ABC):
        @abstractmethod
        def item_id(self):
                pass
        
        @abstractmethod
        def item_name(self):
                pass

        @abstractmethod
        def item_position(self):
                pass
        
        @abstractmethod
        def item_amount(self):
                pass

class item_Printer(item_management):
        def item_id():
                return "1"
                
        def item_name():
                return "Printer"
        
        def item_position(position):
                return position
        
        def item_amount(amount):
                return amount
        

class item_PC(item_management):
        def item_id():
                return "2"
                
        def item_name():
                return "PC"
                
        def item_position(position):
                return position
        
        def item_amount(amount):
                return amount
   
   
def item_name_to_ID(x):
        if x == "PC":
                item_id_entry.config(state="normal")
                item_id_entry.delete(0,END)
                item_id_entry.insert(END,item_PC.item_id())
                item_id_entry.config(state="disabled")
        elif x == "Printer":
                item_id_entry.config(state="normal")
                item_id_entry.delete(0,END)
                item_id_entry.insert(END,item_Printer.item_id())
                item_id_entry.config(state="disabled")
                        
def add_to_list():
        if item_name_var.get() == "Printer":
                data_item_name_list.append("Printer")
                data_item_id_list.append("1")
                data_item_position_list.append(item_position_var.get())
                data_item_amount_list.append(item_amount_entry.get())
        elif item_name_var.get() == "PC":
                data_item_name_list.append("PC")
                data_item_id_list.append("2")
                data_item_position_list.append(item_position_var.get())
                data_item_amount_list.append(item_amount_entry.get())
                        
                
                        
#------------------------------------------------               


data_previous = pd.read_excel("output1.xlsx")
print(data_previous)


#------------------------------------------------
data_item_position_list = []
data_item_id_list = []
data_item_name_list = []
data_item_amount_list = []
warehouse_list =[
        "Warehouse Ankara",
        "Warehouse Istanbul",
        "Warehouse Izmir",
        "Warehouse Çanakkale"
]
item_name_list = [
        "Printer",
        "PC"
]


#------------------------------------------------
# <- Data management starts here

data = {
        "Item ID" : data_item_id_list,
        "Item Name" : data_item_name_list,
        "Item Position" : data_item_position_list,
        "Item Amount" : data_item_amount_list
        }
for x in data_item_id_list:
        data["Item ID"].append(data_item_id_list[x])
        
for x in data_item_name_list:
        data["Item Name"].append(data_item_name_list(x))

for x in data_item_position_list:
        data["Item Position"].append(data_item_position_list(x))
        
for x in data_item_amount_list:
        data["Item Amount"].append(data_item_amount_list(x))
# <- Data management ends here

        #-------------------UI START------------------

        # <- base starts here
        
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
    global item_id_entry,item_position_var,item_name_var, item_amount_entry
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
                if access_level == "Admin" or access_level == "Worker":
                    root = Tk()
                    root.title("Warehouse Management")
                    root.geometry("300x160")
                    root.resizable(0,0)

                    # <- base ends here
                    #---------------------------------------------
                    # <- labelling starts here

                    item_name_label = Label(root, text = "Item Name")
                    item_name_label.grid(column = 0, row = 0, padx = 5, pady = 5)

                    item_id_label = Label(root, text = "Item ID")
                    item_id_label.grid(column = 0, row = 1, padx = 5, pady = 5)

                    item_position_label = Label(root, text = "Item Position")
                    item_position_label.grid(column = 0, row = 2, padx = 5, pady = 5)

                    item_amount_label = Label(root, text = "Item Amount")
                    item_amount_label.grid(column = 0, row = 3, padx = 5, pady = 5)

                    # <- labelling ends here
                    #---------------------------------------------
                    # <- optionmenus starts here

                    item_name_var = StringVar(root)
                    item_name_var.set(item_name_list[0])
                    item_name_option_menu = OptionMenu(root, item_name_var,*item_name_list, command = item_name_to_ID)
                    item_name_option_menu.config(width = 17)
                    item_name_option_menu.grid(column  =1,row = 0, padx = 5, pady = 5)

                    item_position_var = StringVar(root)
                    item_position_var.set("")
                    item_position_option_menu = OptionMenu(root, item_position_var, *warehouse_list)
                    item_position_option_menu.config(width = 17)
                    item_position_option_menu.grid(column = 1, row = 2, padx = 5, pady = 5) 

                    # <- optionmenus ends here
                    #---------------------------------------------
                    # <- entrys starts here

                    item_id_entry = Entry(root, justify = CENTER)
                    item_id_entry.insert(0,"Item ID")
                    item_id_entry.config(state = "disabled", width = 23)
                    item_id_entry.grid(column = 1,row = 1, padx = 5, pady = 5)

                    item_amount_entry = Entry(root, justify = CENTER)
                    item_amount_entry.config(width = 23)
                    item_amount_entry.grid(column = 1, row = 3, padx = 5, pady = 5)

                    # <- entrys ends here
                    #---------------------------------------------
                    # <- buttons starts here

                    add_to_list_button = Button(root, text = "Add", command = add_to_list)
                    add_to_list_button.grid(row = 0, column = 3, rowspan = 4, padx = 5, pady = 5)
                    add_to_list_button.config(height= 9, width = 5)
                    root.mainloop()
                elif access_level == "Admin" or access_level == "Security":
                        pass


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

#--------------------UI END-------------------
        

# df = pd.DataFrame(data)
# df.to_excel(r'desktop\File Name.xlsx', index=False)
# print(df)

# print(data)
# print(data_item_id_list)
# print(data_item_name_list)
# print(data_item_position_list)
# print(data_item_amount_list)

data = pd.DataFrame(data)
print(data)

new_data = pd.concat([data_previous,data], ignore_index=True)
new_data.reset_index()
new_data.drop("Unnamed: 0", inplace = True, axis = 1)
new_data.to_excel('output1.xlsx')



# data.to_excel('output1.xlsx')
# print(data)