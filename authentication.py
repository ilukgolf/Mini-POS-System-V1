import tkinter as tk
import tkinter.font as tkfont
import config
import alert_message

# TODO: Call function to change password

def authentication_frame(root):
    root.unbind("<F5>")     # Unbind F5 key from menu (refresh)
    auth_frame = tk.Frame(root, background=config.window_background_color)

    global login_icon
    login_icon = tk.PhotoImage(file="assets\\backend\\images\\login_icon.png")

    def create_frame():
        global main_frame, top_frame, center_frame, bottom_frame

        # main frame for authentication
        main_frame = tk.Frame(auth_frame, background=config.window_background_color)
        main_frame.pack(expand=True)

        # top frame for authentication
        top_frame = tk.Frame(main_frame, background=config.window_background_color)
        top_frame.pack(expand=True)

        # center frame for authentication
        center_frame = tk.Frame(main_frame, background=config.window_background_color)
        center_frame.pack(expand=True, padx=0, pady=50)

        # bottom frame for authentication
        bottom_frame = tk.Frame(main_frame, background=config.window_background_color)
        bottom_frame.pack(expand=True)

    def top_frame_content():
        global title_head_frame

        # title label in top frame
        title_head_frame = tk.Frame(top_frame, background=config.window_background_color)
        title_head_frame.pack(expand=True)

        title_label_1 = tk.Label(
            title_head_frame, text="Mini", font=tkfont.Font(family='FC Lamoon', size=40, weight='normal'),
            background=config.window_background_color, foreground=config.color_default)
        title_label_1.grid(row=0, column=0, padx=5, pady=3, sticky=tk.S)

        title_label_2 = tk.Label(
            title_head_frame, text="POS", font=tkfont.Font(family='FC Lamoon', size=50, weight='bold', underline=1),
            background=config.window_background_color, foreground=config.color_highlight)
        title_label_2.grid(row=0, column=1, padx=5, pady=0, sticky=tk.S)

        title_label_3 = tk.Label(
            title_head_frame, text="System", font=tkfont.Font(family='FC Lamoon', size=40, weight='normal'),
            background=config.window_background_color, foreground=config.color_default)
        title_label_3.grid(row=0, column=2, padx=5, pady=3, sticky=tk.S)

        title_version = tk.Label(
            title_head_frame, text="(BETA 1.0)", font=tkfont.Font(family='FC Lamoon', size=22, weight='normal'),
            background=config.window_background_color, foreground=config.color_default)
        title_version.grid(row=0, column=3, padx=5, pady=9, sticky=tk.S)
        title_version.bind('<Button-1>', lambda event: alert_message.version_info())

        title_description = tk.Label(
            top_frame, text="(Final project for CS311 S.127F 2/21 Bangkok university)",
            font=tkfont.Font(family='FC Lamoon', size=18, weight='normal'),
            background=config.window_background_color, foreground=config.color_default)
        title_description.pack(expand=True)

    def center_frame_content():
        global center_frame_top, center_frame_bottom, center_frame_center, center_frame_center_inside, center_frame_bottom
        global username_entry, password_entry, username_input, password_input, login_button, forget_password_label
        username_input, password_input = tk.StringVar(), tk.StringVar()
        # username_input.set("jirawat.bunm")
        # password_input.set("password")

        center_frame['bg'] = config.window_background_color2

        center_frame_top = tk.Frame(center_frame, background=config.window_background_color2)
        center_frame_top.pack(expand=True, padx=60, pady=20)

        center_frame_center = tk.Frame(center_frame, background=config.window_background_color2)
        center_frame_center.pack(expand=True, padx=60, pady=0)
        center_frame_center_inside = tk.Frame(center_frame_center, background=config.window_background_color2)
        center_frame_center_inside.pack(expand=True, padx=0, pady=0)

        center_frame_bottom = tk.Frame(center_frame, background=config.window_background_color2)
        center_frame_bottom.pack(expand=True, padx=60, pady=20)

        # logo and title in center frame
        logo_label = tk.Label(center_frame_top, image=login_icon, background=config.window_background_color2)
        logo_label.grid(row=0, column=0, padx=10, pady=0, sticky=tk.NSEW)
        login_label = tk.Label(center_frame_top, text="กรุณาเข้าสู่ระบบ", font=tkfont.Font(family='FC Lamoon', size=26, weight='bold'),
                                 background=config.window_background_color2, foreground=config.color_default)
        login_label.grid(row=1, column=0, padx=10, pady=0, sticky=tk.NSEW)

        # username and password in center frame
        username_label = tk.Label(
            center_frame_center_inside, text="ชื่อผู้ใช้", font=tkfont.Font(family='FC Lamoon', size=22, weight='normal'),
            background=config.window_background_color2, foreground=config.color_default)
        username_label.grid(row=0, column=0, padx=0, pady=2, sticky=tk.W)
        username_entry = tk.Entry(
            center_frame_center_inside, font=tkfont.Font(family='FC Lamoon', size=22, weight='normal'),
            background=config.color_white, foreground=config.color_black, textvariable=username_input)
        username_entry.grid(row=1, column=0, padx=0, pady=2, sticky=tk.NSEW)
        username_entry.icursor(tk.END)

        password_label = tk.Label(
            center_frame_center_inside, text="รหัสผ่าน", font=tkfont.Font(family='FC Lamoon', size=22, weight='normal'),
            background=config.window_background_color2, foreground=config.color_default)
        password_label.grid(row=2, column=0, padx=0, pady=2, sticky=tk.W)
        password_entry = tk.Entry(
            center_frame_center_inside, font=tkfont.Font(family='FC Lamoon', size=22, weight='normal'),
            show="*", background=config.color_white, foreground=config.color_black, textvariable=password_input)
        password_entry.grid(row=3, column=0, padx=0, pady=2, sticky=tk.NSEW)
        password_entry.icursor(tk.END)

        forget_password_label = tk.Label(
            center_frame_center_inside, text="ลืมรหัสผ่าน ?", font=tkfont.Font(family='FC Lamoon', size=18, weight='normal'),
            background=config.window_background_color2, foreground=config.color_default, cursor="hand2")
        forget_password_label.grid(row=4, column=0, padx=0, pady=5, sticky=tk.E)
        forget_password_label.bind("<Button-1>", lambda event: forget_password())

        # login button in center frame
        login_button = tk.Button(
            center_frame_bottom, text=" เข้าสู่ระบบ ", font=tkfont.Font(family='FC Lamoon', size=22, weight='bold'),
            background=config.color_highlight, foreground=config.color_default, relief="raised", cursor="hand2",
            activebackground=config.color_highlight, activeforeground=config.color_default,
            command=lambda: login_button_click(username_entry.get(), password_entry.get()))
        login_button.pack(padx=0, pady=0)

    def bottom_frame_content():
        credits_label = tk.Label(
            bottom_frame,
            text="( Created by:  JIRAWAT BUNMARAKSASAKUL 1630708046  |  PORNNARAI JUMROON 1630708475  |  NAWAPON KLIBBURIN 6620900016 )",
            font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
            background=config.window_background_color, foreground=config.color_default)
        credits_label.pack(expand=True)

    def login_button_click(username, password, event=None):
        if len(username) == 0 and len(password) == 0:
            alert_message.login_error(1)
            username_entry.focus_force()
        elif len(username) == 0:
            alert_message.login_error(2)
            username_entry.focus_force()
        elif len(password) == 0:
            alert_message.login_error(3)
            password_entry.focus_force()
        else:
            import connect_database
            sql = "SELECT * FROM user_accounts WHERE user_username = '%s'" % (username)
            user_select_info = connect_database.database_execute(sql)
            if len(user_select_info) > 1:
                alert_message.login_error(0, len(user_select_info))
                username_input.set("")
                password_input.set("")
                username_entry.focus_force()
            elif len(user_select_info) == 0:
                alert_message.login_error(4)
                username_entry.focus_force()
                username_entry.select_range(0, tk.END)
                username_entry.icursor(tk.END)
                password_input.set("")
            else:
                import password_check
                login_status = password_check.password_decrypt(username, password, user_select_info[0])
                if login_status == 1:
                    alert_message.login_success(user_select_info[0][5])
                    auth_frame.destroy()
                    import menu
                    menu_frame = menu.main_menu_frame(root, user_data = user_select_info[0])
                    menu_frame.place(x=0, y=0, width=config.window_width, height=config.window_height)
                elif login_status == 2:
                    # TODO: Call function to change password
                    pass
                elif login_status == 3:
                    alert_message.login_error(5)
                    username_entry.focus_force()
                    username_entry.select_range(0, tk.END)
                    username_entry.icursor(tk.END)
                    password_input.set("")
                else:
                    alert_message.login_error(4)
                    username_entry.focus_force()
                    username_entry.select_range(0, tk.END)
                    username_entry.icursor(tk.END)
                    password_input.set("")

    def forget_password(event=None):
        alert_message.forgot_password()
        username_input.set("")
        password_input.set("")
        username_entry.focus_force()
        # TODO: (future) Update new feature to forget username and password.

    def ask_quit(event=None):
        if alert_message.ask_quit():
            root.destroy()

    create_frame()
    top_frame_content()
    center_frame_content()
    bottom_frame_content()
    username_entry.focus_force()
    username_entry.bind("<Return>", lambda event: login_button_click(username_entry.get(), password_entry.get()))
    password_entry.bind("<Return>", lambda event: login_button_click(username_entry.get(), password_entry.get()))
    login_button.bind("<Return>", lambda event: login_button_click(username_entry.get(), password_entry.get()))
    root.bind("<Escape>", ask_quit)
    root.bind('<Alt-F4>', ask_quit)
    return auth_frame

if __name__ == '__main__':
    import main
    main.App()