from tkinter import *                       #tkinter library
from datetime import *                      #Datetime library
import sqlite3
from tkinter import messagebox
db=sqlite3.connect("phonebook.db")
c=db.cursor()


date=datetime.now().date()                  #object for date
date=str(date)

class Application(object):                      #object is used here as arbitary argument
    def __init__(self, master):
        self.master=master

        #frames
        self.top=Frame(master, height=150, bg="white")          #top frame
        self.top.pack(fill=X)

        self.bottom=Frame(master, height=500, bg="#34baeb")     #bottom frame
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image=PhotoImage(file="icons/book.png")   #image
        self.top_image_label=Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=140, y=10)

        self.heading=Label(self.top, text="PhoneBook", font="arial 25 bold", bg="white",fg="orange")       #heading
        self.heading.place(x=300, y=60)

        self.date_lbl=Label(self.top, text=date, font="arial 12 bold", fg="orange", bg="white")
        self.date_lbl.place(x=550,y=20)

        #bottom frame design

        #button1=view
        self.photo_ppl = PhotoImage(file=r"icons\ppl_hm.png")
        self.view_button = Button(self.bottom, text="     My People     ",bg="white", fg="#34baeb" , font="arial 12 bold", image=self.photo_ppl,compound=LEFT ,command=self.my_people)
        self.view_button.place(x=200, y=70)

        #button2=add
        self.photo_add = PhotoImage(file=r"icons\add_hm.png")
        self.add_button = Button(self.bottom, text="    Add People    ", bg="white",fg="#34baeb",font="arial 12 bold",image=self.photo_add,compound=LEFT ,command=self.add_ppl)
        self.add_button.place(x=200, y=300)


    def my_people(self):
        people=MyPeople()           #object of mypeople class

    def add_ppl(self):
        addpplwindow=AddPeople()    #object of addpeople class



class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550+850+150")
        self.title("Add New Person")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg="white")  # top frame
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="orange")  # bottom frame
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file="icons/add.png")  # image
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=140, y=10)

        self.heading = Label(self.top, text="Add New Person", font="arial 20 bold", bg="white",
                             fg="#34baeb")  # heading
        self.heading.place(x=300, y=60)

        # name
        self.label_name = Label(self.bottom, text="NAME", font="airal 13 bold", fg="white", bg="orange")
        self.label_name.place(x=40, y=50)

        self.entry_name = Entry(self.bottom, width=40, bd=2)
        self.entry_name.insert(0, "enter name")
        self.entry_name.place(x=170, y=50)

        # surname
        self.label_surname = Label(self.bottom, text="SURNAME", font="airal 13 bold", fg="white", bg="orange")
        self.label_surname.place(x=40, y=100)

        self.entry_surname = Entry(self.bottom, width=40, bd=2)
        self.entry_surname.insert(0, "enter surname")
        self.entry_surname.place(x=170, y=100)

        # email
        self.label_email = Label(self.bottom, text="EMAIL ID", font="airal 13 bold", fg="white", bg="orange")
        self.label_email.place(x=40, y=150)

        self.entry_email = Entry(self.bottom, width=40, bd=2)
        self.entry_email.insert(0, "enter E-mail ID")
        self.entry_email.place(x=170, y=150)

        # phone
        self.label_phone = Label(self.bottom, text="PHONE NO", font="airal 13 bold", fg="white", bg="orange")
        self.label_phone.place(x=40, y=200)

        self.entry_phone = Entry(self.bottom, width=40, bd=2)
        self.entry_phone.insert(0, "enter phone number")

        self.entry_phone.place(x=170, y=200)

        # address
        self.label_address = Label(self.bottom, text="ADDRESS", font="airal 13 bold", fg="white", bg="orange")
        self.label_address.place(x=40, y=250)

        self.entry_address = Text(self.bottom, width=30, height=5)
        self.entry_address.place(x=170, y=250)

        # button

        self.save_button = Button(self.bottom, text="Add Person", font="arial 13 bold", bg="white", fg="#34baeb",
                                  bd=4, command=self.add_people)
        self.save_button.place(x=300, y=350)

    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')

        if name and surname and email and phone and address != "":
            if len(phone) != 10:
                messagebox.showinfo("Error", "enter valid phone number", icon="warning")

            elif "@" not in email:
                messagebox.showinfo("Error", "enter valid email id", icon="warning")

            elif ".com" not in email:
                messagebox.showinfo("Error", "enter valid email id", icon="warning")

            else:
                c.execute(
                    "insert into 'addressbook' (person_name,person_surname,person_email,person_phone,person_address) values('{}','{}','{}','{}','{}')".format(
                        name, surname, email, phone, address))
                db.commit()
                messagebox.showinfo("success", "contact saved")
        else:
            messagebox.showerror("error", "fill all the fields", icon="warning")




