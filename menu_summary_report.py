import tkinter as tk
import config

def summary_report(display, user_data):
    summary_report_frame = tk.Frame(display, bg=config.color_default)

    # ! IMPORTANT: Create a new frame over order_product_frame by pack grid or place.
    # ! IMPORTANT: And write everything on frame you create.

    test_label = tk.Label(summary_report_frame, text="Test", bg=config.color_default)
    test_label.pack(expand=True, fill="both")

    return summary_report_frame

if __name__ == '__main__':
    import main
    main.App()