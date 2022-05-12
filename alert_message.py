import tkinter.messagebox as tkmsg
import winsound

def beep():
    winsound.Beep(400, 125)

def product_search_input_empty():
    tkmsg.showinfo("เพิ่มสินค้าลงตะกร้าไม่สำเร็จ", "กรุณากรอกรหัสสินค้าที่ต้องการเพิ่มลงตะกร้า")

def summary_selling_error():
    tkmsg.showinfo("บันทึกการขายไม่สำเร็จ", "ไม่มีสินค้าอยู่ในตะกร้า")

def cash_received_error(x):
    if x == 1:
        tkmsg.showinfo("บันทึกการขายไม่สำเร็จ", "กรุณากรอกจำนวนเงินที่รับมา")
    elif x == 2:
        tkmsg.showinfo("บันทึกการขายไม่สำเร็จ", "กรุณากรอกจำนวนเงินทีเป็นตัวเลขเท่านั้น")
    elif x == 3:
        tkmsg.showinfo("บันทึกการขายไม่สำเร็จ", "จำนวนเงินที่รับมาน้อยกว่าจำนวนที่ต้องชำระ")

def edit_amount_fail():
    tkmsg.showinfo("แก้ไขจำนวนไม่สำเร็จ", "กรอกจำนวนเป็นตัวเลขเท่านั้น")

def product_not_found():
    tkmsg.showinfo("เพิ่มสินค้าลงตะกร้าไม่สำเร็จ", "ไม่พบข้อมูลสินค้าในคลังสินค้า")

def version_info():
    tkmsg.showinfo("เวอร์ชั่นที่กำลังใช้งาน", "เวอร์ชั่น: BATA version 1.0 (ทดลอง)\nอัปเดตล่าสุดเมื่อ: 05/05/2022 00:00:00")

def fullscreen_error():
    tkmsg.showinfo('Fullscreen Error', 'Can not use F11 for fullscreen on BATA version.\nไม่สามารถใช้ F11 เพื่อเปิดเต็มหน้าจอได้ในเวอร์ชั่น BATA')

def forgot_password():
    tkmsg.showinfo("ลืมชื่อผู้ใช้ หรือรหัสผ่าน", "กรุณาติดต่อผู้ดูแลระบบเมื่อลืมชื่อผู้ใช้ หรือรหัสผ่าน")

def save_selling(total_price):
    winsound.PlaySound('SystemQuestion', winsound.SND_ASYNC)
    return tkmsg.askyesno("บันทึกการขาย", f"เงินทอน {total_price} บาท\nคุณต้องการบันทึกการขายหรือไม่\nYes (ใช่) / No (ไม่)")

def ask_logout():
    winsound.PlaySound('SystemQuestion', winsound.SND_ASYNC)
    return tkmsg.askyesno("ออกจากระบบ", "คุณต้องการออกจากระบบหรือไม่\nYes (ใช่) / No (ไม่)")

def ask_quit():
    winsound.PlaySound('SystemQuestion', winsound.SND_ASYNC)
    return tkmsg.askyesno("ออกจากโปรแกรม", "คุณต้องการออกจากโปรแกรมหรือไม่\nYes (ใช่) / No (ไม่)")

def ask_remove_product():
    winsound.PlaySound('SystemQuestion', winsound.SND_ASYNC)
    return tkmsg.askyesno("ลบสินค้าออกจากตะกร้า", "คุณต้องการลบสินค้าออกจากตะกร้าหรือไม่\nYes (ใช่) / No (ไม่)")

def login_success(user):
    tkmsg.showinfo("เข้าสู่ระบบสำเร็จ", "ยินดีต้อนรับคุณ %s เข้าสู่ระบบ" % (user))

def login_error(code, user = None):
    if code == 0:
        tkmsg.showerror("เกิดข้อผิดพลาด", "พบข้อมูลผู้ใช้จำนวน %s รายการซ้ำภายในระบบ\nกรุณาติดต่อผู้ดูแลระบบ" % (user))
    elif code == 1:
        tkmsg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "กรุณากรอกชื่อผู้ใช้ และรหัสผ่านให้ครบถ้วน")
    elif code == 2:
        tkmsg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "กรุณากรอกชื่อผู้ใช้")
    elif code == 3:
        tkmsg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "กรุณากรอกรหัสผ่าน")
    elif code == 4:
        tkmsg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "ชื่อผู้ใช้งาน หรือรหัสผ่านไม่ถูกต้อง")
    elif code == 5:
        tkmsg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "บัญชีถูกระงับการใช้งาน กรุณาติดต่อผู้ดูแลระบบ")
    else:
        tkmsg.showerror("เกิดข้อผิดพลาด", "เกิดข้อผิดพลาดที่ไม่รู้จัก กรุณาติดต่อผู้ดูแลระบบ")

def Hmmm():
    import assets.backend.what_is_pos as what_is_pos
    what_is_pos.Hmmm()

if __name__ == '__main__':
    import main
    main.App()