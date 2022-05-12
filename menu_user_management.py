import tkinter as tk
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
        show_user_account_frame = tk.Frame(main_frame, bg=config.color_red)
        show_user_account_frame.place(x=5, y=5, width=1037, height=610)

        import connect_database
        sql = "SELECT * FROM user_accounts"
        user_account_list = connect_database.database_execute(sql)

        print(user_account_list)

        top_frame = tk.Frame(show_user_account_frame, bg=config.color_default)
        top_frame.place(x=0, y=0, width=1037, height=50)

        add_new_user_button = tk.Button(
            top_frame, text=" เพิ่มบัญชีผู้ใช้ ", cursor="hand2", compound=tk.LEFT,
            activebackground=config.color_green, activeforeground=config.color_white,
            font=tkfont.Font(family='FC Lamoon', size=14, weight='bold'),
            background=config.color_green, foreground=config.color_white,
            command=lambda: add_new_user_account())
        add_new_user_button.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5, pady=5, sticky=tk.E)

    def show_user_account_detail():
        pass

    def add_new_user_account():
        pass

    create_frame()
    show_user_account()
    return user_management_frame

if __name__ == '__main__':
    import main
    main.App()