import sqlite3
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# เชื่อมต่อกับฐานข้อมูล SQLite3
conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
cursor = conn.cursor()
#สร้างตารางเมนูทั้งหมด
cursor.execute(''' CREATE TABLE IF NOT EXISTS ListMenu ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        id_Menu TEXT,
        Name_Menu TEXT,
        price_Menu INTEGER)''')
#สร้างตารางเก็ยข้อมูลลูกค้า
cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurant ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        DAY TEXT,
        TIME TEXT,
        Customer_name TEXT,
        Menuname TEXT,
        Number INTEGER,
        Summary_price INTEGER,
        Address TEXT,
        Tel TEXT)''')
#สร้างตารางใบเสร็จ
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bill ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        id_Menu TEXT,
        Menuname TEXT,
        Number INTEGER,
        price_Menu INTEGER)''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Summary ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        DAY TEXT,
        TIME TEXT,
        Customer_name TEXT,
        Menuname TEXT,
        Number INTEGER,
        price_Menu INTEGER,
        Address TEXT,
        Tel TEXT)''')
conn.commit()


from tkinter import * #สร้างหน้าต่าง
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox,Style
from datetime import datetime

root= Tk()
root.title("ร้านมะอู๊ด เดลิเวอร์รี่")
root.geometry("1285x760+125+15")

image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\2.png")
photo = ImageTk.PhotoImage(image)

# สร้าง Label และเซ็ตรูปภาพเป็นพื้นหลัง
Label(root, image=photo).place(relwidth=1, relheight=1)

def closecustomer():
    global customer
    customer.destroy()

