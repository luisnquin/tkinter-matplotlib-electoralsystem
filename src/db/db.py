import sqlite3

class DatabaseConnection:
    def __init__(self):
        if __name__=='__main__':
            self.connection = sqlite3.connect("db.db")
        else:
            self.connection = sqlite3.connect("db/db.db")
        
        self.cursor = self.connection.cursor()

        """self.cursor.execute("CREATE TABLE citizen (identification INTEGER NOT NULL PRIMARY KEY)")
        self.cursor.execute("CREATE TABLE candidates(ID VARCHAR NOT NULL PRIMARY KEY, fullname VARCHAR(50) NOT NULL PRIMARY KEY)")
        self.cursor.execute("CREATE TABLE votes(citizen INTEGER NOT NULL, candidatesId VARCHAR)")"""
        self.connection.commit()



if __name__ == '__main__':
    DatabaseConnection()