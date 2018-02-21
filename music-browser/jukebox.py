import sqlite3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect("music.db")
#Very nice example of OOPS

class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
        self["yscrollcommand"] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window)

        self.linked_box = None
        self.link_field = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        self.bind('<Double-Button-1>', self.on_select)
        if sort_order:
            self.sql_sort = " ORDER BY " + ", ".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def requery(self, link_value=None):
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)
            self.cursor.execute(sql, (link_value, ))
        else:
            self.cursor.execute(self.sql_select + self.sql_sort)

        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            index = int(self.curselection()[0])
            value = self.get(index)

            link_id = conn.execute(self.sql_select + " WHERE " + self.field + "=?", (value,)).fetchone()[1]
            self.linked_box.requery(link_id)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field


# def load_artists(listBox):
#     cursor = conn.cursor()
#     cursor.execute("SELECT name FROM artists ORDER BY name")
#     for item in cursor:
#         listBox.insert(tkinter.END, item[0])
#
#     cursor.close()
#
#
# def load_albums(event):
#     songLV.set(("Choose an album",))
#     lb = event.widget
#     index = int(lb.curselection()[0])
#     name = lb.get(index)
#
#     album_list = []
#     artist_id = conn.execute("SELECT artists._id FROM artists WHERE name = ?", (name,)).fetchone()[0]
#     for album in conn.execute("SELECT name FROM albums WHERE artist = ?", (artist_id,)):
#         album_list.append(album[0])
#     albumV.set(tuple(album_list))
#
#
# def load_songs(event):
#     lb = event.widget
#     index = int(lb.curselection()[0])
#     name = lb.get(index)
#     song_list = []
#     album_id = conn.execute("SELECT albums._id FROM albums WHERE name = ?", (name,)).fetchone()[0]
#     for song in conn.execute("SELECT title FROM songs WHERE album = ?", (album_id,)):
#         song_list.append(song[0])
#
#     songLV.set(tuple(song_list))
#

mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry("1024x768")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# === Labels ===========

tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

#====== Artists List Box =============

artistList = DataListBox(mainWindow, conn, "artists", "name")
artistList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30,0))
artistList.config(border=2, relief="sunken")
artistList.requery()
# artistList.bind('<Double-Button-1>', load_albums)

#=====Albums List Box
albumV = tkinter.Variable(mainWindow)
albumV.set(("Choose an artist",))
albumList = DataListBox(mainWindow, conn, "albums", "name", ("name", ))
albumList.grid(row=1, column=1, sticky="nsew", padx=(30,0))
albumList.config(border=2, relief="sunken")
artistList.link(albumList, 'artist')

# albumList.bind('<Double-Button-1>', load_songs)

#===== Songs List Box
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
songList.grid(row=1, column=2, sticky="nsew", padx=(30,0))
songList.config(border=2, relief="sunken")
albumList.link(songList, 'album')

#========== Main loop =====
# albumV.set(tuple(range(0,100)))
mainWindow.mainloop()
conn.close()