class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x640+850+100")
        self.title("My People")
        self.resizable(False,False)


        self.top=Frame(self, height=150, bg="white")          #top frame
        self.top.pack(fill=X)

        self.bottom=Frame(self, height=500, bg="orange")     #bottom frame
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image=PhotoImage(file="icons/people.png")   #image
        self.top_image_label=Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=140, y=10)


        self.heading=Label(self.top, text="My People", font="arial 20 bold", bg="white",fg="#34baeb")      #heading
        self.heading.place(x=300, y=60)

        self.scroll=Scrollbar(self.bottom, orient=VERTICAL)

        self.listbox=Listbox(self.bottom, width=60, height=30)
        self.listbox.grid(row=0, column=0, padx=(40,0))
        self.listbox.config(yscrollcommand=self.scroll.set)


        persons=c.execute("select * from 'addressbook'").fetchall()
        count=0
        for i in persons:
            self.listbox.insert(count, str(i[0])+". "+i[1]+" "+i[2])
            count +=1

        self.scroll.grid(row=0, column=1, sticky=N+S)

        #buttons

        #add

        self.photo_ad=PhotoImage(file = r"icons\ad.png")
        self.btnadd= Button(self.bottom, text="      ADD        ", width=150, font="sans 12 bold", image = self.photo_ad , compound = LEFT, command=self.add_people)
        self.btnadd.place(x=450,y=60)



        #update
        self.photo_up = PhotoImage(file=r"icons\update.png")

        self.btnupdate = Button(self.bottom, text="   UPDATE   ", width=150, font="sans 12 bold", image = self.photo_up , compound = LEFT, command=self.update_people)
        self.btnupdate.place(x=450,y=120)


        #display
        self.photo_disp = PhotoImage(file=r"icons\display.png")

        self.btndisplay = Button(self.bottom, text="   DISPLAY   ", width=150, font="sans 12 bold", image = self.photo_disp , compound = LEFT, command=self.display_people)
        self.btndisplay.place(x=450,y=180)


        #delete
        self.photo_del = PhotoImage(file=r"icons\delete.png")

        self.btndelete = Button(self.bottom, text="   DELETE   ", width=150, font="sans 12 bold", image = self.photo_del , compound = LEFT, command=self.delete_people)
        self.btndelete.place(x=450,y=240)

    def add_people(self):
        add_page=AddPeople()
        self.destroy()

    def update_people(self):
        selected_item=self.listbox.curselection()
        person=self.listbox.get(selected_item)
        person_id=person.split(".")[0]
        updatepage=Update(person_id)
        self.destroy()

    def display_people(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        displaypage=Display(person_id)
        self.destroy()

    def delete_people(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]


        ans=messagebox.askquestion("warning","Are you sure you wanna delete this person information?", icon="warning")

        if ans=='yes':
            try:
                c.execute("delete from addressbook where person_id={}".format(person_id))
                db.commit()
                messagebox.showinfo("Success","Deleted")
                self.destroy()


            except EXCEPTION as e:
                messagebox.showinfo("info",str(e))





class Update(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry("650x550+850+150")
        self.title("Update Person")
        self.resizable(False,False)



        result=c.execute("select * from addressbook where person_id='{}'".format(person_id)).fetchone()
        self.person_id=person_id
        person_name =result[1]
        person_surname = result[2]
        person_email = result[3]
        person_phone = result[4]
        person_address = result[5]
        db.commit()

        self.top = Frame(self, height=150, bg="white")  # top frame
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="orange")  # bottom frame
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file="icons/add.png")  # image
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=140, y=10)

        self.heading = Label(self.top, text="Add New Person", font="arial 20 bold", bg="white", fg="#34baeb")  # heading
        self.heading.place(x=300, y=60)

        # name
        self.label_name = Label(self.bottom, text="NAME", font="airal 13 bold", fg="white", bg="orange")
        self.label_name.place(x=40, y=50)

        self.entry_name = Entry(self.bottom, width=40, bd=2)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=170, y=50)

        # surname
        self.label_surname = Label(self.bottom, text="SURNAME", font="airal 13 bold", fg="white", bg="orange")
        self.label_surname.place(x=40, y=100)

        self.entry_surname = Entry(self.bottom, width=40, bd=2)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.place(x=170, y=100)

        # email
        self.label_email = Label(self.bottom, text="EMAIL ID", font="airal 13 bold", fg="white", bg="orange")
        self.label_email.place(x=40, y=150)

        self.entry_email = Entry(self.bottom, width=40, bd=2)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=170, y=150)

        # phone
        self.label_phone = Label(self.bottom, text="PHONE NO", font="airal 13 bold", fg="white", bg="orange")
        self.label_phone.place(x=40, y=200)
        self.entry_phone = Entry(self.bottom, width=40, bd=2)
        self.entry_phone.insert(0, person_phone)
        self.entry_phone.place(x=170, y=200)

        # address
        self.label_address = Label(self.bottom, text="ADDRESS", font="airal 13 bold", fg="white", bg="orange")
        self.label_address.place(x=40, y=250)
        self.entry_address = Text(self.bottom, width=30, height=5)
        self.entry_address.insert(1.0, person_address)
        self.entry_address.place(x=170, y=250)

        # button

        self.save_button = Button(self.bottom, text="Update Person", font="arial 13 bold", bg="white", fg="#34baeb", bd=4, command=self.update_people)
        self.save_button.place(x=300, y=350)

    def update_people(self):
        id=self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address=self.entry_address.get(1.0,'end-1c')

        c.execute("update addressbook set person_name= '{}', person_surname= '{}', person_email= '{}', person_phone= '{}', person_address= '{}' where person_id= {}" .format(name,surname,email,phone,address, id))
        db.commit()
        messagebox.showinfo("success","Contact Updated")



