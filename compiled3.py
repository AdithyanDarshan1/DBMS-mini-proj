import mysql.connector
import tkinter as tk
from tkinter import *
import customtkinter as ctk
from pathlib import Path
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk
from random import*
import mysql.connector
from tkinter import ttk
# Backend python functions code starts :
def createtable():
    conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
    cursor=conn.cursor()
    cursor.execute("create table if not exists customer(name varchar(50),address varchar(50),email varchar(30),phone varchar(50),age int,password varchar(50),account varchar(30))")
    conn.commit
    conn.close()
    
def deletecustomer(accountno):
    conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
    cursor=conn.cursor()
    cursor.execute('delete from customer where account=?',(accountno))
    conn.commit()
    conn.close()
def accountexist():
    conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
    cursor=conn.cursor()
    cursor.execute("select count(*) from customer where account='"+entry1.get()+"'"+"and password='"+entry2.get()+"'")
    result=cursor.fetchone()
    conn.close()
    return result[0]>0

    # frontend python functions code starts :

window=ctk.CTk()
def welcome():
    window.geometry("600x450+383+106")
    window.title("Start Page")
    window.config(bg='navy')
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    frame=ctk.CTkFrame(master=window,fg_color='yellow2')
    frame.pack(pady=50,padx=80,fill="both",expand=True)
    label1=ctk.CTkLabel(master=frame,text="Welcome To Our Bank",font=("TkHeadingFont",26))
    label1.pack(pady=20,padx=40)
    button1=ctk.CTkButton(master=frame,text="admin",command=adminlogin)
    button1.pack(pady=20,padx=40)
    button2=ctk.CTkButton(master=frame,text="customer",command=customerlogin)
    button2.pack(pady=20,padx=40)
    '''img=ImageTk.PhotoImage(Image.open("./images/bank1.png"))
    label2=Label(image=img)
    label2.image=img
    label2.pack(pady=20)'''

def status():
    print("test")
def delete():
    print("test")
def support():
        nw4=Toplevel(window)
        nw4.geometry("600x500")
        nw4.title("Customer Support")
        ctk.set_appearance_mode("light")
        nw4.config(bg='blue4')
        framemsg=ctk.CTkFrame(master=nw4,width=100,height=100,corner_radius=15,fg_color='ivory2')
        framemsg.pack(pady=20,padx=40,fill="both",expand=True)
        actext=ctk.CTkLabel(master=framemsg,text='''Thank you for reaching us,

    for further help
    
        contact:4563728913
        or
        email:customerhelp@gmail.com''',font=("Arial",20),text_color='black')
        actext.pack(pady=20,padx=40)
        '''userimg=Image.open("./images/custserv.png")
        resized=userimg.resize((200,200),Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized)
       
        labeluser=tk.Label(framemsg,image=tk_image)
        labeluser.image=tk_image
        labeluser.place(x=150,y=200)
        '''
def register():
    global a
    a=randint(100000000,999999999)
    name=entry3.get()
    address=entry4.get()
    email=entry5.get()
    phone=entry6.get()
    age=entry7.get()
    password=entry8.get()
    account=a
    if(name=="" or address=="" or email=="" or phone=="" or age=="" or password=="" ):
        messagebox.showinfo("Insert Status","All fields required")
    else:
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
        cursor=conn.cursor()
        query = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, address, email, phone, age, password, account)
        cursor.execute("select * from customer")
        rows=cursor.fetchall()
        for row in rows:
            if row[0]==name:
                entry3.delete(0,'end')
                entry4.delete(0,'end')
                entry5.delete(0,'end')
                entry6.delete(0,'end')
                entry7.delete(0,'end')
                entry8.delete(0,'end')
                messagebox.showinfo("Insert Status","Account already exists")
                cursor.close()
                conn.close
                  
        cursor.execute(query, values)
        conn.commit()
        entry3.delete(0,'end')
        entry4.delete(0,'end')
        entry5.delete(0,'end')
        entry6.delete(0,'end')
        entry7.delete(0,'end')
        entry8.delete(0,'end')
        conn.close()
        nw3=Toplevel(window)
        nw3.geometry("400x400")
        nw3.title("ACCOUNT NUMBER")
        ctk.set_appearance_mode("light")
        framemsg=ctk.CTkFrame(master=nw3,width=600,height=600,corner_radius=15,fg_color='ivory2')
        framemsg.pack(pady=0,padx=0,fill="both",expand=True)
        actext=ctk.CTkLabel(master=framemsg,text='''Registeration Successfull!!
        Account Number is:''',font=("TkHeading",15),text_color='black')
        actext.pack(pady=20,padx=40)
        label9=ctk.CTkLabel(master=framemsg,text=a,font=("TkHeading",26),text_color='black')
        label9.pack(pady=20,padx=40)
