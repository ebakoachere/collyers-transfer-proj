import sqlite3


class Data:
    def __init__(self):
        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()

        '''self.c.execute("""CREATE TABLE customers(
                        CID INT PRIMARY KEY NOT NULL,
                       firstName VARCHAR(20) NOT NULL,
                       secondName VARCHAR(20) NOTNULL,
                       number INT NOT NULL,
                       showdate VARCHAR(8) NOT NULL
                       );""")'''

    def enter(self, CID, firstName, secondName, number, showdate):
        print('hello')

        self.c.execute("INSERT INTO customers VALUES(?, ?, ?, ?)", (CID, firstName, secondName, number, showdate))
        self.conn.commit()
        self.c.execute("SELECT * FROM customers ")


