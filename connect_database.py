import sqlite3

def database_execute(sql):
    global conn, cursor
    conn = sqlite3.connect('assets\\backend\\database\\minipos.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    data_fetched = cursor.fetchall()
    conn.close()
    return data_fetched

if __name__ == '__main__':
    import main
    main.App()