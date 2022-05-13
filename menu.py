import tkinter as tk
import tkinter.font as tkfont
import config
import alert_message

def main_menu_frame(root, user_data):
    menu_frame = tk.Frame(root, bg=config.window_background_color)

    global pos_logo, user_management_icon, seller_management_icon, warehouse_management_icon
    global selling_product_icon, search_product_icon, summary_report_icon, order_product_icon, logout_icon
    pos_logo = tk.PhotoImage(file="assets\\backend\\images\\pos_logo_64.png")
    user_management_icon = tk.PhotoImage(file="assets\\backend\\images\\menu\\user_management.png")
    seller_management_icon = tk.PhotoImage(file="assets\\backend\\images\\menu\\seller_management.png")
    warehouse_management_icon = tk.PhotoImage(file="assets\\backend\\images\\menu\\warehouse_management.png")
    selling_product_icon = tk.PhotoImage(file="assets\\backend\\images\\menu\\selling_product.png")
    search_product_icon = tk.PhotoImage(file="assets\\backend\\images\\menu\\search_product.png")
    summary_report_icon = tk.PhotoImage(file="assets\\backend\\images\\menu\\summary_report.png")
    order_product_icon = tk.PhotoImage(file="assets\\backend\\images\\menu\\order_product.png")
    logout_icon = tk.PhotoImage(file="assets\\backend\\images\\logout.png")

    def create_frame():
        global main_frame, top_frame, left_frame

        # main frame for menu
        main_frame = tk.Frame(menu_frame, background=config.window_background_color)
        main_frame.place(x=0, y=0, width=config.window_width, height=config.window_height)

        # top frame for menu
        top_frame = tk.Frame(main_frame, background=config.window_background_color)
        top_frame.place(x=0, y=0, width=config.window_width, height=95)

        # left frame for menu
        left_frame = tk.Frame(main_frame, background=config.window_background_color)
        left_frame.place(x=8, y=90, width=210, height=620)

        # right frame for menu
        # right_frame = tk.Frame(main_frame, background=config.color_default)
        # right_frame.place(x=225, y=90, width=1047, height=620)

    def top_frame_content():
        global top_frame_inside, top_frame_inside_left, top_frame_inside_right

        top_frame_inside = tk.Frame(top_frame, background=config.color_default)
        top_frame_inside.pack(expand=True)

        top_frame_inside_left = tk.Frame(top_frame_inside, background=config.color_default)
        top_frame_inside_left.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W, ipadx=210, ipady=0)

        top_frame_inside_right = tk.Frame(top_frame_inside, background=config.color_default)
        top_frame_inside_right.grid(row=0, column=1, padx=5, pady=2, sticky=tk.E)

        # logo
        logo_label = tk.Label(
            top_frame_inside_left, image=pos_logo, background=config.color_default, cursor="hand2")
        logo_label.grid(row=0, column=0, columnspan=1, rowspan=2, padx=0, pady=0)
        logo_label.bind("<Button-1>", lambda event: refresh_menu_frame())

        # title label
        title_label_1 = tk.Label(
            top_frame_inside_left, text="Mini",
            font=tkfont.Font(family='FC Lamoon', size=18, weight='normal'),
            background=config.color_default, foreground=config.color_black, anchor=tk.E)
        title_label_1.grid(row=0, column=1, columnspan=1, rowspan=1, padx=0, pady=0, sticky=tk.SE)

        title_label_2 = tk.Label(
            top_frame_inside_left, text="POS",
            font=tkfont.Font(family='FC Lamoon', size=18, weight='bold', underline=1),
            background=config.color_default, foreground=config.color_black, anchor=tk.S)
        title_label_2.grid(row=0, column=2, columnspan=1, rowspan=1, padx=0, pady=0, sticky=tk.S)
        title_label_2.bind("<Button-1>", lambda event: alert_message.Hmmm())

        title_label_3 = tk.Label(
            top_frame_inside_left, text="System",
            font=tkfont.Font(family='FC Lamoon', size=18, weight='normal'),
            background=config.color_default, foreground=config.color_black, anchor=tk.W)
        title_label_3.grid(row=0, column=3, columnspan=1, rowspan=1, padx=0, pady=0, sticky=tk.SW)

        title_label_4 = tk.Label(
            top_frame_inside_left, text="(by CS311 Project @ BU)",
            font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
            background=config.color_default, foreground=config.color_black, anchor=tk.N)
        title_label_4.grid(row=1, column=1, columnspan=3, rowspan=1, padx=0, pady=0, sticky=tk.N)

        user_showname = ""
        if user_data[4] == 'mr':
            user_showname = user_showname + "นาย"
        elif user_data[4] == 'ms':
            user_showname = user_showname + "นาง"
        elif user_data[4] == 'miss':
            user_showname = user_showname + "นางสาว"
        if user_data[5] != '-':
            user_showname = user_showname + str(user_data[5])
        if user_data[6] != '-':
            user_showname = user_showname + " " + str(user_data[6])
        if user_data[0][4] == '1' and user_data[13] != 'admin':
           user_showname = user_showname + " (ผู้ดูแลระบบ)"
        elif user_data[0][4] == '2':
            user_showname = user_showname + " (พนักงาน)"
        if user_data[0][4] == '1' and user_data[13] == 'admin':
            user_showname = "Admin (ผู้ดูแลระบบ)"
        if user_data[0][4] == '2' and user_data[13] == 'staff':
            user_showname = "Staff (พนักงาน)"

        # user name label
        user_name_label = tk.Label(
            top_frame_inside_right, text=user_showname,
            font=tkfont.Font(family='FC Lamoon', size=18, weight='normal'),
            background=config.color_default, foreground=config.color_black, width=57, anchor=tk.E)
        user_name_label.grid(row=0, column=0, columnspan=1, rowspan=1, padx=5, pady=0)

        # logout button
        logout_button = tk.Button(
            top_frame_inside_right, text=" ออกจากระบบ ", cursor="hand2", image=logout_icon, compound=tk.LEFT,
            activebackground=config.color_red, activeforeground=config.color_white,
            font=tkfont.Font(family='FC Lamoon', size=14, weight='bold'),
            background=config.color_red, foreground=config.color_white,
            command=lambda: logout_button_click())
        logout_button.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5, pady=0, sticky=tk.E)

    def left_frame_content():
        global left_frame_inside, user_management_frame, seller_management_frame, warehouse_management_frame
        global selling_product_frame

        def switch_menu_selection(content):
            for widget in left_frame_inside.winfo_children():
                    if isinstance(widget, tk.Frame) and widget is content:
                        widget['background'] = config.color_highlight
                        for item in widget.winfo_children():
                            if isinstance(item, tk.Label):
                                item['background'] = config.color_highlight
                                item['foreground'] = config.color_white
                    elif isinstance(widget, tk.Frame) and widget is not content:
                        widget['background'] = config.window_background_color2
                        for item in widget.winfo_children():
                            if isinstance(item, tk.Label):
                                item['background'] = config.window_background_color2
                                item['foreground'] = config.color_white
            for frame in main_frame.winfo_children():
                if isinstance(frame, tk.Frame) and frame is not top_frame and frame is not left_frame:
                    frame.destroy()

        global selling_product_frame_click
        def selling_product_frame_click():
            switch_menu_selection(selling_product_frame)
            import menu_selling_product
            frame = menu_selling_product.selling_product(main_frame, user_data)
            frame.place(x=225, y=90, width=1047, height=620)

        def search_product_frame_click():
            switch_menu_selection(search_product_frame)
            import menu_search_product
            frame = menu_search_product.search_product(main_frame, user_data)
            frame.place(x=225, y=90, width=1047, height=620)

        def user_management_frame_click():
            switch_menu_selection(user_management_frame)
            import menu_user_management
            frame = menu_user_management.user_management(main_frame, user_data)
            frame.place(x=225, y=90, width=1047, height=620)

        # def seller_management_frame_click():
        #     switch_menu_selection(seller_management_frame)
        #     import menu_seller_management
        #     frame = menu_seller_management.seller_management(main_frame, user_data)
        #     frame.place(x=225, y=90, width=1047, height=620)

        def warehouse_management_frame_click():
            switch_menu_selection(warehouse_management_frame)
            import menu_warehouse_management
            frame = menu_warehouse_management.warehouse_management(main_frame, user_data)
            frame.place(x=225, y=90, width=1047, height=620)

        # def summary_report_frame_click():
        #     switch_menu_selection(summary_report_frame)
        #     import menu_summary_report
        #     frame = menu_summary_report.summary_report(main_frame, user_data)
        #     frame.place(x=225, y=90, width=1047, height=620)

        # def order_product_frame_click():
        #     switch_menu_selection(order_product_frame)
        #     import menu_order_product
        #     frame = menu_order_product.order_product(main_frame, user_data)
        #     frame.place(x=225, y=90, width=1047, height=620)

        left_frame_inside = tk.Frame(left_frame, background=config.window_background_color)
        left_frame_inside.pack(expand=True, fill=tk.Y)

        selling_product_frame = tk.Frame(left_frame_inside, background=config.window_background_color2, cursor="hand2")
        selling_product_frame.pack(fill=tk.Y, padx=0, pady=0, ipadx=10)
        selling_product_image = tk.Label(
            selling_product_frame, image=selling_product_icon,
            background=config.window_background_color2, width=70, height=70)
        selling_product_image.grid(row=0, column=0, columnspan=1, rowspan=1, padx=2, pady=3)
        selling_product_label = tk.Label(
            selling_product_frame, text="ขายสินค้า\n(บันทึกการขาย)",
            font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), width=12,
            background=config.window_background_color2, foreground=config.color_black, anchor=tk.CENTER)
        selling_product_label.grid(row=0, column=1, columnspan=1, rowspan=1, padx=2, pady=3, sticky=tk.E)
        selling_product_frame.bind("<Button-1>", lambda event: selling_product_frame_click())
        selling_product_image.bind("<Button-1>", lambda event: selling_product_frame_click())
        selling_product_label.bind("<Button-1>", lambda event: selling_product_frame_click())

        search_product_frame = tk.Frame(left_frame_inside, background=config.window_background_color2, cursor="hand2")
        search_product_frame.pack(fill=tk.Y, padx=0, pady=10, ipadx=10)
        search_product_image = tk.Label(
            search_product_frame, image=search_product_icon,
            background=config.window_background_color2, width=70, height=70)
        search_product_image.grid(row=1, column=0, columnspan=1, rowspan=1, padx=2, pady=3)
        search_product_label = tk.Label(
            search_product_frame, text="ค้นหาสินค้า\n(ดูข้อมูลสินค้า)",
            font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), width=12,
            background=config.window_background_color2, foreground=config.color_black, anchor=tk.CENTER)
        search_product_label.grid(row=1, column=1, columnspan=1, rowspan=1, padx=2, pady=3, sticky=tk.E)
        search_product_frame.bind("<Button-1>", lambda event: search_product_frame_click())
        search_product_image.bind("<Button-1>", lambda event: search_product_frame_click())
        search_product_label.bind("<Button-1>", lambda event: search_product_frame_click())

        if user_data[0][4] == '1':
            user_management_frame = tk.Frame(left_frame_inside, background=config.window_background_color2, cursor="hand2")
            user_management_frame.pack(fill=tk.Y, padx=0, pady=0, ipadx=10)
            user_management_image = tk.Label(
                user_management_frame, image=user_management_icon,
                background=config.window_background_color2, width=70, height=70)
            user_management_image.grid(row=2, column=0, columnspan=1, rowspan=1, padx=2, pady=3)
            user_management_label = tk.Label(
                user_management_frame, text="จัดการบัญชี\nผู้ใช้งานระบบ",
                font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), width=12,
                background=config.window_background_color2, foreground=config.color_black, anchor=tk.CENTER)
            user_management_label.grid(row=2, column=1, columnspan=1, rowspan=1, padx=2, pady=3, sticky=tk.E)
            user_management_frame.bind("<Button-1>", lambda event: user_management_frame_click())
            user_management_image.bind("<Button-1>", lambda event: user_management_frame_click())
            user_management_label.bind("<Button-1>", lambda event: user_management_frame_click())

            # seller_management_frame = tk.Frame(left_frame_inside, background=config.window_background_color2, cursor="hand2")
            # seller_management_frame.pack(fill=tk.Y, padx=0, pady=10, ipadx=10)
            # seller_management_image = tk.Label(
            #     seller_management_frame, image=seller_management_icon,
            #     background=config.window_background_color2, width=70, height=70)
            # seller_management_image.grid(row=3, column=0, columnspan=1, rowspan=1, padx=2, pady=3)
            # seller_management_label = tk.Label(
            #     seller_management_frame, text="จัดการบัญชี\nตัวแทนจำหน่าย",
            #     font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), width=12,
            #     background=config.window_background_color2, foreground=config.color_black, anchor=tk.CENTER)
            # seller_management_label.grid(row=3, column=1, columnspan=1, rowspan=1, padx=2, pady=3, sticky=tk.E)
            # seller_management_frame.bind("<Button-1>", lambda event: seller_management_frame_click())
            # seller_management_image.bind("<Button-1>", lambda event: seller_management_frame_click())
            # seller_management_label.bind("<Button-1>", lambda event: seller_management_frame_click())

            warehouse_management_frame = tk.Frame(left_frame_inside, background=config.window_background_color2, cursor="hand2")
            warehouse_management_frame.pack(fill=tk.Y, padx=0, pady=10, ipadx=10)
            warehouse_management_image = tk.Label(
                warehouse_management_frame, image=warehouse_management_icon,
                background=config.window_background_color2, width=70, height=70)
            warehouse_management_image.grid(row=3, column=0, columnspan=1, rowspan=1, padx=2, pady=3)
            warehouse_management_label = tk.Label(
                warehouse_management_frame, text="จัดการบัญชี\nทะเบียนสินค้า",
                font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), width=12,
                background=config.window_background_color2, foreground=config.color_black, anchor=tk.CENTER)
            warehouse_management_label.grid(row=3, column=1, columnspan=1, rowspan=1, padx=2, pady=3, sticky=tk.E)
            warehouse_management_frame.bind("<Button-1>", lambda event: warehouse_management_frame_click())
            warehouse_management_image.bind("<Button-1>", lambda event: warehouse_management_frame_click())
            warehouse_management_label.bind("<Button-1>", lambda event: warehouse_management_frame_click())

            # summary_report_frame = tk.Frame(left_frame_inside, background=config.window_background_color2, cursor="hand2")
            # summary_report_frame.pack(fill=tk.Y, padx=0, pady=10, ipadx=10)
            # summary_report_image = tk.Label(
            #     summary_report_frame, image=summary_report_icon,
            #     background=config.window_background_color2, width=70, height=70)
            # summary_report_image.grid(row=5, column=0, columnspan=1, rowspan=1, padx=2, pady=3)
            # summary_report_label = tk.Label(
            #     summary_report_frame, text="จัดการรายงาน\nสรุปยอดขาย",
            #     font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), width=12,
            #     background=config.window_background_color2, foreground=config.color_black, anchor=tk.CENTER)
            # summary_report_label.grid(row=5, column=1, columnspan=1, rowspan=1, padx=2, pady=3, sticky=tk.E)
            # summary_report_frame.bind("<Button-1>", lambda event: summary_report_frame_click())
            # summary_report_image.bind("<Button-1>", lambda event: summary_report_frame_click())
            # summary_report_label.bind("<Button-1>", lambda event: summary_report_frame_click())

            # order_product_frame = tk.Frame(left_frame_inside, background=config.window_background_color2, cursor="hand2")
            # order_product_frame.pack(fill=tk.Y, padx=0, pady=0, ipadx=10)
            # order_product_image = tk.Label(
            #     order_product_frame, image=order_product_icon,
            #     background=config.window_background_color2, width=70, height=70)
            # order_product_image.grid(row=6, column=0, columnspan=1, rowspan=1, padx=2, pady=3)
            # order_product_label = tk.Label(
            #     order_product_frame, text="จัดการสินค้า\nรายการคำสั่งซื้อ",
            #     font=tkfont.Font(family='FC Lamoon', size=18, weight='bold'), width=12,
            #     background=config.window_background_color2, foreground=config.color_black, anchor=tk.CENTER)
            # order_product_label.grid(row=6, column=1, columnspan=1, rowspan=1, padx=2, pady=3, sticky=tk.E)
            # order_product_frame.bind("<Button-1>", lambda event: order_product_frame_click())
            # order_product_image.bind("<Button-1>", lambda event: order_product_frame_click())
            # order_product_label.bind("<Button-1>", lambda event: order_product_frame_click())
            selling_product_frame_click()   # default selected menu
        elif user_data[0][4] == '2':
            selling_product_frame_click()

    def logout_button_click():
        if alert_message.ask_logout():
            menu_frame.destroy()
            import authentication
            authentication_frame = authentication.authentication_frame(root)
            authentication_frame.place(x=0, y=0, width=config.window_width, height=config.window_height)

    def refresh_menu_frame():
        main_frame.destroy()
        create_frame()
        top_frame_content()
        left_frame_content()

    create_frame()
    top_frame_content()
    left_frame_content()
    root.bind("<F5>", lambda event: refresh_menu_frame())
    root.bind('<Escape>', lambda event: logout_button_click())
    root.bind('<Alt-F4>', lambda event: logout_button_click())
    return menu_frame

if __name__ == '__main__':
    import main
    main.App()