import pandas as pd
from abc import *
from tkinter import *
import cv2 as cv



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
cam_for_warehouse_list = [
                          4,
                          4,
                          2,
                          2
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
    global access_level,login_person
    access_list = user_data.loc[user_data["ID"] == int(username_entry.get())]
    access_list = access_list.values.tolist()
    if username_entry.get() == str(access_list[0][0]):
            if password_entry.get() == str(access_list[0][2]):
                login_person = "Welcome "+ access_list[0][1] + "."
                user_panel.destroy()
                welcome_page = Tk()
                welcome_page.title("STATUS")
                welcome_page.geometry("500x400")
                welcome_page.config(bg = "#e3dac9")
                welcome_page.resizable(0,0)
                person_label = Label(welcome_page, text = login_person, bg = "#e3dac9", font=("Arial", 20))
                person_label.place(relx = .5, rely = .4, anchor=CENTER)
                
                if access_list[0][3] == 1 and access_list[0][4] == 1:
                    access_level = "Admin"
                    
                elif access_list[0][3] == 1:
                    access_level = "Worker"
                    
                else:
                    access_level = "Security"
                
                access_level_label = Label(welcome_page, text = "Your access level is " + access_level, bg = "#e3dac9", font=("Arial", 17))
                access_level_label.place(relx = .5, y= 210,anchor=CENTER)
                warning_label = Label(welcome_page, text = "Please don't close this page while you are working", bg = "#e3dac9", font=("Arial", 13,"italic"))
                warning_label.place(relx= .5, y = 275, anchor=CENTER)
                if access_level == "Admin":
                        management_page_open() 
                        cam_page_open()
                elif access_level == "Security":
                        work_station = access_list[0][5]
                        work_station_label = Label(welcome_page, text = "Your work station is " + work_station,bg = "#e3dac9", font=("Arial", 17))
                        work_station_label.place(relx = 0.5, y = 245, anchor=CENTER)
                        cam_page_open()
                elif access_level == "Worker":
                        management_page_open()


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

def management_page_open():
        global username_entry,item_id_entry,item_position_var,item_name_var, item_amount_entry
        management_page = Tk()
        management_page.title("Warehouse Management")
        management_page.geometry("500x400")
        management_page.resizable(0,0)

        # <- base ends here
        #---------------------------------------------
        # <- labelling starts here

        item_name_label = Label(management_page, text = "Item Name")
        item_name_label.grid(column = 0, row = 0, padx = 5, pady = 5)

        item_id_label = Label(management_page, text = "Item ID")
        item_id_label.grid(column = 0, row = 1, padx = 5, pady = 5)

        item_position_label = Label(management_page, text = "Item Position")
        item_position_label.grid(column = 0, row = 2, padx = 5, pady = 5)

        item_amount_label = Label(management_page, text = "Item Amount")
        item_amount_label.grid(column = 0, row = 3, padx = 5, pady = 5)

        # <- labelling ends here
        #---------------------------------------------
        # <- optionmenus starts here

        item_name_var = StringVar(management_page)
        item_name_var.set(item_name_list[0])
        item_name_option_menu = OptionMenu(management_page, item_name_var,*item_name_list, command = item_name_to_ID)
        item_name_option_menu.config(width = 17)
        item_name_option_menu.grid(column  =1,row = 0, padx = 5, pady = 5)

        item_position_var = StringVar(management_page)
        item_position_var.set("")
        item_position_option_menu = OptionMenu(management_page, item_position_var, *warehouse_list)
        item_position_option_menu.config(width = 17)
        item_position_option_menu.grid(column = 1, row = 2, padx = 5, pady = 5) 

        # <- optionmenus ends here
        #---------------------------------------------
        # <- entrys starts here

        item_id_entry = Entry(management_page, justify = CENTER)
        item_id_entry.insert(0,"Item ID")
        item_id_entry.config(state = "disabled", width = 23)
        item_id_entry.grid(column = 1,row = 1, padx = 5, pady = 5)

        item_amount_entry = Entry(management_page, justify = CENTER)
        item_amount_entry.config(width = 23)
        item_amount_entry.grid(column = 1, row = 3, padx = 5, pady = 5)

        # <- entrys ends here
        #---------------------------------------------
        # <- buttons starts here

        add_to_list_button = Button(management_page, text = "Add", command = add_to_list)
        add_to_list_button.grid(row = 0, column = 3, rowspan = 4, padx = 5, pady = 5)
        add_to_list_button.config(height= 9, width = 5)



def cam_page_open():
        global cam_page
        cam_page = Tk()
        cam_page.title("Camera Management")
        cam_page.geometry("500x400")
        cam_page.resizable(0,0)
        cam_page.config(bg = "#e3dac9")
        login_person_name = login_person.split(" ")
        login_person_name = login_person_name[1]
        login_person_name = login_person_name.split(".")
        login_person_name = login_person_name[0]
        work_station = user_data.loc[user_data["Fullname"] == login_person_name]
        work_station = work_station.values.tolist()
        
        
                 
                                
        if work_station[0][5] == "all":
                
                for i in range(0,4):
                        name_of_warehouse = warehouse_list[i]
                        button_i = Button(cam_page, text = warehouse_list[i], bg = "#e3dac9", font=("Arial", 17), command = open_page_cam)
                        button_i.config(justify=CENTER, width = 250)
                        button_i.pack()
                        
        elif work_station[0][5] == warehouse_list[0]:
                for i in range(0, cam_for_warehouse_list[0]):
                        button_cami = Button(cam_page, text = "CAM "+ str(i), bg = "#e3dac9", font=("Arial", 17), command = open_page_cam)
                        button_cami.config(justify=CENTER, width = 250)
                        button_cami.pack()
                
        elif work_station[0][5] == warehouse_list[1]:
                for i in range(0, cam_for_warehouse_list[1]):
                        button_cami = Button(cam_page, text = "CAM "+ str(i), bg = "#e3dac9", font=("Arial", 17), command = open_page_cam)
                        button_cami.config(justify=CENTER, width = 250)
                        button_cami.pack()
        elif work_station[0][5] == warehouse_list[2]:
                for i in range(0, cam_for_warehouse_list[2]):
                        button_cami = Button(cam_page, text = "CAM "+ str(i), bg = "#e3dac9", font=("Arial", 17), command = open_page_cam)
                        button_cami.config(justify=CENTER, width = 250)
                        button_cami.pack()
        elif work_station[0][5] == warehouse_list[2]:
                for i in range(0, cam_for_warehouse_list[1]):
                        button_cami = Button(cam_page, text = "CAM "+ str(i), bg = "#e3dac9", font=("Arial", 17), command = open_page_cam)
                        button_cami.config(justify=CENTER, width = 250)
                        button_cami.pack()
        
        
        cam_page.mainloop()
def open_page_cam():
                 cam_page.destroy()
                 cam_cord = cv.VideoCapture(0)
                 while (True):
                         _, frame = cam_cord.read()
                         cv.imshow("CAM 0", frame)
                         if cv.waitKey(1) & 0xFF == ord('q'):
                                break
                 cam_cord.release()
                 cv.destroyAllWindows()    
                 cam_page_open()  

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

print(new_data)




# data.to_excel('output1.xlsx')
# print(data)