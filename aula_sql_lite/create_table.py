import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

create_table_query = """
    create table if not exists clients (
    id integer not null primary key autoincrement,
    nome text not null,
    idade integer,
    cpf text
    );
"""

conn.execute(create_table_query)
conn.commit()

# criando uma lista de dados
lista = [(
    'Fabio', 23, '44444444444'),
    ('Joao', 21, '55555555555'),
    ('Xavier', 24, '66666666666')]


# inserindo dados na tabela
cursor.executemany("""
    INSERT INTO clients (nome, idade, cpf)
    VALUES (?,?,?)
""", lista)

conn.commit()
conn.close()
