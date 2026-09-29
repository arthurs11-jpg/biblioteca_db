import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela editoras
conn.execute("DROP TABLE IF EXISTS autores")