class Display(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry("650x550+850+150")
        self.title("Display Person")
        self.resizable(False,False)



        result=c.execute("select * from addressbook where person_id='{}'".format(person_id)).fetchone()
        self.person_id=person_id
        person_name =result[1]
        person_surname = result[2]
        person_email = result[3]
        person_phone = result[4]
        person_address = result[5]
        db.commit()

        self.top = Frame(self, height=150, bg="white")  # top frame
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="orange")  # bottom frame
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file="icons/add.png")  # image
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=140, y=10)

        self.heading = Label(self.top, text="Person Details", font="arial 20 bold", bg="white", fg="#34baeb")  # heading
        self.heading.place(x=300, y=60)

        # name
        self.label_name = Label(self.bottom, text="NAME", font="airal 13 bold", fg="white", bg="orange")
        self.label_name.place(x=40, y=50)

        self.entry_name = Entry(self.bottom, width=40, bd=2)
        self.entry_name.insert(0, person_name)
        self.entry_name.config(state="disabled")
        self.entry_name.place(x=170, y=50)

        # surname
        self.label_surname = Label(self.bottom, text="SURNAME", font="airal 13 bold", fg="white", bg="orange")
        self.label_surname.place(x=40, y=100)

        self.entry_surname = Entry(self.bottom, width=40, bd=2)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.config(state="disabled")
        self.entry_surname.place(x=170, y=100)

        # email
        self.label_email = Label(self.bottom, text="EMAIL ID", font="airal 13 bold", fg="white", bg="orange")
        self.label_email.place(x=40, y=150)

        self.entry_email = Entry(self.bottom, width=40, bd=2)
        self.entry_email.insert(0, person_email)
        self.entry_email.config(state="disabled")
        self.entry_email.place(x=170, y=150)

        # phone
        self.label_phone = Label(self.bottom, text="PHONE NO", font="airal 13 bold", fg="white", bg="orange")
        self.label_phone.place(x=40, y=200)
        self.entry_phone = Entry(self.bottom, width=40, bd=2)
        self.entry_phone.insert(0, person_phone)
        self.entry_phone.config(state="disabled")
        self.entry_phone.place(x=170, y=200)

        # address
        self.label_address = Label(self.bottom, text="ADDRESS", font="airal 13 bold", fg="white", bg="orange")
        self.label_address.place(x=40, y=250)
        self.entry_address = Text(self.bottom, width=30, height=5)
        self.entry_address.insert(1.0, person_address)
        self.entry_address.config(state="disabled")
        self.entry_address.place(x=170, y=250)























def main():
    root=Tk()                                   #created object
    app=Application(root)                       #application class is called here and properties of root are passed
    root.title("PhoneBook")                     #title for window
    root.geometry("650x650+100+50")            #size of window
    root.resizable(False,False)                 #size should not vary

    root.mainloop()                             #to stop  this window on main window


main()
