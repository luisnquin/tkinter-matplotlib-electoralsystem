from tkinter import messagebox

import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.dataToSent, self.receivedData = [None, None, None], [None, None, None]
        self.countPre, self.countVicepre, self.flag = [], [], True

        if __name__=='__main__':
            self.connection = sqlite3.connect("db.db")
        else:
            self.connection = sqlite3.connect("databasef/db.db")
        
        self.cursor = self.connection.cursor()

    def insertOneData(self):
        if self.receivedData[0][0] == "0" and len(self.receivedData[0]) == 10:
            if self.receivedData[0] not in self.getIdentifications():
                self.cursor.execute("INSERT INTO votes VALUES(?, ?, ?)", self.receivedData)
                self.connection.commit()
            else:
                messagebox.showerror("Error", "La cédula introducida ya fue usada con anterioridad.")
                self.flag = False
        else:
            messagebox.showerror("Error", "La consulta no se pudo realizar, verifique si la cédula contiene 10 dígitos o si esta misma inicia con 0.")
            self.flag = False


    def getIdentifications(self):
        list_ids = []

        self.cursor.execute("SELECT citizenId FROM votes")
        for identifier in self.cursor.fetchall():
            list_ids.append(identifier[0])

        return list_ids

    def getCountPresidents(self):
        # ["Guillermo Lasso", "Segundo Andres Arauz", "Cynthia Viteri"]
        self.cursor.execute("SELECT COUNT(votePre) FROM votes WHERE votePre = 'Guillermo Lasso'")
        self.countPre.append(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(votePre) FROM votes WHERE votePre = 'Segundo Andres Arauz'")
        self.countPre.append(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(votePre) FROM votes WHERE votePre = 'Cynthia Viteri'")
        self.countPre.append(self.cursor.fetchone()[0])


    def getCountVicepre(self):
        # ["Doris Quiroz", "Ramiro Aguilar", "Jorge Glas"]
        self.cursor.execute("SELECT COUNT(voteVipre) FROM votes WHERE voteVipre = 'Doris Quiroz'")
        self.countVicepre.append(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(voteVipre) FROM votes WHERE voteVipre = 'Ramiro Aguilar'")
        self.countVicepre.append(self.cursor.fetchone()[0])

        self.cursor.execute("SELECT COUNT(voteVipre) FROM votes WHERE voteVipre = 'Jorge Glas'")
        self.countVicepre.append(self.cursor.fetchone()[0])


if __name__ == '__main__':
    DatabaseConnection()


"""self.cursor.execute("CREATE TABLE votes(citizenId VARCHAR NOT NULL PRIMARY KEY, votePre VARCHAR(60) NOT NULL, voteVipre VARCHAR(60) NOT NULL)")"""
