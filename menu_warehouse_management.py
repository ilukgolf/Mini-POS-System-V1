import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import config

def warehouse_management(display, user_data):
    warehouse_management_frame = tk.Frame(display, bg=config.color_default)

    product_id = tk.StringVar()
    product_name = tk.StringVar()
    product_quantity = tk.StringVar()
    product_quantity_unit = tk.StringVar()
    product_type = tk.StringVar()
    product_unit = tk.StringVar()
    product_sell_price = tk.StringVar()
    product_amount = tk.StringVar()

    add_new_user_account_frame = tk.Frame(warehouse_management_frame, bg=config.color_default)
    add_new_user_account_frame.place(x=5, y=5, width=1037, height=610)
    style_label = ttk.Style()
    style_label.configure("A.Label", font=("FC Lamoon Bold", 18), anchor="e")
    
    label_menu = tk.Label(add_new_user_account_frame, text="เพิ่มทะเบียนสินค้า", font=tkfont.Font(family='FC Lamoon', size=30, weight='bold'))
    label_menu.place(x=0, y=50, width=1020)
            
    ttk.Label(add_new_user_account_frame, text="รหัสสินค้า :", style="A.Label").place(x=79, y=150, width=200)
    ttk.Label(add_new_user_account_frame, text="ชื่อสินค้า :", style="A.Label").place(x=0, y=200, width=280)
    ttk.Label(add_new_user_account_frame, text="ปริมาณ :", style="A.Label").place(x=79, y=250, width=200)
    ttk.Label(add_new_user_account_frame, text="หน่วยนับ :", style="A.Label").place(x=79, y=300, width=200)
    ttk.Label(add_new_user_account_frame, text="ประเภท :", style="A.Label").place(x=79, y=350, width=200)
    ttk.Label(add_new_user_account_frame, text="ราคาขายต่อหน่วย :", style="A.Label").place(x=79, y=400, width=200)
    ttk.Label(add_new_user_account_frame, text="หน่วยนับของปริมาณ :", style="A.Label").place(x=520, y=250, width=200)

    def only_numbers(char):
        return char.isdigit()
    validation = add_new_user_account_frame.register(only_numbers)
    
    Id = ttk.Entry(add_new_user_account_frame, font=("FC Lamoon", 18), textvariable=product_id)
    Id.place(x=290, y=150, width=250, height=30)

    name = tk.Entry(add_new_user_account_frame, font=("FC Lamoon", 18), textvariable=product_name)
    name.place(x=290, y=200, width=250, height=30)

    quantity = tk.Entry(add_new_user_account_frame, font=("FC Lamoon", 18), textvariable=product_quantity)
    quantity.place(x=290, y=250, width=250, height=30)

    quantity_unit = tk.Entry(add_new_user_account_frame, font=("FC Lamoon", 18), textvariable=product_quantity_unit)
    quantity_unit.place(x=730, y=250, width=250, height=30)

    unit = tk.Entry(add_new_user_account_frame, font=("FC Lamoon", 18), textvariable=product_unit)
    unit.place(x=290, y=300, width=250, height=30)

    type_product = tk.Entry(add_new_user_account_frame, font=("FC Lamoon", 18), textvariable=product_type)
    type_product.place(x=290, y=350, width=250, height=30)

    sell_price = tk.Entry(add_new_user_account_frame, font=("FC Lamoon", 18), textvariable=product_sell_price)
    sell_price.place(x=290, y=400, width=250, height=30)

    cancel_botton = tk.Button(add_new_user_account_frame, bg="#C40000", text="ยกเลิก", font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), fg="white", command=lambda: cancel())
    cancel_botton.place(x=725, y=520, width=110, height=50)

    save_botton = tk.Button(add_new_user_account_frame, bg="#00C400", text="บันทึก", font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), fg="white", command=lambda: save())
    save_botton.place(x=860, y=520, width=110, height=50)

    def save():
        import datetime
        day = datetime.datetime.now().strftime("%d")
        month = datetime.datetime.now().strftime("%m")
        year = datetime.datetime.now().strftime("%y")
        Year = datetime.datetime.now().strftime("%Y")
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        second = datetime.datetime.now().strftime("%S")

        a_product_id = Id.get()
        a_product_date_create = day + "/" + month + "/" + Year + " " + hour + ":" + minute + ":" + second
        a_product_date_update = a_product_date_create
        a_product_type = type_product.get()
        a_product_name = name.get()
        a_product_quantity = quantity.get()
        a_product_quantity_unit = quantity_unit.get()
        a_product_amount = 999
        a_product_unit = unit.get()
        a_product_sell_price = sell_price.get()

        if not (product_id == "" or product_name == "" or product_quantity == "" or product_quantity_unit == "" or product_unit == "" or product_sell_price == ""):
            import sqlite3
            conn = sqlite3.connect('assets\\backend\\database\\minipos.db')
            cursor = conn.cursor()

            sql = '''INSERT INTO product_storage (product_id, product_date_create, product_date_update, product_type, product_name, product_quantity, product_quantity_unit, product_amount, product_unit, product_selling_price, product_seller_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(sql, (a_product_id, a_product_date_create, a_product_date_update, a_product_type, a_product_name, a_product_quantity, a_product_quantity_unit, a_product_amount, a_product_unit, a_product_sell_price, "165030099"))
            conn.commit()
            conn.close()
    def cancel():
        product_id.set("")
        product_name.set("")
        product_quantity.set("")
        product_quantity_unit.set("")
        product_type.set("")
        product_unit.set("")
        product_sell_price.set("")
        product_amount.set("")


    return warehouse_management_frame

if __name__ == '__main__':
    import main
    main.App()