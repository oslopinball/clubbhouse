#!/usr/bin/env python3

import sqlite3

class Member:
    def __init__(self, database):
        self.database = database
        self.connect()

    def __del__(self):
        self.close()

    def connect(self):
        print("Member: Connecting to database: " + self.database)
        self.db = sqlite3.connect(self.database)
        self.cursor = self.db.cursor()

    def close(self):
        print("Member: Closing database: " + self.database)
        self.db.close()

    def create(self):
        print("Member: Creating database: " + self.database)

    def importCSV(self, csv):
        print("Member: Importing CSV file: " + csv)

    def getID(self, id):
        id = str(id)

        print("Member: Getting ID: " + id)

        sql = 'SELECT * FROM members WHERE card_id="' + id + '"'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()

        if data:
            member = data[1] + " " + data[2] + " [" + data[3] + "]"
        else:
            member = "ERROR"

        return member

    def getTAG(self, name):
        print("Member: Getting TAG for name: " + name)

        members = []

        sql = "SELECT * FROM members WHERE firstname LIKE '%" + name + "%' OR lastname LIKE '%" + name + "%'"
        for member in self.db.execute(sql):
            m = member[1] + " " + member[2] + " [" + member[3] + "]"
            members.append(m)

        return members

    def getMobile(self, tag):
        tag = tag.upper()

        print("Member: Getting mobile for TAG: " + tag)

        sql = 'SELECT mobile FROM members WHERE tag="' + tag + '"'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()

        if data:
            mobile = data[0]
        else:
            mobile = "Fant ikke"

        return mobile

    def getEmail(self, tag):
        tag = tag.upper()

        print("Member: Getting e-mail for TAG: " + tag)

        sql = 'SELECT email FROM members WHERE tag="' + tag + '"'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()

        if data:
            email = data[0]
        else:
            email = "Fant ikke"

        return email
