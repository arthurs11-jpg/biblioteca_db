import sqlite3

conn = sqlite3.connect("biblioteca.db")
conn.executemany("INSERT INTO usuarios(nome) VALUES (?)",
[("Arthur",), ("Bruna",), ("Lauryen",)])
conn.commit()