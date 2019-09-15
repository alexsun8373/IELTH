import sqlite3

def creat_database(db_name,table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    # create table
    c.execute("CREATE TABLE "+ table_name +" (id integer primary key,org text,act text,error_mark integer,remembered integer)")
    c.execute("INSERT INTO " + table_name + " VALUES (1,'Buy','BUY',1,1)")
    conn.commit()
    for row in c.execute('SELECT * FROM ' + table_name + ' ORDER BY id'):
        print(row)
    conn.close


def add_table(db_name, sheet_name, list_ele):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # create table
    c.execute("CREATE TABLE " + sheet_name + " (id integer primary key," + sheet_name + " text)")

    j = 1
    c.executemany("INSERT INTO " + sheet_name + " VALUES (?,?)", list_ele)
    conn.commit()
    conn.close


def delete_table(db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    # DELETE table
    c.execute("DROP TABLE " + table_name)

    conn.commit()
    conn.close
