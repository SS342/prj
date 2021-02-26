import tkinter as tk
from tkinter import ttk
import sqlite3

class APP:
    def __init__(self, conn, cursor1):
        self.conn = conn
        self.cursor1 = cursor1

    def start_app(self):
        window = tk.Tk()
        window.geometry('300x300+100+100')

        window.title('admin')
        ##########Добавить "Tab Widget"#################
        style = ttk.Style(window)
        style.configure('uptab.TNotebook', tabposition='ws')

        notebook = ttk.Notebook(window, style='lefttab.TNotebook')
        f1 = tk.Frame(notebook, width=200, height=200)


        notebook.add(f1, text='delete')
        notebook.pack()
        ########################################################

        but = ttk.Button(f1,text = 'delete',command = self.delete)
        but.grid()
        window.mainloop()
    def delete(self):
        sql = 'DELETE FROM user'
        self.cursor1.execute(sql)
        self.conn.commit()
        print(1)