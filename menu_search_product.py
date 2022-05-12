import tkinter as tk
import tkinter.ttk as ttk
import config

def search_product(display, user_data):
    search_product_frame = tk.Frame(display, bg=config.color_default)

    main_frame = tk.Frame(search_product_frame, bg=config.color_default)
    main_frame.pack(fill=tk.BOTH, expand=1, padx=15, pady=15)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('AngsanaUPC', 15, 'bold'))
    style.configure("Treeview", font=('AngsanaUPC', 15), rowheight=25)
    style.map('Treeview', background=[('selected', config.color_list_selected)])

    product_list_tree = ttk.Treeview(
        main_frame, padding=5, selectmode='extended',
        columns=('#1', '#2', '#3', '#4', '#5', '#6'), height=22, show='headings')
    product_list_tree.pack(padx=5, pady=0)

    product_list_tree.tag_configure("even", background=config.color_list_even)
    product_list_tree.tag_configure("odd", background=config.color_list_odd)

    product_list_tree.heading('#0', text='')
    product_list_tree.heading('#1', text='ลำดับ')
    product_list_tree.heading('#2', text='ประเภท')
    product_list_tree.heading('#3', text='ชื่อสินค้า')
    product_list_tree.heading('#4', text='ปริมาณ')
    product_list_tree.heading('#5', text='จำนวนคงเหลือ')
    product_list_tree.heading('#6', text='ราคาขาย')

    product_list_tree.column('#0', width=0)
    product_list_tree.column('#1', width=50, anchor=tk.CENTER, stretch=True)
    product_list_tree.column('#2', width=160, anchor=tk.W, stretch=True)
    product_list_tree.column('#3', width=500, anchor=tk.W, stretch=True)
    product_list_tree.column('#4', width=100, anchor=tk.W, stretch=True)
    product_list_tree.column('#5', width=100, anchor=tk.W, stretch=True)
    product_list_tree.column('#6', width=90, anchor=tk.E, stretch=True)

    import connect_database
    sql = "SELECT * FROM product_storage ORDER by product_name ASC"
    product_list = connect_database.database_execute(sql)

    for i, product_record in enumerate(product_list):
            if i%2 == 0:
                if len(product_list) < 10:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.1d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                elif len(product_list) < 100:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.2d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                elif len(product_list) < 1000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.3d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                elif len(product_list) < 10000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.4d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                elif len(product_list) < 100000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%.5d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                else:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('even',),
                    values=("%d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
            else:
                if len(product_list) < 10:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.1d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                elif len(product_list) < 100:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.2d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                elif len(product_list) < 1000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.3d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                elif len(product_list) < 10000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.4d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                elif len(product_list) < 100000:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%.5d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))
                else:
                    product_list_tree.insert(parent='', index='end', text=product_record[0], tags=('odd',),
                    values=("%d" %(i+1), product_record[3], product_record[4], str(product_record[5]) + " " + product_record[6], str(product_record[7]) + " " + product_record[8], "%.2f บาท" %product_record[9]))


    return search_product_frame

if __name__ == '__main__':
    import main
    main.App()