def Customer():
    global customer
    customer=Toplevel()
    customer.title("ลูกค้า")
    customer.geometry("1285x760+125+15")

    image = Image.open( r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\4.png")
    photo = ImageTk.PhotoImage(image)
    
    def closemenu():
        global menu
        menu.destroy()

    def change_background(event):
        selected_item = MenuVar.get()
        if selected_item == "ผัดกะเพรา":
        # เปลี่ยนภาพพื้นหลังเมื่อเลือก "ผัดกะเพรา"
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\15.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ผัดพริกแกง":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\16.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ผัดขี้เมา":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\17.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ผัดผงกะหรี่":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\18.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ผัดผัก":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\19.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ผัดพริกเผา":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\20.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ผัดซีอิ๊ว":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\21.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ราดหน้า":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\22.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "คั่วพริกเกลือ":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\23.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ข้าวผัด":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\24.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ต้ม / แกง":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\25.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "ยำ":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\26.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        if selected_item == "เมนูบวกเพิ่ม":
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\36.png")
            new_photo = ImageTk.PhotoImage(image)
            background_label.configure(image=new_photo)
            background_label.image = new_photo
        

    def Menu():
        global menu,MenuVar,combo,background_label
        menu=Toplevel()
        menu.title("เมนู")
        menu.geometry("1285x760+125+15")
        MenuVar = StringVar()

        image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\13.png")
        photo = ImageTk.PhotoImage(image)
        background_label = Label(menu, image=photo)
        background_label.place(relwidth=1, relheight=1)        
        Button(menu,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closemenu).place(x=95,y=668)
        listmenu = ["ผัดกะเพรา", "ผัดพริกแกง", "ผัดขี้เมา","ผัดผงกะหรี่","ผัดผัก", "ผัดพริกเผา", "ผัดซีอิ๊ว","ราดหน้า","คั่วพริกเกลือ", "ข้าวผัด", "ต้ม / แกง","ยำ","เมนูบวกเพิ่ม"]
        global combo
        combo=Combobox(menu,font=("FC Muffin",30,"bold"),width=20, values=listmenu, state="readonly", textvariable=MenuVar)
        combo.place(x=450,y=115)
        style = Style()
        style.configure("TCombobox.field", font=("FC Muffin", 30))
        root.option_add("*Font","consolas 35")
        combo.bind("<<ComboboxSelected>>", change_background)

        menu.mainloop()

    def closeorder():
        global order
        order.destroy()
    def Order():
        global order
        order=Toplevel()
        order.title("สั่งอาหาร")
        order.geometry("1285x760+125+15")
        image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\6.png")
        photo = ImageTk.PhotoImage(image)
        Label(order, image=photo).place(relwidth=1, relheight=1)
        order.option_add("*Font", "consolas 28")

        input_menuString = StringVar()
        input_numVar = IntVar ()
        input_menu = tk.Entry(order,textvariable = input_menuString, borderwidth=0, relief="flat",width=15,bg="#1F798A",justify="center")
        input_menu.place(x=138,y=265)
        input_num = tk.Entry(order, textvariable= input_numVar, borderwidth=0, relief="flat",width=8,bg="#1F798A",justify="center")
        input_num.place(x=195,y=350)

        #input_menuGet = input_menuString.get()
        # input_numGet = input_numVar.get()
        
        def Add():
            global existing_price,existing_number
            input_menuGet = input_menuString.get()
            input_numGet = input_numVar.get()
            
            if input_menuGet and input_numGet:
                # ค้นหาข้อมูลจากรายการอาหาร foodLists
                conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
                cursor = conn.cursor()
                cursor.execute('''SELECT * FROM ListMenu WHERE id_Menu = ?''', (input_menuGet,))
                food_data = cursor.fetchone()
                
                if food_data:
                    id, id_Menu, Name_Menu, price_Menu = food_data
                    foodName = Name_Menu
                    priceAll = int(price_Menu)
                    
                    # ค้นหาข้อมูลใน BillTable ว่ารายการที่สั่งอยู่แล้วหรือไม่
                    cursor.execute('''SELECT id, Number, price_Menu FROM Bill WHERE id_Menu = ?''', (input_menuGet,))
                    existing_item = cursor.fetchone()

                    if existing_item:
                        # หากรายการมีอยู่แล้วให้บวกค่า Number และอัปเดตราคาใน BillTable
                        id, existing_number, existing_price = existing_item
                        new_number = existing_number + input_numGet
                        new_price = new_number * (existing_price / existing_number)
                        cursor.execute('''UPDATE Bill SET Number = ?, price_Menu = ? WHERE id = ?''', (new_number, new_price, id,))
                        conn.commit()
                    else:
                        # หากรายการยังไม่มีอยู่ใน BillTable ให้เพิ่มรายการใหม่
                        priceSum = priceAll * input_numGet
                        data = (input_menuGet, foodName, input_numGet, priceSum)
                        cursor.execute('INSERT INTO Bill (id_Menu, Menuname, Number, price_Menu) VALUES (?, ?, ?, ?)', data)
                        conn.commit()
                        
                    # ลบรายการทั้งหมดใน Listbox และแสดงรายการใหม่
                    listbox.delete(0, tk.END)
                    cursor.execute("SELECT id_Menu, Menuname, Number, price_Menu FROM Bill")
                    data = cursor.fetchall()
                    for row in data:
                        listbox.insert(tk.END, row)
                conn.close()
        def Delete2():
            global existing_price ,existing_number
            input_menuGet = input_menuString.get()
            input_numGet = input_numVar.get()

            if input_menuGet and input_numGet:
                # เชื่อมต่อกับฐานข้อมูล SQLite
                conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
                cursor = conn.cursor()

                # ค้นหารายการที่ต้องการลบโดยใช้รหัสรายการ
                cursor.execute('''SELECT id, Number FROM Bill WHERE id_Menu = ?''', (input_menuGet,))
                item_to_delete = cursor.fetchone()

                if item_to_delete:
                    id_to_delete, num_to_delete = item_to_delete

                    if num_to_delete > input_numGet:
                        # ถ้าจำนวนที่ต้องการลบมากกว่าจำนวนที่มีอยู่
                        new_number = num_to_delete - input_numGet
                        new_price = new_number * (existing_price / existing_number)

                        # อัปเดตจำนวนและราคาใน BillTable
                        cursor.execute('''UPDATE Bill SET Number = ?, price_Menu = ? WHERE id = ?''', (new_number, new_price, id_to_delete))
                    else:
                        # ถ้าจำนวนที่ต้องการลบมากกว่าหรือเท่ากับจำนวนที่มีอยู่
                        # ให้ลบรายการนี้ออกจาก BillTable
                        cursor.execute('''DELETE FROM Bill WHERE id = ?''', (id_to_delete,))

                    # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
                    conn.commit()

                    # ลบรายการที่ถูกลบออกจาก Listbox และแสดงรายการที่เหลืออยู่
                    listbox.delete(0, tk.END)
                    cursor.execute("SELECT id_Menu, Menuname, Number, price_Menu FROM Bill")
                    data = cursor.fetchall()
                    for row in data:
                        listbox.insert(tk.END, row)

                # ปิดการเชื่อมต่อกับฐานข้อมูล SQLite
                conn.close()



            #สร้างเฟรมให้listboxอยู่
        frame = tk.Frame(order)
        frame.place(x=550,y=150)
        #สร้างlistboxในเฟรม
        listbox = tk.Listbox(frame, width=33, height=12)
        listbox.configure(bg="White")
        listbox.pack()

        def PDF():
            conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")  
            cursor = conn.cursor()
            cursor.execute("SELECT Menuname,Number,price_Menu FROM Bill")        
            data = cursor.fetchone()
            pdfmetrics.registerFont(TTFont('Th', r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\cordia.ttc"))
            current_datetime =datetime.now()
            pdf_file_name = f'receipt_{current_datetime.strftime("%Y%m%d_%H%M%S")}.pdf'  
            doc = SimpleDocTemplate(pdf_file_name, pagesize=letter)
            elements = []
            styles = getSampleStyleSheet()
            normal_style_head = styles['Normal']
            normal_style_head.fontName = 'Th'  
            normal_style_head.fontSize = 20

            styles = getSampleStyleSheet()
            normal_style1 = styles['Normal']
            normal_style1.fontName = 'Th'  
            normal_style1.fontSize = 30

            styles = getSampleStyleSheet()
            normal_style2 = styles['Normal']
            normal_style2.fontName = 'Th'  
            normal_style2.fontSize = 25

                                        #สร้างคำในใบเสร็จ
            head = Paragraph("ใบเสร็จ", normal_style1)
            head1 = Paragraph("ร้านมะอู๊ดเดริเวอร์รี่", normal_style1)
            head2 = Paragraph("104บ้านนัทธมน 779 ม.12 ต.ศิลา อ.เมือง จ.ขอนแก่น 40000", normal_style_head)
            head21=Paragraph("โทร.087-3744983 / 098-8373521",normal_style_head)
            datepdf = Paragraph("วันที่ : %s"%day, normal_style_head)
            Time = Paragraph("เวลา : %s"%time, normal_style_head)
            Name = Paragraph("ชื่อ :  {}     เบอร์ : {}".format(name, tel), normal_style_head)
            desun1 = Paragraph("ที่อยู่จัดส่ง :  %s "%address_input,normal_style_head)
            line = Paragraph("--------------------------------------------------------", normal_style_head)
            sum = Paragraph("Total : %d บาท"%price, normal_style1)

            spacer = Spacer(1, 10)  
            spacer1 = Spacer(1, 50)
            spacer2 = Spacer(1, 20)


            elements.append(head)
            elements.append(spacer)
            elements.append(head1)
            elements.append(spacer1)
            elements.append(head2)
            elements.append(spacer)
            elements.append(head21)
            elements.append(spacer1)
            elements.append(datepdf)
            elements.append(spacer)
            elements.append(Time)
            elements.append(spacer)
            elements.append(Name)
            elements.append(spacer)
            elements.append(desun1)
            elements.append(spacer)
            elements.append(line)
            elements.append(spacer2)
            elements.append(sum)



            doc.build(elements)

                                        #เปิดสลิปpdf
            subprocess.Popen(pdf_file_name, shell=True)

        def closeaddress():
            global address
            address.destroy()
        def Address():
            global address,day,time,price
            address=Toplevel()
            address.title("กรุณากรอก")
            address.geometry("1285x760+125+15")
            image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\8.png")
            photo = ImageTk.PhotoImage(image)
            Label(address, image=photo).place(relwidth=1, relheight=1)
            address.option_add("*Font", "consolas 28")
            now=datetime.now()
            day = now.strftime("%Y-%m-%d")
            time=now.strftime("%H:%M")
            input_nameString = StringVar()
            input_addressString=StringVar()
            input_telString=StringVar()
            input_name = tk.Entry(address,textvariable = input_nameString, borderwidth=0, relief="flat",width=15,bg="white")
            input_name.place(x=140,y=190)
            input_tel = tk.Entry(address,textvariable = input_telString,borderwidth=0, relief="flat",width=12,bg="white")
            input_tel.place(x=195,y=265)
            input_address = tk.Entry(address, textvariable= input_addressString, borderwidth=0, relief="flat",width=12,bg="white")
            input_address.place(x=180,y=345)
            
            conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Bill")        
            data = cursor.fetchall()
                #สร้างเฟรมให้listboxอยู่
            frame = tk.Frame(address)
            frame.place(x=550,y=150)
            #สร้างlistboxในเฟรม
            listbox = tk.Listbox(frame, width=33, height=10)
            listbox.configure(bg="White")
            listbox.pack()
            for row in data:
                listbox.insert(tk.END, row)  # เพิ่มข้อมูลลงใน Listbox
            cursor.execute('SELECT Menuname,Number,price_Menu FROM Bill')
            Allmenu=[row[0] for row in cursor.fetchall()]
            cursor.execute('SELECT Number FROM Bill')
            Allnum = sum(int(row[0]) for row in cursor.fetchall())
            cursor.execute('SELECT price_Menu FROM Bill')
            price = sum(int(row[0]) for row in cursor.fetchall())
            Allmenu_str=','.join(Allmenu)
            def check1():
                tel=input_tel.get()
                if len(tel) == 10 and tel.isdigit():
                    confirm()
                else:
                    messagebox.showerror("ข้อมูลไม่ถูกต้อง", "กรุณากรอกเบอร์โทรศัพท์ 10 ตัวเลขเท่านั้น")
                    address.deiconify()
            def confirm(): 
                global name,tel,address_input
                name=input_name.get()
                tel=input_tel.get()
                address_input=input_address.get()
                cursor.execute('''INSERT INTO restaurant (DAY, TIME, Customer_name, Menuname, Number, Summary_price,Address,Tel)VALUES (?, ?, ?, ?, ?, ?,?,?)''', (day, time, name, Allmenu_str,Allnum,price,address_input,tel ))
                cursor.execute('''INSERT INTO Summary (DAY, TIME, Customer_name, Menuname, Number, price_Menu,Address,Tel)VALUES (?, ?, ?, ?, ?, ?,?,?)''', (day, time, name, Allmenu_str,Allnum,price,address_input,tel ))
                conn.commit()
                input_menu.delete(0,END)
                input_num.delete(0,END)
                PDF()
                cursor.execute('DROP TABLE Bill ')
                cursor.execute(''' CREATE TABLE IF NOT EXISTS Bill (id INTEGER PRIMARY KEY AUTOINCREMENT, id_Menu TEXT,Menuname TEXT,Number INTEGER,price_Menu INTEGER)''')
                conn.commit()
                address.destroy()
                order.destroy()
            Label(address,text="รวมเป็นเงิน  " +str(price) +" บาท",font=("FC Muffin",45,"bold"),bg='#CB5B3B',fg='#FFFFB0').place(x=750,y=620)
            Button(address,text="ยืนยัน",font=("FC Muffin",20,"bold"),borderwidth = 0,width=7,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=check1).place(x=215,y=529)
            Button(address,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closeaddress).place(x=95,y=668)
            address.mainloop()
            
        Button(order,text="เมนู",font=("FC Muffin",25,"bold"),borderwidth = 0,width=8,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Menu).place(x=80,y=100)
        Button(order,text="เพิ่ม",font=("FC Muffin",22,"bold"),borderwidth = 0,width=8,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Add).place(x=110,y=430)
        Button(order,text="ลบ",font=("FC Muffin",22,"bold"),borderwidth = 0,width=8,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Delete2).place(x=310,y=430)
        Button(order,text="ยืนยัน",font=("FC Muffin",22,"bold"),borderwidth = 0,width=7,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Address).place(x=215,y=525)
        Button(order,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closeorder).place(x=95,y=668)

        order.mainloop()
    def closedoQ():
        global doQ
        doQ.destroy()
    def DoQ():
        global doQ
        doQ=Toplevel()
        doQ.title("ดูลำดับคิวการสั่ง")
        doQ.geometry("1285x760+125+15")
        doQ.option_add("*Font", "consolas 20")

        image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\10.png")
        photo = ImageTk.PhotoImage(image)
        Label(doQ, image=photo).place(relwidth=1, relheight=1)

        def Showsql_info():
            conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id,DAY, TIME, Customer_name,Summary_price,Address,Tel FROM restaurant")
            data = cursor.fetchall()
            for row in data:
                listbox.insert(tk.END, row)  # เพิ่มข้อมูลลงใน Listbox
            conn.close()
        #สร้างเฟรมให้listboxอยู่
        frame = tk.Frame(doQ)
        frame.place(x=100,y=140)
        #สร้างlistboxในเฟรม
        listbox = tk.Listbox(frame, width=73, height=14)
        listbox.configure(bg="white")
        listbox.pack()

        Button(doQ,text="แสดงคิว",font=("FC Muffin",23,"bold"),borderwidth = 0,width=10,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Showsql_info).place(x=1040,y=668)
        Button(doQ,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closedoQ).place(x=95,y=668)

        doQ.mainloop()
    def closeedit():
        global edit
        edit.destroy()
    def ooo(arg):
            global entry_name,entry_address,entry_tel,Q_num
            Q_num=num.get()
            if not Q_num:
                return
            conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM restaurant WHERE id=?", (Q_num,))
            data = cursor.fetchone()
            if data:
                    num.delete(0, tk.END)
                    num.insert(0, data[0])
                    entry_name.delete(0, tk.END)
                    entry_name.insert(0, data[3])  # 1 คือ index ของ firstname ในข้อมูล
                    entry_address.delete(0, tk.END)
                    entry_address.insert(0, data[8])  # 2 คือ index ของ lastname ในข้อมูล
                    entry_tel.delete(0, tk.END)
                    entry_tel.insert(0, data[7])
            else:
                    messagebox.showwarning("ไม่มีคิวที่เลือก","ไม่มีคิวที่เลือก กรุณาเลือกคิวใหม่อีกครั้ง")
                    edit.deiconify()
    def Updet():
            global customer_name,residency,phone,Q_num
            customer_name=entry_name.get()
            residency=entry_address.get()
            phone=entry_tel.get()
            conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM restaurant WHERE id=?", (Q_num,))
            existing_data = cursor.fetchone()

            if existing_data:
                # อัปเดตข้อมูล
                cursor.execute("UPDATE restaurant SET Customer_name=?, Address=?, Tel=? WHERE id=?",
                            ( customer_name, residency,phone,Q_num))
                conn.commit()
                edit.destroy()
    def Edit():
        global edit,entry_name,entry_address,entry_tel,Q_num,num
        edit=Toplevel()
        edit.title("แก้ไขชื่อ-เบอร์-ที่อยู่")
        edit.geometry("1285x760+125+15")
        edit.option_add("*Font", "consolas 15")
        image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\12.png")
        photo = ImageTk.PhotoImage(image)
        Label(edit, image=photo).place(relwidth=1, relheight=1)
        num = tk.Entry(edit,font=("FC Muffin",26,),width=17,borderwidth=0, relief="flat",justify="center")
        num.place(x=510,y=225)
        num.configure(background="white",fg="Black")
        num.bind("<KeyRelease>", ooo)
        entry_name = tk.Entry(edit,font=("FC Muffin",26,),width=32,borderwidth=0, relief="flat")
        entry_name.place(x=450,y=325)
        entry_name.configure(bg="white",fg="Black")
        entry_address = tk.Entry(edit,font=("FC Muffin",26,),width=32,borderwidth=0, relief="flat")
        entry_address.place(x=450,y=425)
        entry_address.configure(bg="white",fg="Black")
        entry_tel = tk.Entry(edit,font=("FC Muffin",26,),width=32,borderwidth=0, relief="flat")
        entry_tel.place(x=450,y=525)
        entry_tel.configure(bg="white",fg="Black")

        Button(edit,text="ยืนยัน",font=("FC Muffin",23,"bold"),borderwidth = 0,width=10,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Updet).place(x=575,y=615)
        Button(edit,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closeedit).place(x=95,y=668)        
        edit.mainloop()
    

    # สร้าง Label และเซ็ตรูปภาพเป็นพื้นหลัง
    Label(customer, image=photo).place(relwidth=1, relheight=1)
    Button(customer,text="สั่งอาหาร",font=("FC Muffin",25,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Order).place(x=220,y=110)
    Button(customer,text="ดูลำดับคิวการสั่ง",font=("FC Muffin",25,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=DoQ).place(x=520,y=110)
    Button(customer,text="แก้ไขชื่อ-เบอร์-ที่อยู่",font=("FC Muffin",25,"bold"),borderwidth = 0,width=18,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Edit).place(x=820,y=110)
    Button(customer,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closecustomer).place(x=95,y=668)

    customer.mainloop()
def closepwattendant():
    global pwattendant
    pwattendant.destroy()
def PwAttendant():
    global pwattendant,pw
    pwattendant=Toplevel()
    pwattendant.title("กรุณาใส่รหัส")
    pwattendant.geometry("1285x760+125+15")

    image = Image.open( r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\28.png")
    photo = ImageTk.PhotoImage(image)
    Label(pwattendant, image=photo).place(relwidth=1, relheight=1)
    pwattendant.option_add("*Font", "consolas 33")
    pw = tk.Entry(pwattendant,borderwidth=0, relief="flat")
    pw.place(x=480,y=360)
    Button(pwattendant,text="ยืนยัน",font=("FC Muffin",23,"bold"),borderwidth = 0,width=10,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Confirm).place(x=575,y=615)
    Button(pwattendant,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closepwattendant).place(x=95,y=668)

    pwattendant.mainloop()
def Confirm():
    global pw
    if pw.get()=="Maood69":
        pwattendant.destroy()
        Attendant()
    else:
        p = messagebox.showinfo("แจ้งเตือน","กรอกรหัสร้านไม่ถูกต้อง")
        if p=='ok':
            pwattendant.deiconify()
def closeattendant():
    global attendant
    attendant.destroy()
def Attendant():
    global attendant
    attendant=Toplevel()
    attendant.title("ผู้ดูแลระบบ")
    attendant.geometry("1285x760+125+15")
    image = Image.open( r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\30.png")
    photo = ImageTk.PhotoImage(image)
    Label(attendant, image=photo).place(relwidth=1, relheight=1)
    def closeshow():
        global showfood
        showfood.destroy()
    def Showfood():
        global showfood
        showfood=Toplevel()
        showfood.title("แสดงรายการอาหารที่สั่งแล้ว")
        showfood.geometry("1285x760+125+15")
        image = Image.open( r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\32.png")
        photo = ImageTk.PhotoImage(image)
        Label(showfood, image=photo).place(relwidth=1, relheight=1)
        showfood.option_add("*Font", "consolas 20")
        def Showsql_info():
            conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id,DAY, TIME, Customer_name,Menuname,Summary_price,Address,Tel FROM restaurant")        
            data = cursor.fetchall()
            for row in data:
                listbox.insert(tk.END, row)  # เพิ่มข้อมูลลงใน Listbox
            conn.close()
    #สร้างเฟรมให้listboxอยู่
        frame = tk.Frame(showfood)
        frame.place(x=100,y=140)
        #สร้างlistboxในเฟรม
        listbox = tk.Listbox(frame, width=73, height=14)
        listbox.configure(bg="white")
        listbox.pack()
        Button(showfood,text="แสดงคิว",font=("FC Muffin",23,"bold"),borderwidth = 0,width=10,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Showsql_info).place(x=750,y=673)
        def clear_frame():
            listbox.delete(0,tk.END)
        Button(showfood,text="ล้างคิว",font=("FC Muffin",23,"bold"),borderwidth = 0,width=10,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=clear_frame).place(x=1040,y=673)
        Button(showfood,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closeshow).place(x=95,y=668)
        showfood.mainloop()
    def closedelete():
        global summary
        summary.destroy()
    def Summary():
        global summary
        summary=Toplevel()
        summary.title("สรุปยอดขาย")
        summary.geometry("1285x760+125+15")
        image = Image.open( r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\35.png")
        photo = ImageTk.PhotoImage(image)
        Label(summary, image=photo).place(relwidth=1, relheight=1)
        summary.option_add("*Font", "consolas 25")
        def SummaryDay():
            connection = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
            cursor = connection.cursor()
            # ดึงข้อมูลการขายจากฐานข้อมูล
            cursor.execute("SELECT day, SUM(price_Menu) FROM Summary GROUP BY day")
            results = cursor.fetchall() 
            style = ttk.Style()
            style.configure("Treeview", font=("consolas", 20)) 
            style.configure("Treeview.Heading", font=("consolas", 20))
            
            for row in result_tree.get_children():
                result_tree.delete(row)
            # แสดงผลลัพธ์ในตาราง
            for day, price_Menu in results:
                total_with_baht = f"{price_Menu} บาท"
                result_tree.insert("", "end", values=(day, total_with_baht))

        def SummaryMonth():
            connection = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
            cursor = connection.cursor()
            # ดึงข้อมูลการขายจากฐานข้อมูล
            # เปลี่ยน SQL Query เพื่อรวมยอดขายรายเดือน
            cursor.execute("SELECT strftime('%Y-%m', day) AS month, SUM(price_Menu) FROM Summary GROUP BY month")
            results = cursor.fetchall() 
            style = ttk.Style()
            style.configure("Treeview", font=("consolas", 20)) 
            style.configure("Treeview.Heading", font=("consolas", 20))
            for row in result_tree.get_children():
                result_tree.delete(row)
            # แสดงผลลัพธ์ในตาราง
            for month, price_Menu in results:
                total_with_baht = f"{price_Menu} บาท"
                result_tree.insert("", "end", values=(month, total_with_baht))
        result_tree = ttk.Treeview(summary, columns=("Date", "Total"),height=20)
        result_tree.heading("#1", text="วันที่")
        result_tree.heading("#2", text="ยอดรวม")
        result_tree.place(x=350,y=100)
        vertical_scrollbar = ttk.Scrollbar(summary, orient="vertical", command=result_tree.yview)
        # เชื่อมตาราง Treeview กับ Scrollbar
        result_tree.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.place(x=610,y=1000)    
        Button(summary,text="รายวัน",font=("FC Muffin",23,"bold"),borderwidth = 0,width=10,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=SummaryDay).place(x=750,y=673)
        Button(summary,text="รายเดือน",font=("FC Muffin",23,"bold"),borderwidth = 0,width=10,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=SummaryMonth).place(x=1040,y=673)
        Button(summary,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closedelete).place(x=95,y=668)
        summary.mainloop()
    def closecancel():
        global cancel
        cancel.destroy()
    def Cancel():
        global cancel
        cancel=Toplevel()
        cancel.title("ยกเลิกออเดอร์")
        cancel.geometry("1285x760+125+15")
        image = Image.open(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\14.png")
        photo = ImageTk.PhotoImage(image)
        Label(cancel, image=photo).place(relwidth=1, relheight=1)
        cancel.option_add("*Font", "consolas 30")
        q = tk.Entry(cancel,font=("FC Muffin",26,),width=32,borderwidth=0, relief="flat",justify="center")
        q.place(x=470,y=355)
        q.configure(background="white",fg="Black")
        def deletenext2():
            global cancel
            # เชื่อมต่อกับฐานข้อมูล SQLite3
            conn = sqlite3.connect(r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\DB Browser for SQLite\sql\projectfood.db")
            cursor = conn.cursor()
            # สร้างคำสั่ง SQL สำหรับลบข้อมูล
            # เช่น ลบข้อมูลในตาราง receipts ที่มี id = 1
            id = q.get()
            cursor.execute('''DELETE FROM restaurant WHERE id = ?''', (id,))
            # ยืนยันการเปลี่ยนแปลง
            conn.commit()
            # ปิดการเชื่อมต่อกับฐานข้อมูล
            conn.close()
            p = messagebox.showinfo("แจ้งเตือน","การลบออเดอร์ดำเนินการเสร็จสิ้น")
            if p:
                cancel.destroy()
        Button(cancel,text="ยืนยัน",font=("FC Muffin",23,"bold"),borderwidth = 0,width=10,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=deletenext2).place(x=575,y=615)
        Button(cancel,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closecancel).place(x=95,y=668)
        
        cancel.mainloop()
    Button(attendant,text="แสดงรายการอาหารที่สั่งแล้ว",font=("FC Muffin",24,"bold"),borderwidth = 0,width=25,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Showfood).place(x=180,y=110)
    Button(attendant,text="สรุปยอดขาย",font=("FC Muffin",24,"bold"),borderwidth = 0,width=25,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Summary).place(x=510,y=110)
    Button(attendant,text="ยกเลิกออเดอร์",font=("FC Muffin",25,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Cancel).place(x=880,y=110)
    Button(attendant,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closeattendant).place(x=95,y=668)

    attendant.mainloop()
def closedeverloper():
    global deverloper
    deverloper.destroy()
def Deverloper():
    global deverloper
    deverloper=Toplevel()
    deverloper.title("ผู้พัฒนาระบบ")
    deverloper.geometry("1285x760+125+15")
    image = Image.open( r"C:\Users\Chany\OneDrive\Documents\year2term1\python\codepython\root\33.png")
    photo = ImageTk.PhotoImage(image)
    Label(deverloper, image=photo).place(relwidth=1, relheight=1)
    Button(deverloper,text="⤌ ย้อนกลับ",font=("FC Muffin",23,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=closedeverloper).place(x=95,y=668)

    deverloper.mainloop()
Button(root,text="ลูกค้า",font=("FC Muffin",25,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Customer).place(x=175,y=110)
Button(root,text="ผู้ดูแลระบบ",font=("FC Muffin",25,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=PwAttendant).place(x=550,y=110)
Button(root,text="ผู้พัฒนาระบบ",font=("FC Muffin",25,"bold"),borderwidth = 0,width=15,bg='#1F798A',fg='#FFFFB0',activebackground = "#1F798A",command=Deverloper).place(x=900,y=110)
root.configure(background='')
root.mainloop() #ทำงานวน