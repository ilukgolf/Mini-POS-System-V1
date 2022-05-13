import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import config
import alert_message
from tkcalendar import DateEntry

def user_management(display, user_data):
    user_management_frame = tk.Frame(display, bg=config.color_default)

    user_rank = tk.StringVar()
    user_identification_id = tk.StringVar()
    user_name_prefix = tk.StringVar()
    user_name_th = tk.StringVar()
    user_lastname_th = tk.StringVar()
    user_name_en = tk.StringVar()
    user_lastname_en = tk.StringVar()
    user_date_of_birthday = tk.StringVar()
    user_phone_number = tk.StringVar()

    def create_frame():
        global main_frame
        main_frame = tk.Frame(user_management_frame, bg=config.color_default)
        main_frame.place(x=0, y=0, width=1047, height=620)

        # show_user_account_frame = tk.Frame(main_frame, bg=config.color_red)
        # show_user_account_frame.place(x=5, y=5, width=1037, height=610)

        # show_user_account_detail_frame = tk.Frame(main_frame, bg=config.color_default)
        # show_user_account_detail_frame.place(x=5, y=5, width=1037, height=610)

    def show_user_account():
        global show_user_account_frame
        show_user_account_frame = tk.Frame(main_frame, bg=config.color_default)
        show_user_account_frame.place(x=5, y=5, width=1037, height=610)

        top_frame = tk.Frame(show_user_account_frame, bg=config.color_default)
        top_frame.place(x=0, y=0, width=1037, height=50)

        bottom_frame = tk.Frame(show_user_account_frame, bg=config.color_default)
        bottom_frame.place(x=0, y=55, width=1037, height=560)

        add_new_user_button = tk.Button(
            top_frame, text=" เพิ่มบัญชีผู้ใช้ ", cursor="hand2", compound=tk.LEFT,
            activebackground=config.color_green, activeforeground=config.color_white,
            font=tkfont.Font(family='FC Lamoon', size=14, weight='bold'),
            background=config.color_green, foreground=config.color_white,
            command=lambda: add_new_user_account())
        add_new_user_button.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5, pady=5, sticky=tk.E)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('AngsanaUPC', 15, 'bold'))
        style.configure("Treeview", font=('AngsanaUPC', 15), rowheight=25)
        style.map('Treeview', background=[('selected', config.color_list_selected)])

        global user_account_tree
        user_account_tree = ttk.Treeview(
            bottom_frame, padding=5, selectmode='extended',
            columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'), height=20, show='headings')
        user_account_tree.pack(padx=5, pady=0)

        user_account_tree.tag_configure("even", background=config.color_list_even)
        user_account_tree.tag_configure("odd", background=config.color_list_odd)

        user_account_tree.heading('#0', text='')
        user_account_tree.heading('#1', text='ลำดับ')
        user_account_tree.heading('#2', text='สถานะบัญชี')
        user_account_tree.heading('#3', text='ตำแหน่ง')
        user_account_tree.heading('#4', text='ชื่อผู้ใช้')
        user_account_tree.heading('#5', text='ชื่อ-นามสกุล')
        user_account_tree.heading('#6', text='เบอร์โทรศัพท์')
        user_account_tree.heading('#7', text='ที่อยู่')


        user_account_tree.column('#0', width=0)
        user_account_tree.column('#1', width=50, anchor=tk.CENTER, stretch=True)
        user_account_tree.column('#2', width=100, anchor=tk.W, stretch=True)
        user_account_tree.column('#3', width=100, anchor=tk.W, stretch=True)
        user_account_tree.column('#4', width=110, anchor=tk.W, stretch=True)
        user_account_tree.column('#5', width=220, anchor=tk.W, stretch=True)
        user_account_tree.column('#6', width=120, anchor=tk.CENTER, stretch=True)
        user_account_tree.column('#7', width=300, anchor=tk.W, stretch=True)

        import connect_database
        sql = "SELECT * FROM user_accounts"
        global user_account_list
        user_account_list = connect_database.database_execute(sql)

        for i, user_record in enumerate(user_account_list):
            # user account status
            if user_record[3] == 'active':
                u_status = 'ปกติ'
            elif user_record[3] == 'inactive':
                u_status = 'ปิดใช้งาน'
            elif user_record[3] == 'locked':
                u_status = 'ถูกระงับ'

            # user account full name
            name = ""
            if user_record[4] == 'mr':
                name += 'นาย'
            elif user_record[4] == 'miss':
                name += 'นางสาว'
            elif user_record[4] == 'ms':
                name += 'นาง'
            if user_record[5] != '-':
                name += user_record[5]
            if user_record[6] != '-':
                name += " " + user_record[6]

            # user account rank
            rank = ""
            if user_record[0][4] == '1':
                rank = 'ผู้ดูแลระบบ'
            elif user_record[0][4] == '2':
                rank = 'พนักงาน'

            if i%2 == 0:
                if len(user_account_list) < 10:
                    user_account_tree.insert(parent='', index='end', text=user_record[0], tags=('even',),
                    values=("%.1d" %(i+1), u_status, rank, user_record[13], name, user_record[11], user_record[12]))
                elif len(user_account_list) < 100:
                    user_account_tree.insert(parent='', index='end', text=user_record[0], tags=('even',),
                    values=("%.2d" %(i+1), u_status, rank, user_record[13], name, user_record[11], user_record[12]))
            else:
                if len(user_account_list) < 10:
                    user_account_tree.insert(parent='', index='end', text=user_record[0], tags=('odd',),
                    values=("%.1d" %(i+1), u_status, rank, user_record[13], name, user_record[11], user_record[12]))
                elif len(user_account_list) < 100:
                    user_account_tree.insert(parent='', index='end', text=user_record[0], tags=('odd',),
                    values=("%.2d" %(i+1), u_status, rank, user_record[13], name, user_record[11], user_record[12]))

    def show_user_account_detail():
        show_user_account_detail_frame = tk.Frame(main_frame, bg=config.color_default)
        show_user_account_detail_frame.place(x=5, y=5, width=1037, height=610)

        user_record = user_account_tree.item(user_account_tree.focus())
        user_account_tree.selection_remove(user_account_tree.focus())
        print(user_record)


        pass

    def add_new_user_account():
        global add_new_user_account_frame
        add_new_user_account_frame = tk.Frame(main_frame, bg=config.color_default)
        add_new_user_account_frame.place(x=5, y=5, width=1037, height=610)
        style_label = ttk.Style()
        style_label.configure("A.Label", font=("FC Lamoon Bold", 18), anchor="e")

        label_menu = tk.Label(add_new_user_account_frame, text="เพิ่มบัญชีผู้ใช้", font=tkfont.Font(family='FC Lamoon', size=30, weight='bold'))
        label_menu.place(x=0, y=50, width=1020)

        ttk.Label(add_new_user_account_frame, text="ตำแหน่ง :", style="A.Label").place(x=79, y=150, width=200)
        ttk.Label(add_new_user_account_frame, text="เลขประจำตัวบัตรประชาชน :", style="A.Label").place(x=0, y=200, width=280)
        ttk.Label(add_new_user_account_frame, text="คำนำหน้าชื่อ :", style="A.Label").place(x=79, y=250, width=200)
        ttk.Label(add_new_user_account_frame, text="ชื่อจริง (ไทย) :", style="A.Label").place(x=79, y=300, width=200)
        ttk.Label(add_new_user_account_frame, text="นามสกุล (ไทย) :", style="A.Label").place(x=79, y=350, width=200)
        ttk.Label(add_new_user_account_frame, text="ที่อยู่อาศัย :", style="A.Label").place(x=79, y=400, width=200)
        ttk.Label(add_new_user_account_frame, text="ชื่อจริง (อังกฤษ) :", style="A.Label").place(x=500, y=300, width=200)
        ttk.Label(add_new_user_account_frame, text="นามสกุล (อังกฤษ) :", style="A.Label").place(x=500, y=350, width=200)
        ttk.Label(add_new_user_account_frame, text="วัน เดือน ปีเกิด :", style="A.Label").place(x=500, y=400, width=200)
        ttk.Label(add_new_user_account_frame, text="เบอร์โทรศัพท์ :", style="A.Label").place(x=500, y=450, width=200)
        
        def only_numbers(char):
            return char.isdigit()
        validation = add_new_user_account_frame.register(only_numbers)

        rank = ["ผู้ดูแลระบบ", "พนักงาน"]
        position = ttk.Combobox(add_new_user_account_frame , font=tkfont.Font(family='FC Lamoon', size=18), textvariable=user_rank, state="readonly", values=rank)
        user_rank.set(rank[0])
        position.place(x=290, y=150, width=250, height=30)

        identification_id = tk.Entry(add_new_user_account_frame, font=tkfont.Font(family='FC Lamoon', size=18), textvariable=user_identification_id,validate="key", validatecommand=(validation, '%S'))#input digit only
        identification_id.place(x=290, y=200, width=250, height=30)

        prefix = ["นาย", "นาง", "นางสาว"]
        name_prefix = ttk.Combobox(add_new_user_account_frame, font=tkfont.Font(family='FC Lamoon', size=18), textvariable=user_name_prefix, state="readonly", values=prefix)
        name_prefix.set(prefix[0])
        name_prefix.place(x=290, y=250, width=250, height=30)

        name_TH = tk.Entry(add_new_user_account_frame, font=tkfont.Font(family='FC Lamoon', size=18), textvariable=user_name_th)
        name_TH.place(x=290, y=300, width=250, height=30)

        lastname_TH = tk.Entry(add_new_user_account_frame, font=tkfont.Font(family='FC Lamoon', size=18), textvariable=user_lastname_th)
        lastname_TH.place(x=290, y=350, width=250, height=30)

        global user_residence
        user_residence = tk.Text(add_new_user_account_frame, font=tkfont.Font(family='FC Lamoon', size=18))
        user_residence.place(x=290, y=400, width=250, height=90)

        name_EN = tk.Entry(add_new_user_account_frame, font=tkfont.Font(family='FC Lamoon', size=18), textvariable=user_name_en)
        name_EN.place(x=710, y=300, width=250, height=30)

        lastname_EN = tk.Entry(add_new_user_account_frame, font=tkfont.Font(family='FC Lamoon', size=18), textvariable=user_lastname_en)
        lastname_EN.place(x=710, y=350, width=250, height=30)

        birthday = DateEntry(add_new_user_account_frame, date_pattern="dd/mm/yyyy", font=("FC Lamoon", 16), textvariable=user_date_of_birthday, state="readonly")
        birthday.place(x=710, y=400, width=250, height=30)

        phone = tk.Entry(add_new_user_account_frame, font=tkfont.Font(family='FC Lamoon', size=18), textvariable=user_phone_number, validate="key", validatecommand=(validation, '%S'))
        phone.place(x=710, y=450, width=250, height=30)



        cancel_botton = tk.Button(add_new_user_account_frame, bg="#C40000", text="ยกเลิก", font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), fg="white", command=lambda: cancel_click())
        cancel_botton.place(x=725, y=520, width=110, height=50)

        save_botton = tk.Button(add_new_user_account_frame, bg="#00C400", text="บันทึก", font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), fg="white", command=lambda: save_new_user())
        save_botton.place(x=860, y=520, width=110, height=50)

    def cancel_click():
        add_new_user_account_frame.destroy()
        user_rank.set("")
        user_identification_id.set("")
        user_name_prefix.set("")
        user_name_th.set("")
        user_lastname_th.set("")
        user_name_en.set("")
        user_lastname_en.set("")
        user_date_of_birthday.set("")
        user_phone_number.set("")
        show_user_account()

    def save_new_user():
        import datetime
        day = datetime.datetime.now().strftime("%d")
        month = datetime.datetime.now().strftime("%m")
        year = datetime.datetime.now().strftime("%y")
        Year = datetime.datetime.now().strftime("%Y")
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        second = datetime.datetime.now().strftime("%S")

        import sqlite3
        conn = sqlite3.connect('assets\\backend\\database\\minipos.db')
        cursor = conn.cursor()

        if user_rank.get() == "ผู้ดูแลระบบ":
            user_id = str(165010000 + int(user_account_list[len(user_account_list)-1][0][5:9])+1)
        elif user_rank.get() == "พนักงาน":
            user_id = str(165020000 + int(user_account_list[len(user_account_list)-1][0][5:9])+1)

        date_create = day + "/" + month + "/" + Year + " " + hour + ":" + minute + ":" + second
        date_update = date_create

        status = "active"

        if user_name_prefix.get() == "นาย":
            name_prefix = "mr"
        elif user_name_prefix.get() == "นาง":
            name_prefix = "ms"
        elif user_name_prefix.get() == "นางสาว":
            name_prefix = "miss"

        name_th = user_name_th.get()
        lastname_th = user_lastname_th.get()
        name_en = user_name_en.get()
        lastname_en = user_lastname_en.get()

        identification_id = user_identification_id.get()

        date_of_birth = user_date_of_birthday.get()

        phone_number = user_phone_number.get()

        residence = user_residence.get("1.0", "end-1c")

        username = name_en.lower()+"."+lastname_en[0:4].lower()

        import password_encrypt
        password = password_encrypt.password_encrypt(username, phone_number)
        print(password)

        sql = '''INSERT INTO user_accounts (user_id, user_date_create, user_date_update, user_status, user_gender, user_name_th, user_lastname_th, user_name_en, user_lastname_en, user_identification_id, user_date_of_birth, user_phone_number, user_residence, user_username, user_password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        cursor.execute(sql, [user_id, date_create, date_update, status, name_prefix, name_th, lastname_th, name_en, lastname_en, identification_id, date_of_birth, phone_number, residence, username, password])
        conn.commit()
        conn.close()

    create_frame()
    show_user_account()
    # add_new_user_account()
    # user_account_tree.bind('<Double-1>', lambda event: show_user_account_detail())
    return user_management_frame

if __name__ == '__main__':
    import main
    main.App()