import sqlite3

def create_db():
    with open('tables.sql', 'r') as base:
        sql = base.read()

    with sqlite3.connect('tables.db') as connect:
        cur = connect.cursor()
        cur.executescript(sql)

# if __name__ == '__main__':
#     create_db()