def transaction():
    # Backend+
    # python functions code starts :
    con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
    cur=con.cursor()
    '''Query="Create database if not exists bank"
    cur.execute(Query)
    con.commit()'''
    
    Query1="Create table if not exists transaction (accno integer primary key,balance integer);"
    cur.execute(Query1)
    con.commit()

    query4="select * from customer"
    cur.execute(query4)
    data1=cur.fetchall()

    for row in data1:   
        if (row[6]==account):
        # Check if the record already exists
            query_check = "SELECT 1 FROM transaction WHERE accno = %s LIMIT 1"
            values1 = (account,)
            cur.execute(query_check, values1)
            exists = cur.fetchone()
            if not exists:
                # Record doesn't exist, so insert a new record
                query5 = "INSERT INTO transaction (accno,balance) values(%s,0)"
                values = (account,)
                cur.execute(query5, values)
                con.commit()
            else:
                break

    query3="select * from transaction"
    cur.execute(query3)
    data2=cur.fetchall()
    con.close()
    def create_transaction_table(account):
        con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
        cur=con.cursor()
        table_name = f"transaction_{account}"
        cur.execute(f"SHOW TABLES LIKE '{table_name}'")
        table_exists = cur.fetchall()
        if not table_exists:
            query2 = f"""
            CREATE TABLE if not exists {table_name} (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                credited DECIMAL(10, 2),
                debited DECIMAL(10, 2),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cur.execute(query2)
            con.commit()

    for row in data2:
        exists = cur.fetchone()
        if not exists:
            create_transaction_table(row[0])

    def fetchtransac(): 
        cur=con.cursor()
        table_name = f"transaction_{account}"
        cur.execute(f"SHOW TABLES LIKE '{table_name}'")
        table_exists = cur.fetchall()
        if table_exists:
            cur.execute(f'select * from {table_name}')
            transaccno=cur.fetchall()
            con.commit()
            return transaccno

    con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
    cur=con.cursor()
    global bal
    x="select balance from transaction where accno=%s"
    cur.execute(x, (account,))
    bal=cur.fetchone()[0]
    bal =float(bal)
    
    #backend ends
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build1\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def update_balance_label():
            global bal
            canvas.itemconfig(tagOrId=balance_labelm, text=bal)
    def deposit():
        global bal
        OUTPUT_PATH2 = Path(__file__).parent
        ASSETS_PATH2 = OUTPUT_PATH2 / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build2\assets\frame0")

        def relative_to_assets2(path: str) -> Path:
            return ASSETS_PATH2 / Path(path)

        nwindow = Toplevel(window)
        nwindow.title("Deposit")
        nwindow.geometry("450x500")
        nwindow.configure(bg = "#1F43A0")

        def depbalance_update(entry_value):
            global bal
            try:
                # Convert the string to a float
                amount_to_deposit = float(entry_value)
                insert_query = "INSERT INTO transaction_"+str(account)+ "  (credited, debited) VALUES (%s, %s)"
                data = (amount_to_deposit, 0)
                cur.execute(insert_query, data)
                bal=bal+amount_to_deposit
                q = f"UPDATE transaction SET balance = {bal} WHERE accno = '{account}'"
                cur.execute(q)
                con.commit()
                canvas.itemconfig(tagOrId=balance_label,text=bal)
                
            except ValueError:
                messagebox.showinfo("Invalid input","Please enter a valid number.")
                #amount_to_deposit = float(entry_value)
        canvas = Canvas(
            nwindow,
            bg = "#1F43A0",
            height = 500,
            width = 450,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_12 = PhotoImage(
            file=relative_to_assets2("image_12.png"))
        image_2 = canvas.create_image(
            225.0,
            46.0,
            image=image_image_12
        )

        canvas.create_text(
            94.0,
            17.0,
            anchor="nw",
            text="Deposit",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        image_image_22 = PhotoImage(
            file=relative_to_assets2("image_22.png"))
        image_22 = canvas.create_image(
            191.0,
            355.0,
            image=image_image_22
        )

        canvas.create_text(
            75.0,
            268.0,
            anchor="nw",
            text="Enter amount to deposit",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        button_image_12 = PhotoImage(
            file=relative_to_assets2("button_12.png"))
        button_12 = Button(
            nwindow,
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:(nwindow.withdraw(),update_balance_label()),
            relief="flat"
        )
        button_12.place(
            x=146.0,
            y=424.0,
            width=155.0,
            height=44.0
        )

        image_image_32 = PhotoImage(
            file=relative_to_assets2("image_32.png"))
        image_32 = canvas.create_image(
            222.0,
            223.0,
            image=image_image_32
        )

        image_image_42 = PhotoImage(
            file=relative_to_assets2("image_42.png"))
        image_42 = canvas.create_image(
            213.0,
            151.0,
            image=image_image_42
        )

        image_image_52 = PhotoImage(
            file=relative_to_assets2("image_52.png"))
        image_52 = canvas.create_image(
            50.0,
            47.0,
            image=image_image_52
        )


        balance_label=canvas.create_text(
            88.0,
            201.0,
            anchor="nw",
            text=str(bal),
            fill="#000000",
            font=("Inter", 26 * -1)
        )

        entry_image_12 = PhotoImage(
            file=relative_to_assets2("entry_12.png"))
        entry_bg_12 = canvas.create_image(
            194.0,
            355.5,
            image=entry_image_12
        )
        entry_12 = Entry(
            nwindow,
            bd=0,
            bg="#AEC0FF",
            highlightthickness=0
        )
        entry_12.place(
            x=85.0,
            y=335.0,
            width=218.0,
            height=39.0
        )
        button_image_22 = PhotoImage(
            file=relative_to_assets2("button_22.png"))
        button_22 = Button(
            nwindow,
            image=button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:depbalance_update(entry_12.get()),
            relief="flat"
        )
        button_22.place(
            x=346.0,
            y=331.0,
            width=49.0,
            height=49.0
        )
        nwindow.resizable(False, False)
        nwindow.mainloop()

    def withdraw():
        global bal
        OUTPUT_PATH3 = Path(__file__).parent
        ASSETS_PATH3 = OUTPUT_PATH3 / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build3\assets\frame0")

        def relative_to_assets3(path: str) -> Path:
            return ASSETS_PATH3 / Path(path)

        newindow = Toplevel(window)
        newindow.title("Withdraw")
        newindow.geometry("450x500")
        newindow.configure(bg = "#1F43A0")
        def depbalance_update(entry_value):
            global bal
            try:
                # Convert the string to a float
                amount_to_withdraw = float(entry_value)
                try:
                    if(bal>amount_to_withdraw):
                        insert_query = "INSERT INTO transaction_"+str(account)+ " (credited, debited) VALUES (%s, %s)"
                        data = (0, amount_to_withdraw)
                        cur.execute(insert_query, data)
                        bal=bal-amount_to_withdraw
                        q = f"UPDATE transaction SET balance = {bal} WHERE accno = '{account}'"
                        cur.execute(q)
                        con.commit()
                        canvas.itemconfig(tagOrId=balance_label,text=bal)
                except ValueError:
                    messagebox.showinfo("Insufficient funds","Not enough balance.")
            except ValueError:
                    messagebox.showinfo("Invalid input","Please enter a valid number.")
                #amount_to_deposit = float(entry_value)
        canvas = Canvas(
            newindow,
            bg = "#1F43A0",
            height = 500,
            width = 450,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_13 = PhotoImage(
            file=relative_to_assets3("image_13.png"))
        image_13 = canvas.create_image(
            225.0,
            45.0,
            image=image_image_13
        )

        canvas.create_text(
            94.0,
            19.0,
            anchor="nw",
            text="Withdraw",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        image_image_23 = PhotoImage(
            file=relative_to_assets3("image_23.png"))
        image_23 = canvas.create_image(
            191.0,
            355.0,
            image=image_image_23
        )

        entry_image_13 = PhotoImage(
            file=relative_to_assets3("entry_13.png"))
        entry_bg_13 = canvas.create_image(
            194.0,
            355.5,
            image=entry_image_13
        )
        entry_13 = Entry(
            newindow,
            bd=0,
            bg="#AEC0FF",
            highlightthickness=0
        )
        entry_13.place(
            x=85.0,
            y=335.0,
            width=218.0,
            height=39.0
        )

        button_image_13 = PhotoImage(
            file=relative_to_assets3("button_13.png"))
        button_13 = Button(
            newindow,
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:depbalance_update(entry_13.get()),
            relief="flat"
        )
        button_13.place(
            x=346.0,
            y=331.0,
            width=49.0,
            height=49.0
        )

        canvas.create_text(
            63.0,
            259.0,
            anchor="nw",
            text="Enter amount to withdraw :",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        button_image_23 = PhotoImage(
            file=relative_to_assets3("button_23.png"))
        button_23 = Button(
            newindow,
            image=button_image_23,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:(newindow.withdraw(),update_balance_label()),
            relief="flat"
        )
        button_23.place(
            x=148.0,
            y=424.0,
            width=155.0,
            height=44.0
        )

        image_image_33 = PhotoImage(
            file=relative_to_assets3("image_33.png"))
        image_33 = canvas.create_image(
            226.0,
            207.0,
            image=image_image_33
        )

        balance_label=canvas.create_text(
            88.0,
            186.0,
            anchor="nw",
            text=str(bal),
            fill="#000000",
            font=("Inter", 26 * -1)
        )

        image_image_43 = PhotoImage(
            file=relative_to_assets3("image_43.png"))
        image_43 = canvas.create_image(
            50.0,
            48.0,
            image=image_image_43
        )

        image_image_53 = PhotoImage(
            file=relative_to_assets3("image_53.png"))
        image_53 = canvas.create_image(
            212.0,
            142.0,
            image=image_image_53
        )
        newindow.resizable(False, False)
        newindow.mainloop()

    def transhis():
        OUTPUT_PATH4 = Path(__file__).parent
        ASSETS_PATH4 = OUTPUT_PATH4 / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build4\assets\frame0")

        table_columns = ["Transaction_id", "Credited", "Debited","TimeStamp"]
        table_data = fetchtransac()
        newwindow = Toplevel(window)
        newwindow.geometry("900x650")
        newwindow.configure(bg = "#1F43A0")
               
        def relative_to_assets4(path: str) -> Path:
            return ASSETS_PATH4 / Path(path)
        
        canvas = Canvas(
            newwindow,
            bg = "#1F43A0",
            height = 650,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        table= ttk.Treeview(master=newwindow,columns=table_columns,show="headings")
        for column in table_columns:
            table.heading(column= column,text=column,anchor='center')
            table.column(column=column,width=70,anchor='center')
        for row_data in table_data:
            table.insert(parent="",index="end",values=row_data)
        table.pack()
        style= ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="#AEC0FF")
        table.place(x=100.0,y=220.0, height=300, width=700) 

        canvas.place(x = 0, y = 0)

        image_image_14 = PhotoImage(
            file=relative_to_assets4("image_14.png"))
        image_14 = canvas.create_image(
            500.0,
            45.0,
            image=image_image_14
        )
        canvas.create_text(
            94.0,
            16.0,
            anchor="nw",
            text="Transactions History",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        button_image_14 = PhotoImage(
            file=relative_to_assets4("button_14.png"))
        button_14 = Button(
            newwindow,
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=newwindow.withdraw,
            relief="flat"
        )
        button_14.place(
            x=372.0,
            y=569.0,
            width=155.0,
            height=44.0
        )

        '''image_image_24 = PhotoImage(
            file=relative_to_assets4("image_24.png"))
        image_24 = canvas.create_image(
            450.0,
            370.0,
            image=image_image_24
        )'''

        image_image_34 = PhotoImage(
            file=relative_to_assets4("image_34.png"))
        image_34 = canvas.create_image(
            43.0,
            43.0,
            image=image_image_34
        )

        canvas.create_text(
            76.0,
            121.0,
            anchor="nw",
            text="Last 5 transactions :",
            fill="#FFFFFF",
            font=("Inter Bold", 30 * -1)
        ) 

        newwindow.resizable(False, False)
        newwindow.mainloop()

    def transferacc():
        global bal
        global destination_account
        OUTPUT_PATH5 = Path(__file__).parent
        ASSETS_PATH5 = OUTPUT_PATH5 / Path(r"C:\Users\alana\OneDrive\Desktop\dbms proj\Transactions\build5\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH5 / Path(path)

        newwwindow = Toplevel(window)
        newwwindow.title("Transfer")
        newwwindow.geometry("800x600")
        newwwindow.configure(bg = "#1F43A0")
        def desaccno(entry_value):
            global destination_account
            destination_account=entry_value
        def depbalance_update(entry_value):
            global bal
            global destination_account

            try:
                # Convert the string to a float
                amount_to_transfer = float(entry_value)
                cur.execute(f"SELECT 1 FROM transaction WHERE accno = '{destination_account}' LIMIT 1")
                destination_account_exists = cur.fetchone()
                if destination_account_exists:
                    try:
                        if(bal>amount_to_transfer and amount_to_transfer>0):
                            insert_query = "INSERT INTO transaction_"+str(account)+ " (credited, debited) VALUES (%s, %s)"
                            data = (0,amount_to_transfer)
                            cur.execute(insert_query, data)
                            insert_query2 = "INSERT INTO transaction_"+str(destination_account)+ " (credited, debited) VALUES (%s, %s)"
                            data = (amount_to_transfer,0)
                            cur.execute(insert_query2, data)
                            bal=bal-amount_to_transfer
                            q = f"UPDATE transaction SET balance = {bal} WHERE accno = '{account}'"
                            cur.execute(q)
                            con.commit()
                            canvas.itemconfig(tagOrId=balance_label,text=bal)
                            cur.execute(f"SELECT balance FROM transaction WHERE accno = '{destination_account}'")
                            destination_balance_row = cur.fetchone()
                            if destination_balance_row is not None:
                                destination_balance = float(destination_balance_row[0])
                                #destination_balance = float(cur.fetchone()[0])
                                destination_balance += amount_to_transfer
                                q2 = f"UPDATE transaction SET balance = {destination_balance} WHERE accno = '{destination_account}'"
                                
                                cur.execute(q2)
                                con.commit()
                            else:
                                # Handle the case where the destination account does not exist
                                messagebox.showinfo("Error", "Destination account not found.")
                    except ValueError:
                        messagebox.showinfo("Insufficient funds","Not enough balance.")
                else:
                    messagebox.showinfo("ERROR","Please Enter account number")
            except ValueError:
                messagebox.showinfo("Invalid input","Please enter a valid number.")
                    #amount_to_deposit = float(entry_value)
        canvas = Canvas(
            newwwindow,
            bg = "#1F43A0",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_15 = PhotoImage(
            file=relative_to_assets("image_15.png"))
        image_15 = canvas.create_image(
            515.0,
            45.0,
            image=image_image_15
        )

        canvas.create_text(
            94.0,
            25.0,
            anchor="nw",
            text="Transfer to Another Account",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        image_image_25 = PhotoImage(
            file=relative_to_assets("image_25.png"))
        image_25 = canvas.create_image(
            520.0,
            447.0,
            image=image_image_25
        )

        image_image_35 = PhotoImage(
            file=relative_to_assets("image_35.png"))
        image_35 = canvas.create_image(
            543.0,
            314.0,
            image=image_image_35
        )

        entry_image_15 = PhotoImage(
            file=relative_to_assets("entry_15.png"))
        entry_bg_15 = canvas.create_image(
            542.0,
            316.0,
            image=entry_image_15
        )
        entry_15= Entry(
            newwwindow,
            bd=0,
            bg="#AEC0FF",
            highlightthickness=0
        )
        entry_15.place(
            x=423.0,
            y=297.0,
            width=238.0,
            height=36.0
        )

        balance_label=canvas.create_text(
            393.0,
            428.0,
            anchor="nw",
            text=str(bal),
            fill="#000000",
            font=("Inter", 22 * -1)
        )

        image_image_45 = PhotoImage(
            file=relative_to_assets("image_45.png"))
        image_45 = canvas.create_image(
            545.0,
            180.0,
            image=image_image_45
        )

        image_image_55 = PhotoImage(
            file=relative_to_assets("image_55.png"))
        image_55 = canvas.create_image(
            244.0,
            448.0,
            image=image_image_55
        )

        button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
        button_15 = Button(
            newwwindow,
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:(newwwindow.withdraw(),update_balance_label()),
            relief="flat"
        )
        button_15.place(
            x=325.0,
            y=526.0,
            width=155.0,
            height=44.0
        )

        canvas.create_text(
            46.0,
            284.0,
            anchor="nw",
            text="Enter amount to Transfer :",
            fill="#FFFFFF",
            font=("Inter Bold", 26 * -1)
        )

        canvas.create_text(
            46.0,
            156.0,
            anchor="nw",
            text="Enter Account Number to\nTransfer to :",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        image_image_65 = PhotoImage(
            file=relative_to_assets("image_65.png"))
        image_65 = canvas.create_image(
            50.0,
            45.0,
            image=image_image_65
        )
        
        entry_image_25 = PhotoImage(
            file=relative_to_assets("entry_25.png"))
        entry_bg_25 = canvas.create_image(
            543.0,
            181.0,
            image=entry_image_25
        )
        entry_25 = Entry(
            newwwindow,
            bd=0,
            bg="#AEC0FF",
            highlightthickness=0
        )
        entry_25.place(
            x=424.0,
            y=162.0,
            width=238.0,
            height=36.0
        )

        button_image_35 = PhotoImage(
            file=relative_to_assets("button_35.png"))
        button_35 = Button(
            newwwindow,
            image=button_image_35,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:desaccno(entry_25.get()) ,
            relief="flat"
        )

        button_35.place(
            x=716.0,
            y=150.0,
            width=60.0,
            height=60.0
        )

        button_image_25 = PhotoImage(
            file=relative_to_assets("button_25.png"))
        button_25 = Button(
            newwwindow,
            image=button_image_25,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:depbalance_update(entry_15.get()),
            relief="flat"
        )
        
        button_25.place(
            x=716.0,
            y=284.0,
            width=60.0,
            height=60.0
        )

        newwwindow.resizable(False, False)
        newwwindow.mainloop()

    window1 = Toplevel(window)
    window1.title("Transaction")
    window1.geometry("900x600")
    window1.configure(bg = "#1F43A0")
    
    canvas = Canvas(
    window1,
    bg = "#1F43A0",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
    400.0,
    45.0,
    image=image_image_1
    )

    canvas.create_text(
    94.0,
    16.0,
    anchor="nw",
    text="Transactions",
    fill="#000000",
    font=("Inter Bold", 40 * -1)
    )

    image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
    46.0,
    46.0,
    image=image_image_2
    )

    image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
    361.0,
    456.0,
    image=image_image_3
    )

    image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
    113.0,
    456.0,
    image=image_image_4
    )
    
    button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_1 = Button(
    window1,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=deposit,
    relief="flat"
    )
    button_1.place(
    x=583.0,
    y=131.0,
    width=270.0,
    height=70.0
    )

    canvas.create_rectangle(
    44.0,
    140.0,
    464.0,
    372.0,
    fill="#AEBFFF",
    outline="")

    button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_2 = Button(
    window1,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=window1.withdraw,
    relief="flat"
    )
    button_2.place(
    x=395.0,
    y=527.0,
    width=155.0,
    height=44.0
    )

    button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
    button_3 = Button(
    window1,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=withdraw,
    relief="flat"
    )
    button_3.place(
    x=583.0,
    y=231.0,
    width=270.0,
    height=70.0
    )

    button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
    button_4 = Button(
    window1,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=transhis,
    relief="flat"
    )
    button_4.place(
    x=583.0,
    y=333.0,
    width=270.0,
    height=70.0
    )

    button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
    button_5 = Button(
    window1,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=transferacc,
    relief="flat"
    )
    button_5.place(
    x=583.0,
    y=435.0,
    width=270.0,
    height=70.0
    )
    cur.execute("select * from customer")
    rows=cur.fetchall()
    for row in rows:
        if row[5]==password:
            a=row[0]
            b=row[3]
            c=row[4]
    canvas.create_text(
    60.0,
    150.0,
    anchor="nw",
    text="Account No. : "+str(account)+"\n\nName : "+str(a)+"\n\nPhone No. : "+str(c)+"\n\nEmail : "+str(b),
    fill="#000000",
    font=("Inter Bold", 26 * -1)
    )

    balance_labelm=canvas.create_text(
    235.0,
    435.0,
    anchor="nw",
    text=str(bal),
    fill="#000000",
    font=("Inter Bold", 26 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
        
def menupg():
    conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
    cursor=conn.cursor()
    newindow2=Toplevel(window)
    newindow2.geometry("1500x650")
    newindow2.title("Menu Page")
    ctk.set_appearance_mode("light")
    newindow2.config(bg='blue4')
    ctk.set_default_color_theme("blue")
    frame3=ctk.CTkFrame(master=newindow2,width=600,height=600,corner_radius=15,fg_color='ivory2')
    frame3.pack(pady=50,padx=150,fill="both",expand=True)
    label7=ctk.CTkLabel(master=frame3,text="MENU",font=("TkHeading",26),text_color='black')
    label7.pack(pady=20,padx=40)
    def back():
        newindow2.withdraw()
    '''userimg=Image.open("./images/user1.png")
    resized=userimg.resize((200,200),Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(resized)
    labeluser=tk.Label(frame3,image=tk_image)
    labeluser.image=tk_image
    labeluser.place(x=20,y=30)'''
    cursor.execute("select * from customer")
    rows=cursor.fetchall()
    for row in rows:
        if row[5]==password:
            labelname=ctk.CTkLabel(master=frame3,text="Name:"+row[0],font=("Arial",18),text_color='black')
            labelname.place(y=300,x=40)
            labelage=ctk.CTkLabel(master=frame3,text="Age:"+str(row[4]),font=("Arial",18),text_color='black')
            labelage.place(y=320,x=40)
            labelemail=ctk.CTkLabel(master=frame3,text="Email:"+row[2],font=("Arial",18),text_color='black')
            labelemail.place(y=340,x=40)
            label8=ctk.CTkLabel(master=frame3,text="Account number:"+account,font=("Arial",18),text_color='black')
            label8.place(y=370,x=40)
        
    button8=ctk.CTkButton(master=frame3,text="Transactions",command=transaction,height=100,width=300)
    button8.place(y=100,x=600)
    button9=ctk.CTkButton(master=frame3,text="Loan ",command=status,height=100,width=100)
    button9.place(y=250,x=600)
    button10=ctk.CTkButton(master=frame3,text="Request Account Deletion",command=delete,height=100)
    button10.place(y=250,x=730)
    buttonexit=ctk.CTkButton(master=frame3,text="Exit",command=back,height=50,width=100)
    buttonexit.place(y=450,x=650)
    button11=ctk.CTkButton(master=frame3,text="Customer Support",command=support,height=50,width=100)
    button11.place(y=450,x=800)

def clogin():
    global account,password
    createtable()
    account=entry1.get()
    password=entry2.get()
    
    if not(account and password):
        messagebox.showinfo('Error','Enter all fields')
    elif (not(accountexist())):
        messagebox.showinfo('Error','Account or Password incorrect')
    else:
        entry1.delete(0,'end')
        entry2.delete(0,'end')
        menupg()
def csign():
    global entry3,entry4,entry5,entry6,entry7,entry8,newindow1
    newindow1=Toplevel(window)
    newindow1.geometry("925x925")
    newindow1.title("cutomer signin")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    def show():
        if entry8.cget('show')=='*':
            entry8.configure(show='')

        else:
            entry8.configure(show='*')
    def back():
        newindow1.withdraw()
    frame2=ctk.CTkScrollableFrame(master=newindow1,width=470,height=510,corner_radius=15,fg_color='lemon chiffon')
    frame2.pack(pady=0,padx=0,fill="both",expand=True)
    label6=ctk.CTkLabel(master=frame2,text="Customer Registeration",font=("Helvetica",26),text_color='black')
    label6.pack(pady=20,padx=10)
    entry3=ctk.CTkEntry(master=frame2,width=300,placeholder_text="FullName")
    entry3.pack(pady=20,padx=15)
    entry4=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Address")
    entry4.pack(pady=20,padx=15)
    entry5=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Email")
    entry5.pack(pady=20,padx=15)
    entry6=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Mobilenumber")
    entry6.pack(pady=20,padx=15)
    entry7=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Age")
    entry7.pack(pady=20,padx=15)
    label6=ctk.CTkLabel(master=frame2,text="Create Password:",font=("Helvetica",16),text_color='black')
    label6.pack(pady=20,padx=10)
    entry8=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Password",show='*')
    entry8.pack(pady=20,padx=15)
    button7=ctk.CTkCheckBox(master=frame2,text="Show/Hide",command=show)
    button7.pack(pady=20,padx=15)
    button6=ctk.CTkButton(master=frame2,text="Register",command=register)
    button6.pack(pady=20,padx=15)
    buttonback=ctk.CTkButton(master=frame2,text="Back",command=back)
    buttonback.pack(pady=20,padx=15)

    '''
    img2=ImageTk.PhotoImage(Image.open("./images/cust1.png"))
    label5=Label(image=img2)
    label5=ctk.CTkLabel(newindow1,image=img2,text="")
    label5.image=img2
    label5.place(x=0.5,y=0.5)
    '''
def adminlogin():
    print("Test")
def customerlogin():
    global entry1,entry2
    newindow=Toplevel(window)
    newindow.geometry("700x700")
    newindow.title("Cutomer Loginpage")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    def back():
        newindow.withdraw()
    def show():
        if entry2.cget('show')=='*':
            entry2.configure(show='')

        else:
            entry2.configure(show='*')
    frame1=ctk.CTkFrame(master=newindow,width=600,height=600,corner_radius=15,fg_color='light goldenrod')
    frame1.pack(pady=0,padx=0,fill="both",expand=True)
    '''img1=ImageTk.PhotoImage(Image.open("./images/adminLogin1.png"))
    label4=tk.Label(newindow,image=img1)
    label4.image=img1
    label4.pack(pady=0,padx=0)'''
    label3=ctk.CTkLabel(master=frame1,text="Customer Login",font=("TkHeading",26),text_color='black')
    label3.pack(pady=45,padx=50)
    entry1=ctk.CTkEntry(master=frame1,width=220,placeholder_text="AccountNumber")
    entry1.pack(pady=20,padx=40)
    entry2=ctk.CTkEntry(master=frame1,width=220,placeholder_text="Password",show='*')
    entry2.pack(pady=20,padx=40)
    button14=ctk.CTkCheckBox(master=frame1,text="Show/Hide",command=show)
    button14.pack(pady=20,padx=15)
    def close():
        newindow.withdraw()
    button3=ctk.CTkButton(master=frame1,text="Login",command=clogin)
    button3.pack(pady=20,padx=40)
    button4=ctk.CTkButton(master=frame1,text="Signup",command=csign)
    button4.pack(pady=20,padx=40)
    buttonback1=ctk.CTkButton(master=frame1,text="Back",command=back)
    buttonback1.pack(pady=20,padx=15)
    
welcome()
window.mainloop()
