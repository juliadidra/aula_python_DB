"""Module providingFunction printing python version."""

import sqlite3

conn = sqlite3.connect('banco_salao')


table_cliente = """
create table if not exists cliente (
id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome_cliente VARCHAR(40) NOT NULL,
telefone_cliente VARCHAR(20) NOT NULL,
email_cliente VARCHAR(50) NOT NULL
);
"""
conn.execute(table_cliente)
conn.commit()

create_table_produto = """
CREATE TABLE IF NOT EXISTS produto (
id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
nome_produto VARCHAR(50) NOT NULL,
descricao_produto VARCHAR(100),
preco_produto DECIMAL(10,2) NOT NULL
);
"""
conn.execute(create_table_produto)
conn.commit()

create_table_servico = """
CREATE TABLE IF NOT EXISTS servico (
id_servico INTEGER PRIMARY KEY AUTOINCREMENT,
nome_servico VARCHAR(50) NOT NULL,
descricao_servico VARCHAR(100),
preco_servico DECIMAL(10,2) NOT NULL
);
"""
conn.execute(create_table_servico)
conn.commit()

create_table_agendamento_servico = """
CREATE TABLE IF NOT EXISTS agendamento_servico (
id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
id_cliente INTEGER NOT NULL,
id_servico INTEGER NOT NULL,
dia_agendamento DATE NOT NULL,
hora_agendamento TIME NOT NULL,
status_agendamento VARCHAR(10) NOT NULL,
 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
 FOREIGN KEY (id_servico) REFERENCES servico (id_servico)
);
"""
conn.execute(create_table_agendamento_servico)
conn.commit()

create_table_pagar_servico = """
create table if not exists pagar_servico (
id_pagamento_servico integer primary key autoincrement,
id_servico integer not null,
id_cliente integer not null,
forma_pagamento VARCHAR(20) not null,
foreign key (id_servico) references servico (id_servico),
foreign key (id_cliente) references cliente (id_cliente)
);
"""
conn.execute(create_table_pagar_servico)
conn.commit()

create_table_pagar_produto = """
create table if not exists pagar_produto (
id_pagamento_produto integer primary key autoincrement,
id_produto integer not null,
id_cliente integer not null,
forma_pagamento VARCHAR(20) not null,
foreign key (id_produto) references produto (id_produto),
foreign key (id_cliente) references cliente (id_cliente)
);
"""

cursor = conn.cursor()
conn.execute(create_table_pagar_produto)
conn.commit()

