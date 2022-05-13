import tkinter as tk
import pyglet
import config
import alert_message

pyglet.font.add_file('assets\\backend\\fonts\\FC Lamoon Regular ver 1.00.ttf')
pyglet.font.add_file('assets\\backend\\fonts\\FC Lamoon Bold ver 1.00.ttf')

def App():
    # Function create main window
    def create_window():
        # Create window
        root = tk.Tk()
        root.title(config.window_title)
        window_x_pos = (root.winfo_screenwidth() // 2) - (config.window_width // 2)
        window_y_pos = (root.winfo_screenheight() // 2) - (config.window_height // 2)
        root.geometry('{}x{}+{}+{}'.format(config.window_width, config.window_height, window_x_pos, window_y_pos))
        root.resizable(config.window_resizeable, config.window_resizeable)
        root.configure(background=config.window_background_color)
        root.iconbitmap(config.window_logo)
        return root

    # Call function authentication
    def authentication():
        import authentication
        authentication_frame = authentication.authentication_frame(root)
        authentication_frame.place(x=0, y=0, width=config.window_width, height=config.window_height)

    root = create_window()  # Create window
    authentication()        # Call function authentication
    root.bind('<F11>', lambda event: alert_message.fullscreen_error())  # Fullscreen
    root.bind('<F1>', lambda event: alert_message.Hmmm())  # Help

    test_font = ("FC Lamoon", 18)
    root.option_add('*TCombobox*Listbox.font', test_font)

    root.mainloop()         # Start main loop

# Call main function
if __name__ == '__main__':
    App()