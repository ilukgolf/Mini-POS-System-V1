import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import config
import alert_message

def user_management(display, user_data):
    user_management_frame = tk.Frame(display, bg=config.color_default)

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
        user_account_list = connect_database.database_execute(sql)

        for i, user_record in enumerate(user_account_list):
            # user account status
            if user_record[3] == 'active':
                u_status = 'ปกติ'
            elif user_record[3] == 'inactive':
                u_status = 'ปิดใช้งาน'
            elif user_record[3] == 'lock':
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
        add_new_user_account_frame = tk.Frame(main_frame, bg=config.color_default)
        add_new_user_account_frame.place(x=5, y=5, width=1037, height=610)


    create_frame()
    # show_user_account()
    add_new_user_account()
    # user_account_tree.bind('<Double-1>', lambda event: show_user_account_detail())
    return user_management_frame

if __name__ == '__main__':
    import main
    main.App()