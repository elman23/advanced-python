# sudo apt-get install sqlite3
# sqlite3 test.db
# > select sqlite_version();
# > .exit


import sqlite3


def main():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select sqlite_version();')
    data = cursor.fetchone()
    print("SQLite version:", data[0])
    conn.close()


if __name__ == '__main__':
    main()