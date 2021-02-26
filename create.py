import sqlite3

class DataBase:
    def __init__(self,conn,cursor1,j2 = 0):
        self.conn = conn
        self.cursor1 = cursor1
        self.j2 = j2
    def do(self):
        j2 = 0

        self.cursor1.execute("""CREATE TABLE IF NOT EXISTS user(
            ID   STRING,
            name STRING,
            surname STRING,
            middle_name STRING,
            years STRING,
            time_for_play STRING,
            youtube STRING,
            streams STRING,
            becose STRING);
        """)
        char_list = []
        IDD = '0'
        test = 'test'
        self.cursor1.execute("SELECT * FROM user")
        if self.cursor1.fetchall():
            pass
        else:

            self.cursor1.execute("insert into user values ('" + IDD + "','" + test + "','" + test + "','" + test + "','" + test + "','" + test + "','" + test + "','" + test + "','" + test + "')")

            self.conn.commit()
            print(1)
        self.cursor1.execute("SELECT ID FROM user")
        for row in self.cursor1.fetchall():
            print(row)
            char_list.append(row)
            print(char_list)
        string = char_list[-1]
        for c in string:
            char_list.append(c)
        self.j2 = char_list[-1]
        self.j2 = self.j2 + 1
    def save(self,id,name,surname,middle_name,years_old,time_for_play,youtube,streams,becose):
        self.id = id
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.years_old = years_old
        self.time_for_play = time_for_play
        self.youtube = youtube
        self.streams = streams
        self.becose = becose
        self.cursor1.execute("insert into user values ('" + self.id + "','" + self.name + "','" + self.surname + "','" + self.middle_name + "','" + self.years_old + "','" + self.time_for_play + "','" + self.youtube + "','" + self.streams + "','" + self.becose + "')")
        self.conn.commit()


