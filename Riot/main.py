import sqlite3
from sqlite3 import Cursor, OperationalError


def apaga_tabela(nome_tabela: str, cur: Cursor):
    try:
        cursor.execute(query)
        print('tabela DELETADA com sucesso')
    except OperationalError as erro:
        print('a não existe ainda :', erro)


if __name__ == '__main__':
    conn = sqlite3.connect("Banco de Dados de Teste")
    cursor = conn.cursor()

    query = 'DROP TABLE usuarios'
    

    cursor.execute(
        "INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Giovanna', '23'))
    cursor.execute(
        "INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Ana Julia', '19'))
    cursor.execute(
        "INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Victoria', '26'))
    cursor.execute(
        "INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Diovanna', '24'))
    cursor.execute(
        "INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Ariane', '23'))
    # usuario_id = conn.lastrowid
    conn.commit()

    cursor.execute("SELECT * FROM usuarios")
    lista = cursor.fetchall()
    print(lista, '\n')
    """for item in lista:
        print(f'id: {item[0]}')
        print(f'nome: {item[0]}')
        print(f'idade: {item[0]}')"""
    cursor.execute("UPDATE usuarios set nome='Ana elisa' Where nome='Diovanna'"
                   )

    conn.close()