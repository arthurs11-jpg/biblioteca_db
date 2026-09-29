import sqlite3

def add_autores(nome):
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    nome = input("Digite o nome do autor(a): ")
    
    cursor.execute("INSERT INTO autores (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()



def listar_autores():
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")

    resultados = cursor.fetchall()

    for linha in resultados:
            print(f"id: {linha['id']} | nome: {linha['nome']}")
            #print(f"id: {linha[0]} | nome: {linha[1]}")

    conn.close()