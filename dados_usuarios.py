import sqlite3

#conectando o banco de dados. caso não exista, o banco é criado
conn = sqlite3.connect("biblioteca.db")

#inserindo
conn.executemany("INSERT INTO usuarios(nome) VALUES (?)",
[("Arthur",), ("Bruna",), ("Lauryen",)])
conn.commit()