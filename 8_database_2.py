# sudo apt-get install sqlite3
# sqlite3 test.db
# > select sqlite_version();
# > .exit


import sqlite3

from itsdangerous import exc


def main():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('create table pets(id int, name text, price int);')
        cursor.execute('insert into pets values(1, "cat", 400);')
        cursor.execute('insert into pets values(2, "dog", 600);')
        cursor.execute('insert into pets values(3, "rabbit", 200);')
        cursor.execute('insert into pets values(4, "bird", 100);')
        conn.commit()
        cursor.execute('select * from pets;')
        data = cursor.fetchall()
        for row in data:
            print(row)
    except sqlite3.Error:
        if conn:
            print("Error! Rolling back.")
            conn.rollback()
    finally:
        if conn:
            conn.close()



if __name__ == '__main__':
    main()