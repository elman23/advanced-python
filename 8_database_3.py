# sudo apt-get install sqlite3
# sqlite3 test.db
# > select sqlite_version();
# > .exit


import sqlite3


def main():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        
        cursor.executescript("""
            drop table if exists pets;
            create table pets(id int, name text, price int);
            insert into pets values(1, "cat", 400);
            insert into pets values(2, "dog", 600);
        """)

        pets = (
            (3, "rabbit", 200), 
            (4, "bird", 100),
            (5, "goat", 500)
        )
        cursor.executemany("""
        insert into pets values(?, ?, ?);
        """,
        pets)

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