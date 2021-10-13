import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.dataToSent, self.receivedData = [None, None, None], [None, None, None]

        if __name__=='__main__':
            self.connection = sqlite3.connect("db.db")
        else:
            self.connection = sqlite3.connect("db/db.db")
        
        self.cursor = self.connection.cursor()

    def insertOne(self):
        self.cursor.execute("INSERT INTO votes VALUES(?, ?, ?)", self.receivedData)
        self.connection.commit()

    def getData(self):
        self.cursor.execute("SELECT * FROM votes")
        self.dataToSent = self.cursor.fetchall()

    def deleteData(self):
        self.cursor.execute("DELETE FROM votes WHERE citizenId = ?")
        self.connection.commit()


if __name__ == '__main__':
    DatabaseConnection()


"""self.cursor.execute("CREATE TABLE votes(citizenId INTEGER NOT NULL PRIMARY KEY, votePre VARCHAR(60) NOT NULL, voteVipre VARCHAR(60) NOT NULL)")"""