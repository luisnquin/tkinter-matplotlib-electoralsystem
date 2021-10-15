import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.dataToSent, self.receivedData = [None, None, None], [None, None, None]
        self.countPre, self.countVicepre = [], []

        if __name__=='__main__':
            self.connection = sqlite3.connect("db.db")
        else:
            self.connection = sqlite3.connect("db/db.db")
        
        self.cursor = self.connection.cursor()
        self.getCountPresidents()
        self.getCountVicepre()

    def insertOne(self):
        self.cursor.execute("INSERT INTO votes VALUES(?, ?, ?)", self.receivedData)
        self.connection.commit()

    def getData(self):
        self.cursor.execute("SELECT * FROM votes")
        self.dataToSent = self.cursor.fetchall()

    def getCountPresidents(self):
        # ["Guillermo Lasso", "Segundo Andres Arauz", "Cynthia Viteri"]
        self.cursor.execute("SELECT COUNT(votePre) FROM votes WHERE votePre = 'Guillermo Lasso'")
        self.countPre.append(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(votePre) FROM votes WHERE votePre = 'Segundo Andres Arauz'")
        self.countPre.append(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(votePre) FROM votes WHERE votePre = 'Cynthia Viteri'")
        self.countPre.append(self.cursor.fetchone()[0])

        print(self.countPre)

    def getCountVicepre(self):
        # ["Doris Quiroz", "Ramiro Aguilar", "Jorge Glas"]
        self.cursor.execute("SELECT COUNT(voteVipre) FROM votes WHERE voteVipre = 'Doris Quiroz'")
        self.countVicepre.append(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(voteVipre) FROM votes WHERE voteVipre = 'Ramiro Aguilar'")
        self.countVicepre.append(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(voteVipre) FROM votes WHERE voteVipre = 'Jorge Glas'")
        self.countVicepre.append(self.cursor.fetchone()[0])

        print(self.countVicepre)
        

    def deleteData(self):
        self.cursor.execute("DELETE FROM votes WHERE citizenId = ?")
        self.connection.commit()


if __name__ == '__main__':
    DatabaseConnection()


"""self.cursor.execute("CREATE TABLE votes(citizenId INTEGER NOT NULL PRIMARY KEY, votePre VARCHAR(60) NOT NULL, voteVipre VARCHAR(60) NOT NULL)")"""