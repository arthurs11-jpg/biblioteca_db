import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela usuarios
conn.execute("DROP TABLE IF EXISTS usuarios")

#cria a tabela usuarios
conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

#inserindo os registros na tabela usuarios


conn = sqlite3.connect("biblioteca.db")
conn.row_factory = sqlite3.Row

#cria um cursor (objeto para interagir com o banco)
cursor = conn.cursor()

#executa o sql
cursor.execute("SELECT * FROM usuarios")

#pega os registros e guarda na variável resultados
resultados = cursor.fetchall()

#percorre os registros que retornaram
for linha in resultados:
    print(f"id: {linha['id']} | nome: {linha['nome']}")
    #print(f"id: {linha[0]} | nome: {linha[1]}")

#fecha a conexão
conn.close()