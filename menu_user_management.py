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

        # import connect_database
        # sql = "SELECT * FROM user_accounts"
        # user_account_list = connect_database.database_execute(sql)

        # print(user_account_list)

        # top_frame = tk.Frame(show_user_account_frame, bg=config.color_green)
        # top_frame.place(x=0, y=0, width=1037, height=50)

        # add_new_user_button = tk.Button(
        #     top_frame, text=" ออกจากระบบ ", cursor="hand2", image=logout_icon, compound=tk.LEFT,
        #     activebackground=config.color_red, activeforeground=config.color_white,
        #     font=tkfont.Font(family='FC Lamoon', size=14, weight='bold'),
        #     background=config.color_red, foreground=config.color_white,
        #     command=lambda: logout_button_click())
        # add_new_user_button.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5, pady=0, sticky=tk.E)

    def show_user_account_detail():
        pass

    create_frame()
    show_user_account()
    return user_management_frame

if __name__ == '__main__':
    import main
    main.App()