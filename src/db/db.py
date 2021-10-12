import sqlite3

class DatabaseConnection:
    def __init__(self):
        if __name__=='__main__':
            self.connection = sqlite3.connect("db.db")
        else:
            self.connection = sqlite3.connect("db/db.db")
        
        self.cursor = self.connection.cursor()
        


if __name__ == '__main__':
    DatabaseConnection()