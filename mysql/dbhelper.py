import mysql.connector as connector
import csv

class DBHelper:
    def __init__(self, hostname, username, password, db):
        self.con = connector.connect(host=hostname,
                                    port='3306',
                                    user=username,
                                    password=password,
                                    database=db)

    def create_table(self):
        query = 'create table if not exists user(userID int primary key, username varchar(200), phone varchar(20))'
        cur = self.con.cursor()
        cur.execute(query)

    def populate_user_table(self, user, userid, phone):
        query = "INSERT INTO user (userID, username, phone) VALUES (%s, %s, %s)"
        vals = (123, "shahzadqadir", "1234567890")
        cur = self.con.cursor()
        cur.execute(query, vals)
        self.con.commit()
    
    def insert_from_file(self, filename):
        query = "INSERT INTO user (userID, username, phone) VALUES (%s, %s, %s)"
        cur = self.con.cursor()
        with open(filename) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                cur.execute(query, row)
        self.con.commit()

    def delete_user(self, userID):
        query = "DELETE FROM user WHERE userID=%s"
        vals = (userID,)
        cur = self.con.cursor()
        cur.execute(query, vals)
        self.con.commit()

    def update_username(self, userID, new_username):
        query = "UPDATE user SET username=%s WHERE userID=%s"
        vals = (new_username, userID)
        cur = self.con.cursor()
        cur.execute(query, vals)
        self.con.commit()