import sqlite3 as sl

con = sl.connect("teste.db")

with con:
    con.execute("""
        create table testeBrabo
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor INTEGER NOT NULL,
            string VARCHA(30) NOT NULL
        );
        """)

query = 'INSERT INTO testeBrabo VALUES(?,?,?)'
data = [
    ('1', 1, "OI"),
    ('2', 2, "Tchau")
]
with con:
    con.executemany(query, data)

with con:
    retorno = con.execute("select * from testeBrabo;")
    for row in retorno:
        print(row)
