import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import alert_message
import config

# TODO: แก้ไขการรับสินค้าโโยใช้ชื่อสินค้า ให้เหือนกันการใช้รหัสสินค้า
# TODO: ทำหน้าสรุปรายการสินค้า รับเงิน ทอนเงิน และบันทึกเข้าฐานข้อมูล
# TODO: ใบเสร็จรับเงิน ?

def selling_product(display, user_data):
    selling_product_frame = tk.Frame(display, bg=config.color_default)

    # create main frame for left and right side.
    # create left side frame for show all product list and product detail.
    # create right side frame for create selling product.
    #* DONE
    def create_frame():
        global main_frame, left_frame, right_frame
        main_frame = tk.Frame(selling_product_frame, bg=config.color_default)
        main_frame.place(x=0, y=0, width=1047, height=620)

        left_frame = tk.Frame(main_frame, bg=config.color_default)
        left_frame.place(x=0, y=0, width=540, height=620)

        right_frame = tk.Frame(main_frame, bg=config.color_default)
        right_frame.place(x=540, y=0, width=507, height=620)

        # right_frame_inside = tk.Frame(main_frame, bg=config.color_default)
        # right_frame_inside.place(x=540, y=0, width=507, height=620)

        # center_line()

    #* DONE
    def center_line():
        center_line = tk.Frame(main_frame, bg=config.color_default_dark)
        center_line.place(x=539, y=10, width=3, height=600)

    # show all product list and product detail.
    #* DONE
    def show_product_list():
        import connect_database
        sql = "SELECT * FROM product_storage ORDER BY product_name ASC"
        product_list = connect_database.database_execute(sql)
        product_list_total_amount.set("" + str(len(product_list)))

        product_list_title = tk.Label(
            left_frame, text="รายการสินค้าในคลังสินค้า",
            font=tkfont.Font(family='FC Lamoon', size=22, weight='bold'),
            background=config.color_default, foreground=config.color_black)
        product_list_title.pack(padx=0, pady=15, anchor=tk.CENTER)

        product_total_label = tk.Label(
            left_frame, text=f"รวมสินค้าทั้งหมด {product_list_total_amount.get()} รายการ (เรียงตามตัวอักษร)",
            font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
            background=config.color_default, foreground=config.color_black)
        product_total_label.pack(padx=15, pady=0, anchor=tk.W)

        global product_list_tree
        product_list_tree = ttk.Treeview(
            left_frame, padding=5, selectmode='extended',
            columns=('#1', '#2', '#3', '#4', '#5'), height=19, show='headings')
        product_list_tree.pack(padx=5, pady=0)

        product_list_tree.tag_configure("evenrow", background=config.color_list_even)
        product_list_tree.tag_configure("oddrow", background=config.color_list_odd)

        product_list_tree.heading('#0', text='')
        product_list_tree.heading('#1', text='ลำดับ')
        product_list_tree.heading('#2', text='รายการสินค้า')
        product_list_tree.heading('#3', text='ราคา')
        product_list_tree.heading('#4', text='คงเหลือ')
        product_list_tree.heading('#5', text='หน่วย')

        product_list_tree.column('#0', width=0)
        product_list_tree.column('#1', width=50, anchor=tk.CENTER, stretch=True)
        product_list_tree.column('#2', width=270, anchor=tk.W, stretch=True)
        product_list_tree.column('#3', width=60, anchor=tk.E, stretch=True)
        product_list_tree.column('#4', width=80, anchor=tk.CENTER, stretch=True)
        product_list_tree.column('#5', width=60, anchor=tk.W, stretch=True)

        product_list_tree.tag_configure("even", background=config.color_list_even)
        product_list_tree.tag_configure("odd", background=config.color_list_odd)

        product_list_tree.delete(*product_list_tree.get_children())
        for i, product_record in enumerate(product_list):
            if i%2 == 0:
                if len(product_list) < 10:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.1d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                elif len(product_list) < 100:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.2d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                elif len(product_list) < 1000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.3d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                elif len(product_list) < 10000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.4d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                elif len(product_list) < 100000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.5d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                else:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
            else:
                if len(product_list) < 10:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.1d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                elif len(product_list) < 100:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.2d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                elif len(product_list) < 1000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.3d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                elif len(product_list) < 10000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.4d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                elif len(product_list) < 100000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.5d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))
                else:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%d" %(i+1), product_record[4] + " ("+str(product_record[5]) + " " + product_record[6]+")", "%.2f" %product_record[9], product_record[7], product_record[8]))

    # when click record in product list, add product to cart.
    #* DONE
    def product_list_selected():
        product_record = product_list_tree.item(product_list_tree.focus())
        product_list_tree.selection_remove(product_list_tree.focus())
        add_to_cart(product_record['text'])

    # show selling product list
    # add more product to cart, edit amount, delete product from cart
    def show_selling_product_list():
        global right_frame_inside
        right_frame_inside = tk.Frame(main_frame, bg=config.color_default)
        right_frame_inside.place(x=540, y=0, width=507, height=620)

        product_selling_title = tk.Label(
            right_frame_inside, text="ขายสินค้า",
            font=tkfont.Font(family='FC Lamoon', size=22, weight='bold'),
            background=config.color_default, foreground=config.color_black)
        product_selling_title.pack(padx=0, pady=15, anchor=tk.CENTER)

        product_selling_total_label = tk.Label(
            right_frame_inside, text=f"รวมสินค้าทั้งหมด {selling_list_total_amount.get()} รายการ",
            font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
            background=config.color_default, foreground=config.color_black)
        product_selling_total_label.pack(padx=15, pady=0, anchor=tk.W)

        global product_selling_list_tree
        product_selling_list_tree = ttk.Treeview(
            right_frame_inside, padding=5, selectmode='extended',
            columns=('#1', '#2', '#3', '#4'), height=6, show='headings')
        product_selling_list_tree.pack(padx=5, pady=0)
        product_selling_list_tree.bind('<Double-1>', lambda event: selling_product_selected())

        product_selling_list_tree.tag_configure("even", background=config.color_list_even)
        product_selling_list_tree.tag_configure("odd", background=config.color_list_odd)

        product_selling_list_tree.heading('#0', text='')
        product_selling_list_tree.heading('#1', text='ลำดับ')
        product_selling_list_tree.heading('#2', text='รายการสินค้า')
        product_selling_list_tree.heading('#3', text='จำนวน')
        product_selling_list_tree.heading('#4', text='ราคา')

        product_selling_list_tree.column('#0', width=0)
        product_selling_list_tree.column('#1', width=50, anchor=tk.CENTER, stretch=True)
        product_selling_list_tree.column('#2', width=300, anchor=tk.W, stretch=True)
        product_selling_list_tree.column('#3', width=70, anchor=tk.CENTER, stretch=True)
        product_selling_list_tree.column('#4', width=60, anchor=tk.E, stretch=True)

        search_product_to_add_sell_frame = tk.Frame(right_frame_inside, background=config.color_default)
        search_product_to_add_sell_frame.pack(padx=7, pady=5, anchor=tk.NW)

        product_search_label = tk.Label(
            search_product_to_add_sell_frame, text="ค้นหาด้วยรหัสสินค้า : ",
            font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
            background=config.color_default, foreground=config.color_black)
        product_search_label.grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)

        global product_search_entry, product_search_button
        product_search_entry = tk.Entry(
            search_product_to_add_sell_frame, textvariable=product_selling_search_var,
            font=tkfont.Font(family='FC Lamoon', size=18, weight='normal'),
            background=config.color_white, foreground=config.color_black, relief='groove', width=20)
        product_search_entry.grid(row=0, column=1, padx=0, pady=0, ipadx=0, ipady=3, sticky=tk.W)
        product_search_entry.focus_force()

        product_search_button = tk.Button(
            search_product_to_add_sell_frame, text=" เพิ่มลงตะกร้า ",
            cursor="hand2", image=add_to_cart_icon, compound=tk.LEFT,
            activebackground=config.color_green, activeforeground=config.color_white,
            font=tkfont.Font(family='FC Lamoon', size=14, weight='bold'),
            background=config.color_green, foreground=config.color_white,
            command=lambda: add_to_cart(product_selling_search_var.get()))
        product_search_button.grid(row=0, column=2, padx=10, pady=0, sticky=tk.W)

        product_edit_amount_frame = tk.Frame(right_frame_inside, background=config.color_default)
        product_edit_amount_frame.place(x=0, y=330, width=507, height=100)

        if len(config.cart) > 0:
            global product_edit_amount_frame_inside
            product_edit_amount_frame_inside = tk.Frame(product_edit_amount_frame, background=config.color_default)
            product_edit_amount_frame_inside.place(x=0, y=0, width=507, height=140)

            show_edit_product_id_label = tk.Label(
                product_edit_amount_frame_inside, text="แก้ไขรายการ [%s]" %(edit_product_by_id_var.get()),
                font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
                background=config.color_default, foreground=config.color_black, width=61, anchor=tk.W)
            show_edit_product_id_label.grid(row=0, column=0, columnspan=3, padx=5, pady=0, sticky=tk.W)

            show_edit_product_name_label = tk.Label(
                product_edit_amount_frame_inside, text="ชื่อสินค้า : ",
                font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
                background=config.color_default, foreground=config.color_black, width=8, anchor=tk.W)
            show_edit_product_name_label.grid(row=1, column=0, columnspan=1, padx=5, pady=0, sticky=tk.W)

            show_edit_product_name_label2 = tk.Label(
                product_edit_amount_frame_inside, text="%s" %edit_product_by_name_var.get(),
                font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
                background=config.color_default, foreground=config.color_black, width=50, anchor=tk.W)
            show_edit_product_name_label2.grid(row=1, column=1, columnspan=2, padx=0, pady=0, sticky=tk.W)

            show_edit_product_amount_label = tk.Label(
                product_edit_amount_frame_inside, text="จำนวน : ",
                font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
                background=config.color_default, foreground=config.color_black,  width=8, anchor=tk.W)
            show_edit_product_amount_label.grid(row=2, column=0, columnspan=1, padx=5, pady=0, sticky=tk.W)

            global show_edit_product_amount_entry
            show_edit_product_amount_entry = tk.Entry(
                product_edit_amount_frame_inside, textvariable=new_product_amount_var,
                font=tkfont.Font(family='FC Lamoon', size=16, weight='normal'),
                background=config.color_white, foreground=config.color_black, relief='groove', width=5)
            show_edit_product_amount_entry.grid(row=2, column=1, columnspan=1, padx=0, pady=0, sticky=tk.W)

            global edit_button
            edit_button = tk.Button(
                product_edit_amount_frame_inside, text="แก้ไข",
                cursor="hand2", anchor=tk.W,
                activebackground=config.color_green, activeforeground=config.color_white,
                font=tkfont.Font(family='FC Lamoon', size=14, weight='bold'),
                background=config.color_green, foreground=config.color_white,
                command=lambda: update_cart(edit_product_by_id_var.get(), new_product_amount_var.get()))
            edit_button.grid(row=2, column=1, columnspan=1, padx=70, pady=0, sticky=tk.W)
        else:
            try:
                product_edit_amount_frame_inside.destroy()
            except:
                pass

        summary_price_frame = tk.Frame(right_frame_inside, background=config.color_default)
        summary_price_frame.place(x=0, y=470, width=507, height=135)

        global total_price
        total_price = 0
        if len(config.cart) > 0:
            for idx, (id, name, amount, price) in enumerate(config.cart):
                total_price += float(price) * float(amount)
        summary_price_var.set('%.2f' %total_price)

        price_left_frame = tk.Frame(summary_price_frame, background=config.color_default)
        price_left_frame.grid(row=0, column=0, padx=10, pady=0, sticky=tk.W)

        price_right_frame = tk.Frame(summary_price_frame, background=config.color_default)
        price_right_frame.grid(row=0, column=1, padx=100, pady=0, sticky=tk.E)

        total_price_label = tk.Label(
            price_left_frame, text="ราคารวม : ",
            font=tkfont.Font(family='FC Lamoon', size=22, weight='bold'),
            background=config.color_default, foreground=config.color_black, width=8, anchor=tk.W)
        total_price_label.grid(row=0, column=0, padx=5, pady=0, sticky=tk.W)

        total_price_entry = tk.Entry(
            price_left_frame, textvariable="%s" %(summary_price_var), state=tk.DISABLED,
            font=tkfont.Font(family='FC Lamoon', size=50, weight='normal'), justify=tk.RIGHT,
            background=config.color_white, foreground=config.color_black, relief='groove', width=7)
        total_price_entry.grid(row=1, column=0, padx=0, pady=0, ipadx=0, ipady=15, sticky=tk.S)

        cash_received_label = tk.Label(
            price_right_frame, text="รับเงิน : ",
            font=tkfont.Font(family='FC Lamoon', size=22, weight='bold'),
            background=config.color_default, foreground=config.color_black, width=8, anchor=tk.W)
        cash_received_label.grid(row=0, column=0, columnspan=2, padx=5, pady=0, sticky=tk.W)

        cash_received_entry = tk.Entry(
            price_right_frame, textvariable="%s" %(cash_received_var),
            font=tkfont.Font(family='FC Lamoon', size=30, weight='normal'), justify=tk.RIGHT,
            background=config.color_white, foreground=config.color_black, relief='groove', width=8)
        cash_received_entry.grid(row=1, column=0, columnspan=2, padx=0, pady=0, ipadx=0, ipady=5, sticky=tk.S)

        cancel_button = tk.Button(
            price_right_frame, text="ยกเลิก",
            cursor="hand2", anchor=tk.CENTER,
            activebackground=config.color_red, activeforeground=config.color_white,
            font=tkfont.Font(family='FC Lamoon', size=16, weight='bold'),
            background=config.color_red, foreground=config.color_white,
            command=lambda: cancel_order())
        cancel_button.grid(row=2, column=0, columnspan=1, padx=5, pady=5, ipadx=8, ipady=1, sticky=tk.NSEW)

        confirm_button = tk.Button(
            price_right_frame, text="บันทึก",
            cursor="hand2", anchor=tk.CENTER,
            activebackground=config.color_green, activeforeground=config.color_white,
            font=tkfont.Font(family='FC Lamoon', size=16, weight='bold'),
            background=config.color_green, foreground=config.color_white,
            command=lambda: confirm_order())
        confirm_button.grid(row=2, column=1, columnspan=1, padx=5, pady=5, ipadx=8, ipady=1, sticky=tk.NSEW)

        product_search_entry.bind('<Return>', lambda event: add_to_cart(product_selling_search_var.get()))
        product_search_button.bind('<Return>', lambda event: add_to_cart(product_selling_search_var.get()))

    def cancel_order():
        try:
            product_edit_amount_frame_inside.destroy()
        except:
            pass
        config.cart = []
        total_price = 0
        product_selling_list_tree.delete(*product_selling_list_tree.get_children())
        summary_price_var.set('%.2f' %total_price)
        cash_received_var.set('')
        product_search_entry.focus_force()

    def confirm_order():
        if len(config.cart) == 0 or total_price == 0:
            alert_message.summary_selling_error()
        else:
            if cash_received_var.get() == '':
                alert_message.cash_received_error(1)
            elif cash_received_var.get().isdigit() == False:
                alert_message.cash_received_error(2)
            elif float(cash_received_var.get()) < total_price:
                alert_message.cash_received_error(3)
            else:
                question = alert_message.save_selling(float(cash_received_var.get()) - total_price)
                if question == True:
                    confirm_save_selling()

    def confirm_save_selling():
        import connect_database
        import datetime
        import sqlite3
        day = datetime.datetime.now().strftime("%d")
        month = datetime.datetime.now().strftime("%m")
        year = datetime.datetime.now().strftime("%y")
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        second = datetime.datetime.now().strftime("%S")
        sell_id = "1" + year + month + day + hour + minute + second

        global conn, cursor
        conn = sqlite3.connect('assets\\backend\\database\\minipos.db')
        cursor = conn.cursor()

        for idx, (id, name, amount, price) in enumerate(config.cart):
            sql = '''INSERT INTO selling_history
            (selling_id, selling_product_id, selling_product_amount, selling_product_price)
            VALUES (?, ?, ?, ?)'''
            cursor.execute(sql, (sell_id, config.cart[idx][0], config.cart[idx][3], config.cart[idx][2]))
            conn.commit()

        sell_date = day + "/" + month + "/" + datetime.datetime.now().strftime("%Y") + " " + hour + ":" + minute + ":" + second

        sql2 = '''INSERT INTO selling_payment
        (selling_id, selling_date_create, selling_user_id, selling_total_price, selling_cash_received, selling_cash_change)
        VALUES (?, ?, ?, ?, ?, ?)'''
        cursor.execute(sql2, (sell_id, sell_date, user_data[0], float(total_price), float(cash_received_var.get()), float(cash_received_var.get()) - float(total_price)))
        conn.commit()
        conn.close()
        cancel_order()


    # When the user clicks the "เพิ่มลงตะกร้า" button, the product is added to the cart.
    # Or when the user selects a product from the list, the product is added to the cart.
    def add_to_cart(product_id):
        product_search_entry.focus_force()
        product_selling_search_var.set('')

        if product_id == '':    # when insert empty string
            alert_message.product_search_input_empty()
        else:   # when insert product id (or product name) to search
            if product_id.isdigit() == False:   # IF product_id is a character.
                import connect_database
                sql = f"SELECT * FROM product_storage WHERE product_name LIKE '%{product_id}%'"
                product_data = connect_database.database_execute(sql)

                if product_data == []:  # when product not found by product name
                    alert_message.product_not_found()
                elif len(product_data) > 1:
                    alert_message.beep()
                    product_check_insert = 0
                    for i in range(len(config.cart)):
                            if product_data[0][0][0] == config.cart[i][0]:
                                update_cart(product_data[0][0][0])
                            else:
                                product_check_insert += 1
                    if product_check_insert == len(config.cart):
                        insert_product_to_cart(product_data[0][0])
                else:
                    alert_message.beep()
                    product_check_insert = 0
                    for i in range(len(config.cart)):
                            if product_data[0][0] == config.cart[i][0]:
                                update_cart(product_data[0][0])
                            else:
                                product_check_insert += 1
                    if product_check_insert == len(config.cart):
                        insert_product_to_cart(product_data[0])
            else:   # IF product_id is a number.
                import connect_database
                sql = f"SELECT * FROM product_storage WHERE product_id = '{product_id}'"
                product_data = connect_database.database_execute(sql)

                if product_data == []:  # when product not found by product id
                    alert_message.product_not_found()
                else:  # when product found by product id
                    product_check_insert = 0
                    alert_message.beep()
                    if len(config.cart) < 1:
                        insert_product_to_cart(product_data[0])
                    else:
                        for i in range(len(config.cart)):
                            if product_data[0][0] == config.cart[i][0]:
                                update_cart(product_data[0][0])
                            else:
                                product_check_insert += 1
                        if product_check_insert == len(config.cart):
                            insert_product_to_cart(product_data[0])
        product_selling_list_tree.yview_scroll(1, tk.UNITS)

    def refresh_product_selling_list():
        right_frame_inside.destroy()
        selling_list_total_amount.set(len(config.cart))
        show_selling_product_list()
        center_line()
        product_selling_list_tree.delete(*product_selling_list_tree.get_children())
        if len(config.cart) > 0:
            for i in range(len(config.cart)):
                if i%2 == 0:
                    product_selling_list_tree.insert('', 'end', text=config.cart[i][0], tags=('even',),
                    values=("%d" % (i+1), config.cart[i][1], config.cart[i][3],  "%.2f" %(config.cart[i][2] * config.cart[i][3])))
                else:
                    product_selling_list_tree.insert('', 'end', text=config.cart[i][0], tags=('odd',),
                    values=("%d" % (i+1), config.cart[i][1], config.cart[i][3],  "%.2f" %(config.cart[i][2] * config.cart[i][3])))

    def insert_product_to_cart(product_data):   # receive product data to insert to cart
        pd_add_id = product_data[0]
        pd_add_name = product_data[4]+' ('+str(product_data[5])+' '+product_data[6]+')'
        pd_add_price = product_data[9]
        pd_add_amount = 1
        config.cart.append([pd_add_id, pd_add_name, pd_add_price, pd_add_amount])
        set_edit_product_amount("set", pd_add_id)
        # refresh_product_selling_list()

    def update_cart(product_id, amount = None):   # receive product id to update amount in cart
        if amount == None:
            for idx, (id, name, sell_price, amount) in enumerate(config.cart):
                if id == product_id:
                    config.cart[idx][3] += 1
        else:
            if amount.isdigit() == False:
                alert_message.edit_amount_fail()
                for idx, (id, name, sell_price, amount) in enumerate(config.cart):
                        if id == product_id:
                            new_product_amount_var.set(config.cart[idx][3])
            elif amount.isdigit() == True:
                if int(new_product_amount_var.get()) == 0:
                    question = alert_message.ask_remove_product()
                    if question == True:
                        for idx, (id, name, sell_price, amount) in enumerate(config.cart):
                            if id == product_id:
                                config.cart.pop(idx)
                        if len(config.cart) != 0:
                            edit_product_by_id_var.set(config.cart[len(config.cart)-1][0])
                            edit_product_by_name_var.set(config.cart[len(config.cart)-1][1])
                            new_product_amount_var.set(config.cart[len(config.cart)-1][3])

                else:
                    for idx, (id, name, sell_price, amount) in enumerate(config.cart):
                        if id == product_id:
                            config.cart[idx][3] = int(new_product_amount_var.get())
        set_edit_product_amount("unset", product_id)

    def selling_product_selected():
        product_selling_record = product_selling_list_tree.item(product_selling_list_tree.focus())
        product_selling_list_tree.selection_remove(product_selling_list_tree.focus())
        set_edit_product_amount("set", product_selling_record['text'])
        edit_button.bind('<Return>', lambda event: update_cart(edit_product_by_id_var.get(), new_product_amount_var.get()))

    def set_edit_product_amount(state, pd_id = None):
        if state == 'set':
            edit_product_by_id_var.set(pd_id)
            for idx, (id, name, sell_price, amount) in enumerate(config.cart):
                if id == pd_id:
                    edit_product_by_name_var.set(config.cart[idx][1])
                    new_product_amount_var.set(config.cart[idx][3])
        refresh_product_selling_list()

    global add_to_cart_icon
    add_to_cart_icon = tk.PhotoImage(file="assets\\backend\\images\\add_to_basket.png")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('AngsanaUPC', 15, 'bold'))
    style.configure("Treeview", font=('AngsanaUPC', 15), rowheight=25)
    style.map('Treeview', background=[('selected', config.color_list_selected)])

    product_list_total_amount = tk.StringVar()
    product_list_total_amount.set(0)
    selling_list_total_amount = tk.StringVar()
    selling_list_total_amount.set(0)
    product_selling_search_var = tk.StringVar()
    product_selling_search_var.set('')

    edit_product_by_id_var = tk.StringVar()
    edit_product_by_id_var.set('')
    edit_product_by_name_var = tk.StringVar()
    edit_product_by_name_var.set('')
    new_product_amount_var = tk.StringVar()
    new_product_amount_var.set('')

    if len(config.cart) != 0:
        edit_product_by_id_var.set(config.cart[len(config.cart)-1][0])
        edit_product_by_name_var.set(config.cart[len(config.cart)-1][1])
        new_product_amount_var.set(config.cart[len(config.cart)-1][3])

    summary_price_var = tk.StringVar()
    summary_price_var.set('')
    cash_received_var = tk.StringVar()
    cash_received_var.set('')

    create_frame()
    show_product_list()
    show_selling_product_list()
    refresh_product_selling_list()
    product_list_tree.bind('<Double-1>', lambda event: product_list_selected())
    product_selling_list_tree.bind('<Double-1>', lambda event: selling_product_selected())
    # product_search_entry.bind('<Return>', lambda event: add_to_cart(product_selling_search_var.get()))
    # product_search_button.bind('<Return>', lambda event: add_to_cart(product_selling_search_var.get()))
    return selling_product_frame

if __name__ == '__main__':
    import main
    main.App()